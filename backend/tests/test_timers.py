from timers import GeneralTimer
import time
import unittest

class TimerTests(unittest.TestCase):

    def test_general_timer(self):
        timer = GeneralTimer()

        with timer:
            time.sleep(1)
        
        self.assertGreater(timer.expired_milliseconds, 0)
        self.assertGreater(timer.expired_seconds, 0)