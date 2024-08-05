
import unittest
from datetime import date
from battery.spindler_battery import SpindlerBattery

class TestSpindlerBattery(unittest.TestCase):
    def test_needs_service_true(self):
        battery = SpindlerBattery(last_service_date=date.fromisoformat("2017-01-01"), current_date=date.fromisoformat("2020-01-02"))
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        battery = SpindlerBattery(last_service_date=date.fromisoformat("2019-01-01"), current_date=date.fromisoformat("2021-12-31"))
        self.assertFalse(battery.needs_service())

if __name__ == '__main__':
    unittest.main()
