from abc import ABC
from engine import Engine

class SternmanEngine(Engine, ABC):
    def __init__(self, warning_light_on):
        self.__warning_light_on = warning_light_on

    @property
    def warning_light_on(self):
        return self.__warning_light_on
    
    @warning_light_on.setter
    def warning_light_on(self, warning_light_condition):
        self.__warning_light_on = warning_light_condition

    def needs_service(self):
        if self.__warning_light_on:
            return True
        else:
            return False
