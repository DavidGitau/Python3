"""
Abstract class - a class that contains one or more abstract methods
abstract method - a method that has a declaration but does not have an implementation

prevents a user from creating an object of that class
compels a user to override abstrac methods in a child class
"""

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def go(self):
        print('You drive the car')

    def stop(self):
        print('This car is stopped')

class MotorCycle(Vehicle):
    def go(self):
        print('You drive the motorcycle')

    def stop(self):
        print('This motorcycle is stopped')

car = Car()
motorcycle = MotorCycle()
car.go()