class Vehicle:
    def move(self):
        print("All vehicles are moving")

class Car(Vehicle):
    def move(self):
        print("Driving on the road")

class Bicycle(Vehicle):
    def move(self):
        print("Paddling on the road")

#Demonstarting Polymorphism 

vehicles = [Car(), Bicycle()]

for vehicle in vehicles:
    vehicle.move()
