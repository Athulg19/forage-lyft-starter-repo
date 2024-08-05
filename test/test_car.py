import unittest
from datetime import datetime, timedelta
from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine
from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery
from tires.concrete_tires import ConcreteTires
from car import Car

class TestCar(unittest.TestCase):

    def test_capulet_engine_needs_service(self):
        engine = CapuletEngine(current_mileage=35000, last_service_mileage=0)
        self.assertTrue(engine.needs_service())

    def test_capulet_engine_no_service_needed(self):
        engine = CapuletEngine(current_mileage=25000, last_service_mileage=0)
        self.assertFalse(engine.needs_service())

    def test_willoughby_engine_needs_service(self):
        engine = WilloughbyEngine(current_mileage=65000, last_service_mileage=0)
        self.assertTrue(engine.needs_service())

    def test_willoughby_engine_no_service_needed(self):
        engine = WilloughbyEngine(current_mileage=55000, last_service_mileage=0)
        self.assertFalse(engine.needs_service())

    def test_sternman_engine_needs_service(self):
        engine = SternmanEngine(warning_light_is_on=True)
        self.assertTrue(engine.needs_service())

    def test_sternman_engine_no_service_needed(self):
        engine = SternmanEngine(warning_light_is_on=False)
        self.assertFalse(engine.needs_service())

    def test_spindler_battery_needs_service(self):
        last_service_date = datetime.today().date() - timedelta(days=800)
        battery = SpindlerBattery(last_service_date=last_service_date, current_date=datetime.today().date())
        self.assertTrue(battery.needs_service())

    def test_spindler_battery_no_service_needed(self):
        last_service_date = datetime.today().date() - timedelta(days=700)
        battery = SpindlerBattery(last_service_date=last_service_date, current_date=datetime.today().date())
        self.assertFalse(battery.needs_service())

    def test_nubbin_battery_needs_service(self):
        last_service_date = datetime.today().date() - timedelta(days=1500)
        battery = NubbinBattery(last_service_date=last_service_date, current_date=datetime.today().date())
        self.assertTrue(battery.needs_service())

    def test_nubbin_battery_no_service_needed(self):
        last_service_date = datetime.today().date() - timedelta(days=1400)
        battery = NubbinBattery(last_service_date=last_service_date, current_date=datetime.today().date())
        self.assertFalse(battery.needs_service())

    def test_concrete_tires_needs_service(self):
        tires = ConcreteTires(wear_sensors=[0.9, 0.8, 0.8, 0.8])
        self.assertTrue(tires.needs_service())

    def test_concrete_tires_no_service_needed(self):
        tires = ConcreteTires(wear_sensors=[0.8, 0.8, 0.8, 0.8])
        self.assertFalse(tires.needs_service())

    def test_car_needs_service_due_to_engine(self):
        engine = CapuletEngine(current_mileage=35000, last_service_mileage=0)
        battery = SpindlerBattery(last_service_date=datetime.today().date() - timedelta(days=700), current_date=datetime.today().date())
        tires = ConcreteTires(wear_sensors=[0.8, 0.8, 0.8, 0.8])
        car = Car(engine=engine, battery=battery, tires=tires)
        self.assertTrue(car.needs_service())

    def test_car_needs_service_due_to_battery(self):
        engine = CapuletEngine(current_mileage=25000, last_service_mileage=0)
        battery = SpindlerBattery(last_service_date=datetime.today().date() - timedelta(days=800), current_date=datetime.today().date())
        tires = ConcreteTires(wear_sensors=[0.8, 0.8, 0.8, 0.8])
        car = Car(engine=engine, battery=battery, tires=tires)
        self.assertTrue(car.needs_service())

    def test_car_needs_service_due_to_tires(self):
        engine = CapuletEngine(current_mileage=25000, last_service_mileage=0)
        battery = SpindlerBattery(last_service_date=datetime.today().date() - timedelta(days=700), current_date=datetime.today().date())
        tires = ConcreteTires(wear_sensors=[0.9, 0.8, 0.8, 0.8])
        car = Car(engine=engine, battery=battery, tires=tires)
        self.assertTrue(car.needs_service())

    def test_car_no_service_needed(self):
        engine = CapuletEngine(current_mileage=25000, last_service_mileage=0)
        battery = SpindlerBattery(last_service_date=datetime.today().date() - timedelta(days=700), current_date=datetime.today().date())
        tires = ConcreteTires(wear_sensors=[0.8, 0.8, 0.8, 0.8])
        car = Car(engine=engine, battery=battery, tires=tires)
        self.assertFalse(car.needs_service())

if __name__ == '__main__':
    unittest.main()
