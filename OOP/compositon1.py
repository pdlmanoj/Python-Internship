class PetrolEngine:
    def start(self):
        print("Petrol engine starting.....")

class DesielEngine:
    def start(self):
        print("Desiel engine starting .......")


class Car:
    def __init__(self, engine):
        self.engine_type = engine

    def start_car(self):
        self.engine_type.start()


c1 = Car(PetrolEngine())
c1.start_car()

