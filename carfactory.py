from car import Car
from engine import Engine, CapuletEngine, WilloughbyEngine, SternmanEngine 
from battery import battery, SpindleBattery, NubbinBattery
from datetime import date

class CarFactory(Car):
    def create_calliope(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        if CapuletEngine.need_service(last_service_mileage, current_mileage):
            print("CapuletEngine needs a service! ") 
            
        if SpindleBattery.needs_service(last_service_date, current_date):
            print("SpindleBattery needs a service! ")

    def create_glissade(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        if WilloughbyEngine.need_service(last_service_mileage, current_mileage):
            print("WilloughbyEngine needs a service! ") 
            
        if SpindleBattery.needs_service(last_service_date, current_date):
            print("SpindleBattery needs a service! ")

    def create_palindrome(current_date: date, last_service_date: date, warning_light_on: bool):
        if SternmanEngine.need_service(warning_light_on):
            print("SternmanEngine needs a service! ") 
            
        if SpindleBattery.needs_service(last_service_date, current_date):
            print("SpindleBattery needs a service! ")

    def create_rorschach(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        if WilloughbyEngine.need_service(last_service_mileage, current_mileage):
            print("WilloughbyEngine needs a service! ") 
            
        if NubbinBattery.needs_service(last_service_date, current_date):
            print("NubbinBattery needs a service! ")

    def create_thovex(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        if CapuletEngine.need_service(last_service_mileage, current_mileage):
            print("CapuletEngine needs a service! ") 
            
        if NubbinBattery.needs_service(last_service_date, current_date):
            print("NubbinBattery needs a service! ")

if __name__ == "__main__":
    pass

