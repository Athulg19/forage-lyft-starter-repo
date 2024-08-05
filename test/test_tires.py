
import unittest
from tires.carrigan_tires import CarriganTires
from tires.octoprime_tires import OctoprimeTires

class TestCarriganTires(unittest.TestCase):
    def test_needs_service_true(self):
        tires = CarriganTires(wear_sensors=[0.9, 0.1, 0.1, 0.1])
        self.assertTrue(tires.needs_service())

    def test_needs_service_false(self):
        tires = CarriganTires(wear_sensors=[0.1, 0.2, 0.3, 0.4])
        self.assertFalse(tires.needs_service())

class TestOctoprimeTires(unittest.TestCase):
    def test_needs_service_true(self):
        tires = OctoprimeTires(wear_sensors=[0.75, 0.75, 0.75, 0.75])
        self.assertTrue(tires.needs_service())

    def test_needs_service_false(self):
        tires = OctoprimeTires(wear_sensors=[0.5, 0.5, 0.5, 0.5])
        self.assertFalse(tires.needs_service())

if __name__ == '__main__':
    unittest.main()
