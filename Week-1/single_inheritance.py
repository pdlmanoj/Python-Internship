class Vehicle:
    def start(self):
        print("Starting vehicle engine....")
        
        
class Car(Vehicle):
    def drive(self):
        print("Car driving...")
        
        

c1 = Car()
c1.drive()
c1.start()