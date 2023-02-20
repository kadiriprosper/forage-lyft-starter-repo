from my_code.car_factory import CarFactory

newCar1 = CarFactory()
newCar2 = newCar1.create_calliope(10, 200, 300)
print(newCar2.engine.needs_service())
