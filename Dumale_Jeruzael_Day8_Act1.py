from car import *
from carPrinter import *

car1 = Car()
car2 = Car()
car3 = Car()

car1._color = "Green"
car1.model = "Toyota360"
car1.manufacturer = "Toyota"

car2._color = "Pink"
car2.model = "Honda brazer"
car2.manufacturer = "Honda"

car3._color = "Red"
car3.model = "Tesla X01"
car3.manufacturer = "Tesla"

showCarInfo(car1._color, car1.model, car1.manufacturer)
showCarInfo(car2.color, car2.model, car2.manufacturer)
showCarInfo(car3.color, car3.model, car3.manufacturer)