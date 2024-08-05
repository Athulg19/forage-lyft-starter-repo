import unittest
from datetime import date
from battery.nubbin_battery import NubbinBattery

class TestNubbinBattery(unittest.TestCase):
    def test_needs_service_true(self):
        battery = NubbinBattery(last_service_date=date.fromisoformat("2016-01-25"), current_date=date.fromisoformat("2020-05-15"))
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        battery = NubbinBattery(last_service_date=date.fromisoformat("2019-01-10"), current_date=date.fromisoformat("2020-05-15"))
        self.assertFalse(battery.needs_service())

if __name__ == '__main__':
    unittest.main()
