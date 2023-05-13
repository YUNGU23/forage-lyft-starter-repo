from abc import ABC
from engine import Engine

class WilloughbyEngine(Engine, ABC):
    def __init__(self, last_service_mileage, current_mileage):
        self.__last_service_mileage = last_service_mileage
        self.__current_mileage = current_mileage
    
    @property
    def last_service_mileage(self):
        return self.__last_service_mileage
    
    @last_service_mileage.setter
    def last_service_mileage(self, value):
        self.__last_service_mileage = value
    
    @property
    def current_mileage(self):
        return self.__current_mileage
    
    @current_mileage.setter
    def current_mileage(self, value):
        self.__current_mileage = value


    def engine_should_be_serviced(self):
        return self.__current_mileage - self.__last_service_mileage > 60000
