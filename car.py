from abc import ABC, abstractmethod
from serviceable import Serviceable
from engine import Engine
from battery import Battery

class Car(Serviceable, ABC):
    def __init__(self, engine: Engine, battery: Battery):
        self.__engine = engine
        self.__battery = battery

    @property
    def engine(self):
        return self.__engine
    
    @engine.setter
    def engine(self, engine):
        self.__engine = engine

    @property
    def battery(self):
        return self.__battery
    
    @battery.setter
    def battery(self, battery):
        return self.__battery

    @abstractmethod
    def needs_service(self):
        pass
