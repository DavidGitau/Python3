# Method chaining
# Methods have to return self

class Car:
    def turn_on(self):
        print('The car is turned on')
        return self
        
    def drive(self):
        print('The car is driving')
        return self
    
    def brake(self):
        print('The car is braked and stopped')
        return self
    
    def turn_off(self):
        print('The car is turned off')
        return self
        
car = Car()
car.turn_on()\
    .drive()\
    .brake()\
    .turn_off()