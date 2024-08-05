import unittest
from engine.capulet_engine import CapuletEngine

class TestCapuletEngine(unittest.TestCase):
    def test_needs_service_true(self):
        engine = CapuletEngine(current_mileage=31000, last_service_mileage=0)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        engine = CapuletEngine(current_mileage=29000, last_service_mileage=0)
        self.assertFalse(engine.needs_service())

if __name__ == '__main__':
    unittest.main()
