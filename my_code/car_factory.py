from my_code.battery_types.nubbin_battery import NubbinBattery
from my_code.battery_types.spindler_battery import SpindlerBattery
from my_code.car import Car
from my_code.engines.capulet_engine import CapuletEngine
from my_code.engines.sternman_engine import SternmanEngine
from my_code.engines.willoughby_engine import WilloughbyEngine
from my_code.tires.carrigan_tire import CarriganTire
from my_code.tires.octoprime_tire import OctoprimeTire


class CarFactory:
    def __init__(self):
        pass

    @staticmethod
    def create_calliope(current_date, last_service_date, current_milage, last_service_milage, tire_array):
        return Car(CapuletEngine(last_service_milage, current_milage), SpindlerBattery(last_service_date, current_date),
                   CarriganTire(tire_array))

    @staticmethod
    def create_glissade(current_date, last_service_date, current_milage, last_service_milage, tire_array):
        return Car(WilloughbyEngine(last_service_milage, current_milage),
                   SpindlerBattery(last_service_date, current_date), CarriganTire(tire_array))

    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_on, tire_array):
        return Car(SternmanEngine(warning_light_on),
                   SpindlerBattery(last_service_date, current_date), CarriganTire(tire_array))

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_milage, last_service_milage, tire_array):
        return Car(WilloughbyEngine(last_service_milage, current_milage),
                   NubbinBattery(last_service_date, current_date), OctoprimeTire(tire_array))

    @staticmethod
    def create_thovex(current_date, last_service_date, current_milage, last_service_milage, tire_array):
        return Car(CapuletEngine(last_service_milage, current_milage),
                   NubbinBattery(last_service_date, current_date), OctoprimeTire(tire_array))
