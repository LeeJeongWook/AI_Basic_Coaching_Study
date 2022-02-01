class Car():
    def __init__(self, fuel, wheels):
        self.fuel = fuel
        self.wheels = wheels
    
class Bike(Car):
    # TODO

bike = Bike("gas", 2, "small")
print(bike.fuel, bike.wheels, bike.size)