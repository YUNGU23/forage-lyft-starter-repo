from battery import Battery

class SpindleBattery(Battery):
    def __init__(self, last_service_date, current_date):
        self.__last_service_date = last_service_date
        self.__current_date = current_date

    @property
    def last_service_date(self):
        return self.__last_service_date
    
    @last_service_date.setter
    def last_service_date(self, date):
        self.__last_service_date = date
    
    @property
    def current_date(self):
        return self.__current_date
    
    @current_date.setter
    def current_date(self, date):
        self.__current_date = date
    
    def needs_service(self) -> bool:
        self.__current_date - self.__last_service_date > 2