import unittest
from engine.sternman_engine import SternmanEngine

class TestSternmanEngine(unittest.TestCase):
    def test_warning_light_on(self):
        engine = SternmanEngine(warning_light_is_on=True)
        self.assertTrue(engine.needs_service())

    def test_warning_light_off(self):
        engine = SternmanEngine(warning_light_is_on=False)
        self.assertFalse(engine.needs_service())

if __name__ == '__main__':
    unittest.main()
