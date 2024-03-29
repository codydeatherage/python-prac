class Car:
	"""its a car"""
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		long_name = f"{self.year} {self.make} {self.model}"
		return long_name.title()

	def read_odometer(self):
		print(f"This car has {self.odometer_reading} miles on it.")

	def update_odometer(self, mileage):
		self.odometer_reading = mileage


class Battery:
	def __init__(self, battery_size=75):
		self.battery_size = battery_size
	
	def describe_battery(self):
		print(f"This car has a {self.battery_size}-kW battery.")


class ElectricCar(Car):
	def __init__(self, make, model, year):
		super().__init__(make, model, year)
		self.battery = Battery()

	

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_car = Car('toyota', 'car', '2021')
print(my_car.get_descriptive_name())
my_car.read_odometer()
my_car.update_odometer(73)
my_car.read_odometer()