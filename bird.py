"""Drill 14: time-based ten-bird flight."""
from pathlib import Path

FRAME_COUNT = 14
ANIMATION_FPS = 14.0
DRAW_WIDTH, DRAW_HEIGHT = 100, 92
BIRD_COUNT = 10
CANVAS_WIDTH, CANVAS_HEIGHT = 1600, 600


def frame_rect(frame, width, height):
    """Read 14 cells in row order, converting to bottom-origin clips."""
    row, column = divmod(int(frame) % FRAME_COUNT, 5)
    left, right = column * width // 5, (column + 1) * width // 5
    top, bottom = row * height // 3, (row + 1) * height // 3
    return left, height - bottom, right - left, bottom - top


def load_bird_image():
    from pico2d import load_image
    return load_image(str(Path(__file__).with_name('bird_animation.png')))


class Bird:
    def __init__(self, image, x, y, speed=180.0, direction=1, frame=0.0):
        self.image = image
        self.x, self.y = x, y
        self.speed, self.direction = speed, direction
        self.frame = float(frame)

    def animate(self, dt):
        self.frame = (self.frame + ANIMATION_FPS * dt) % FRAME_COUNT

    def update(self, dt=None, canvas_width=CANVAS_WIDTH):
        if dt is None:
            import game_framework
            from pico2d import get_canvas_width
            dt = game_framework.frame_time
            canvas_width = get_canvas_width()
        self.animate(dt)
        self.x += self.direction * self.speed * dt
        self.reflect_at_edges(canvas_width)

    def reflect_at_edges(self, canvas_width):
        left, right = DRAW_WIDTH / 2, canvas_width - DRAW_WIDTH / 2
        if right <= left:
            raise ValueError('Canvas must be wider than a bird')
        span = right - left
        phase = (self.x - left) % (2 * span)
        if self.x <= left or self.x >= right:
            if phase == 0:
                self.x, self.direction = left, 1
            elif phase == span:
                self.x, self.direction = right, -1
            elif phase < span:
                self.x = left + phase
            else:
                self.x = right - (phase - span)
                self.direction *= -1

    def draw(self):
        clip = frame_rect(self.frame, self.image.w, self.image.h)
        self.image.clip_composite_draw(
            *clip, 0, 'h' if self.direction < 0 else '',
            self.x, self.y, DRAW_WIDTH, DRAW_HEIGHT)
