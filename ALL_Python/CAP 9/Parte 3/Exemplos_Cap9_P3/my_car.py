from car import Car

my_new_car = Car('toyota','sw4',2011)
print(my_new_car.get_decriptive_name())

my_new_car.odometer_reading= 20
my_new_car.read_odometer()