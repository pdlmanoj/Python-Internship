from abc import ABC, abstractmethod

# interface
class Vehicle(ABC):
    
    @abstractmethod
    def move(self):
        pass
    
class Car(Vehicle):
    def model(self,model_name):
        print(f"Model{model_name}")
        
    def move(self):
        print("Car is moving.....")
        
    
class Plane(Vehicle):
    def move(self):
        print("Plane is moving....")
    

vehicle = [Car(), Plane()]

print(vehicle[0].model("Toyota"))

for v in vehicle:
    v.move()


    
    