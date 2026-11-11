"""Standalone Drill 14 entry point."""
import random
import time
import pico2d
from bird import (Bird, BIRD_COUNT, CANVAS_WIDTH, CANVAS_HEIGHT,
                  DRAW_WIDTH, FRAME_COUNT, load_bird_image)


def create_flock(image, rng=None):
    rng = rng or random.Random()
    return [Bird(image,
                 rng.uniform(DRAW_WIDTH / 2, CANVAS_WIDTH - DRAW_WIDTH / 2),
                 65 + i * 62, rng.uniform(140, 240),
                 rng.choice((-1, 1)), rng.uniform(0, FRAME_COUNT))
            for i in range(BIRD_COUNT)]


def render(flock):
    pico2d.clear_canvas()
    for bird in flock:
        bird.draw()
    pico2d.update_canvas()


def main():
    pico2d.open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT, sync=True)
    try:
        flock = create_flock(load_bird_image())
        previous = time.perf_counter()
        while handle_events():
            now = time.perf_counter()
            dt = now - previous
            previous = now
            for bird in flock:
                bird.update(dt)
            render(flock)
            pico2d.delay(0.001)
    finally:
        pico2d.close_canvas()


def handle_events():
    for event in pico2d.get_events():
        if event.type == pico2d.SDL_QUIT:
            return False
        if event.type == pico2d.SDL_KEYDOWN and event.key == pico2d.SDLK_ESCAPE:
            return False
    return True


if __name__ == '__main__':
    main()
