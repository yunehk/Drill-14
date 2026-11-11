from pico2d import open_canvas, delay, close_canvas
from pathlib import Path
import os
import game_framework

import play_mode as start_mode

def main():
    previous_directory = Path.cwd()
    os.chdir(Path(__file__).resolve().parent)
    try:
        open_canvas(1600, 600)
        try:
            game_framework.run(start_mode)
        finally:
            close_canvas()
    finally:
        os.chdir(previous_directory)


if __name__ == '__main__':
    main()

