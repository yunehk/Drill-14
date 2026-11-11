"""Drill 14: time-based ten-bird flight."""
from pathlib import Path

FRAME_COUNT = 14
ANIMATION_FPS = 14.0
DRAW_WIDTH, DRAW_HEIGHT = 100, 92
BIRD_COUNT = 10
CANVAS_WIDTH, CANVAS_HEIGHT = 1200, 700


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

    def update(self, dt, canvas_width=CANVAS_WIDTH):
        self.animate(dt)
        self.x += self.direction * self.speed * dt
        self.reflect_at_edges(canvas_width)
