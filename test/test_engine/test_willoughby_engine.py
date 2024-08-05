import unittest
from engine.willoughby_engine import WilloughbyEngine

class TestWilloughbyEngine(unittest.TestCase):
    def test_needs_service_true(self):
        engine = WilloughbyEngine(current_mileage=61000, last_service_mileage=0)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        engine = WilloughbyEngine(current_mileage=59000, last_service_mileage=0)
        self.assertFalse(engine.needs_service())

if __name__ == '__main__':
    unittest.main()
