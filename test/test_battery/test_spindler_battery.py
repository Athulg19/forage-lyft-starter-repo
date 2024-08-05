import unittest
from datetime import date
from battery.spindler_battery import SpindlerBattery

class TestSpindlerBattery(unittest.TestCase):
    def test_needs_service_true(self):
        battery = SpindlerBattery(last_service_date=date.fromisoformat("2018-05-15"), current_date=date.fromisoformat("2020-05-16"))
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        battery = SpindlerBattery(last_service_date=date.fromisoformat("2019-05-15"), current_date=date.fromisoformat("2020-05-14"))
        self.assertFalse(battery.needs_service())

if __name__ == '__main__':
    unittest.main()
