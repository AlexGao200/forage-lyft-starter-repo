from battery_models.nubbin_battery import RubbinBattery
from battery_models.spindler_battery import SpindlerBattery
from car import Car
from datetime import date

from engine_models.capulet_engine import CapuletEngine
from engine_models.capulet_engine import CapuletEngine
from engine_models.sternman_engine import SternmanEngine
from engine_models.willoughby_engine import WilloughbyEngine


class CarFactory():
    @staticmethod
    def create_calliope(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        capulet_engine = CapuletEngine(current_mileage, last_service_mileage)
        spindler_battery = SpindlerBattery(last_service_date, current_date)
        return Car(capulet_engine, spindler_battery)
    
    @staticmethod
    def create_glissade(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        willoughby_engine = WilloughbyEngine(current_mileage, last_service_mileage)
        spindler_battery = SpindlerBattery(last_service_date, current_date)
        return Car(willoughby_engine, spindler_battery)
    
    @staticmethod
    def create_palindrome(self, current_date: date, last_service_date: date, warning_light_on: bool):
        sternman_engine = SternmanEngine(warning_light_on)
        spindler_battery = SpindlerBattery(last_service_date, current_date) 
        return Car(sternman_engine, spindler_battery)
    
    @staticmethod
    def create_rorschach(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        willoughby_engine = WilloughbyEngine(current_mileage, last_service_mileage)
        nubbin_battey = RubbinBattery(current_date, last_service_date)
        return Car(willoughby_engine, nubbin_battey)

    @staticmethod
    def create_thovex(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        capulet_engine = CapuletEngine(current_mileage, last_service_mileage) 
        nubbin_battey = RubbinBattery(current_date, last_service_date)
        return Car(capulet_engine, nubbin_battey) 