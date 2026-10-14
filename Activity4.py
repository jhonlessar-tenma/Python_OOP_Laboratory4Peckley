class Vehicle:
	def __init__(self, brand, speed):
		self.__brand = brand
		self.__speed = speed

	@property
	def brand(self):
		return self.__brand

	@property
	def speed(self):
		return self.__speed

	@speed.setter
	def speed(self, value):
		self.__speed = value

	def start(self):
		print("Vehicle is starting.")


class Car(Vehicle):
	def start(self):
		print("Car engine is starting.")


vehicle = Vehicle("Generic", 0)
car = Car("Toyota", 0)

vehicle.start()
car.start()
