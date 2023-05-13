import unittest
from carfactory import CarFactory
from datetime import datetime

class TestCalliope(unittest.TestCase):
    def __int__(self, last_service_date, current_mileage, last_service_mileage):
        self.today = datetime.today().date()
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def test_battery_should_be_serviced(self):
        self.last_service_date = self.today.replace(year=self.today.year - 3)
        self.current_mileage = 30001
        self.last_service_mileage = 0

        car = CarFactory.create_calliope(self.last_service_date, self.current_mileage, self.last_service_mileage)
        self.assertTrue(car.battery.needs_service())

    def test_engine_should_be_serviced(self):
        self.last_service_date = self.today.replace(year=self.today.year - 3)
        self.current_mileage = 30001
        self.last_service_mileage = 0

        car = CarFactory.create_calliope(self.last_service_date, self.current_mileage, self.last_service_mileage)
        self.assertTrue(car.engine.needs_service())

class TestGlissade(unittest.TestCase):
    def __int__(self, last_service_date, current_mileage, last_service_mileage):
        self.today = datetime.today().date()
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage
        
    def test_battery_should_be_serviced(self):
        self.last_service_date = self.today.replace(year=self.today.year - 3)
        self.current_mileage = 60001
        self.last_service_mileage = 0

        car = CarFactory.create_glissade(self.last_service_date, self.current_mileage, self.last_service_mileage)
        self.assertTrue(car.battery.needs_service())

    def test_engine_should_be_serviced(self):
        self.last_service_date = self.today.replace(year=self.today.year - 3)
        self.current_mileage = 60001
        self.last_service_mileage = 0

        car = CarFactory.create_glissade(self.last_service_date, self.current_mileage, self.last_service_mileage)
        self.assertTrue(car.engine.needs_service())

class TestPalindrome(unittest.TestCase):
    def __int__(self, last_service_date, warning_light_on):
        self.today = datetime.today().date()
        self.last_service_date = last_service_date
        self.warning_light_on = warning_light_on
        
    def test_battery_should_be_serviced(self):
        self.last_service_date = self.today.replace(year=self.today.year - 3)
        self.warning_light_on = True

        car = CarFactory.create_palindrome(self.last_service_date, self.warning_light_one)
        self.assertTrue(car.battery.needs_service())

    def test_engine_should_be_serviced(self):
        self.last_service_date = self.today.replace(year=self.today.year - 3)
        self.current_mileage = 60001
        self.last_service_mileage = 0

        car = CarFactory.create_palindrome(self.last_service_date, self.current_mileage, self.last_service_mileage)
        self.assertTrue(car.engine.needs_service())

class TestRorschach(unittest.TestCase):
    def __int__(self, last_service_date, current_mileage, last_service_mileage):
        self.today = datetime.today().date()
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage
        
    def test_battery_should_be_serviced(self):
        self.last_service_date = self.today.replace(year=self.today.year - 3)
        self.current_mileage = 60001
        self.last_service_mileage = 0

        car = CarFactory.create_rorschach(self.last_service_date, self.current_mileage, self.last_service_mileage)
        self.assertTrue(car.battery.needs_service())

    def test_engine_should_be_serviced(self):
        self.last_service_date = self.today.replace(year=self.today.year - 3)
        self.current_mileage = 60001
        self.last_service_mileage = 0

        car = CarFactory.create_rorschach(self.last_service_date, self.current_mileage, self.last_service_mileage)
        self.assertTrue(car.engine.needs_service())

class TestThovex(unittest.TestCase):
    def __int__(self, last_service_date, current_mileage, last_service_mileage):
        self.today = datetime.today().date()
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage
        
    def test_battery_should_be_serviced(self):
        self.last_service_date = self.today.replace(year=self.today.year - 3)
        self.current_mileage = 30001
        self.last_service_mileage = 0

        car = CarFactory.create_thovex(self.last_service_date, self.current_mileage, self.last_service_mileage)
        self.assertTrue(car.battery.needs_service())

    def test_engine_should_be_serviced(self):
        self.last_service_date = self.today.replace(year=self.today.year - 3)
        self.current_mileage = 30001
        self.last_service_mileage = 0

        car = CarFactory.create_thovex(self.last_service_date, self.current_mileage, self.last_service_mileage)
        self.assertTrue(car.engine.needs_service())

if __name__ == '__main__':
    unittest.main()