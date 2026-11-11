import random
import unittest
from unittest.mock import Mock
from bird import Bird, frame_rect, FRAME_COUNT
from bird_main import create_flock


class BirdTests(unittest.TestCase):
    def test_sprite_rectangles(self):
        rects = [frame_rect(i, 918, 506) for i in range(FRAME_COUNT)]
        self.assertEqual(len(set(rects)), 14)
        self.assertEqual(rects[0], (0, 338, 183, 168))
        self.assertEqual(rects[-1], (550, 0, 184, 169))
        self.assertEqual(frame_rect(14, 918, 506), rects[0])
        for x, y, w, h in rects:
            self.assertTrue(0 <= x < x + w <= 918)
            self.assertTrue(0 <= y < y + h <= 506)

    def test_time_partition_independence(self):
        for direction in (-1, 1):
            a = Bird(None, 500, 100, direction=direction)
            b = Bird(None, 500, 100, direction=direction)
            a.update(19.25)
            for _ in range(1155):
                b.update(1 / 60)
            self.assertAlmostEqual(a.x, b.x)
            self.assertAlmostEqual(a.frame, b.frame)
            self.assertEqual(a.direction, b.direction)

    def test_reflections(self):
        for x, direction, expected in ((1140, 1, -1), (60, -1, 1)):
            bird = Bird(None, x, 100, speed=100, direction=direction)
            bird.update(0.2)
            self.assertAlmostEqual(bird.x, x)
            self.assertEqual(bird.direction, expected)
            bird.update(10000)
            self.assertTrue(50 <= bird.x <= 1150)

    def test_flock_and_facing(self):
        image = Mock(w=918, h=506)
        flock = create_flock(image, random.Random(14))
        self.assertEqual(len(flock), 10)
        self.assertEqual(len({b.y for b in flock}), 10)
        self.assertTrue(all(b.image is image for b in flock))
        for direction, flip in ((1, ''), (-1, 'h')):
            flock[0].direction = direction
            flock[0].draw()
            self.assertEqual(image.clip_composite_draw.call_args.args[5], flip)


if __name__ == '__main__':
    unittest.main()
