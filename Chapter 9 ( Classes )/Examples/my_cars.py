# You can also do import car to import the whole module here. You have to use dot notation if you do.
# You can import all the classes from a module by doing "from moduleName, import *"

from car import Car
from electric_car2 import ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())

