import unittest

from clockapi import Clock
from clockdrift import ClockSync


class TestClockSync(unittest.TestCase):
    def test_first_sample(self):
        sync = ClockSync()
        self.assertEqual(sync.observe(100)["offset"], 100)

    def test_samples_counted(self):
        sync = ClockSync()
        sync.observe(1)
        self.assertEqual(sync.stats()["samples"], 1)

    def test_stats_shape(self):
        self.assertIn("threshold", ClockSync().stats())

    def test_last_tracks_sample(self):
        sync = ClockSync()
        sync.observe(5)
        self.assertEqual(sync.stats()["last"], 5)

    def test_clock_wraps_sync(self):
        clock = Clock()
        clock.observe(7)
        self.assertEqual(clock.sync.stats()["offset"], 7)


if __name__ == "__main__":
    unittest.main()
