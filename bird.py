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
