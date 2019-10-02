from car import Car
from my_electric_car import ElectricCar

new_car = Car('ford', 'f150', 2018)

description1 = new_car.get_descriptive_name()

new_tesla = ElectricCar('tesla', 'model s', 2019)

description2 = new_tesla.get_descriptive_name()

print(description1)
print(description2)

