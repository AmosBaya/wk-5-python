class Vehicles:

    def move(self):
        pass

    def stop(self):
        pass

class Car(Vehicles):

    def move(self):
        print("The car is moving")
    
    def stop(self):
        print("The car has stopped")

class Plane(Vehicles):

    def move(self):
        print("The Plane is flying")
    
    def stop(self):
        print("The Plane has landed")

jet = Plane()
jet.move()
jet.stop()

corola = Car()
corola.move()
corola.stop()