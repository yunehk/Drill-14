"""Flock creation and compatibility entry point for the shared boy scene."""
import random
from bird import (Bird, BIRD_COUNT, CANVAS_WIDTH, DRAW_WIDTH, FRAME_COUNT)


def create_flock(image, rng=None):
    rng = rng or random.Random()
    return [Bird(image,
                 rng.uniform(DRAW_WIDTH / 2, CANVAS_WIDTH - DRAW_WIDTH / 2),
                 240 + i * 30, rng.uniform(140, 240),
                 rng.choice((-1, 1)), rng.uniform(0, FRAME_COUNT))
            for i in range(BIRD_COUNT)]


def main():
    from main import main as run_scene
    run_scene()


if __name__ == '__main__':
    main()
