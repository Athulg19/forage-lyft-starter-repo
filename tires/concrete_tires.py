from tires.tires import Tires

class ConcreteTires(Tires):
    def __init__(self, wear_sensors: list):
        self.wear_sensors = wear_sensors

    def needs_service(self) -> bool:
        return any(sensor >= 0.9 for sensor in self.wear_sensors)
