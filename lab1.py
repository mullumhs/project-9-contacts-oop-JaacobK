"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                    LAB 1
---------------------------------------------------------------------------------
- File Name: lab1.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Create and manipulate Car objects in Python to understand 
  basic concepts of Object-Oriented Programming.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

class Car:
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand
        self.is_engine_on = False
        self.odometer = 0

    def start_engine(self):
        self.is_engine_on = True
        print(f"The engine of the {self.color} {self.brand} is now on.")

    def stop_engine(self):
        self.is_engine_on = False
        print(f"The engine of the {self.color} {self.brand} is now off.")

    def Drive(self, distance):
        self.odometer += self.distance


# Add another property to the Car class called "odometer".
# This property should be initialised to 0.



# Create two Car objects. One should be a red Toyota and the other a blue Ford.

Car1 = Car("red", "Toyota")
Car2 = Car("blue", "Ford")

# Start the engine of the red Toyota.

Car1.start_engine()

# Create a method called "drive" that takes a distance as a parameter.
# The car can only be driven if the engine is on.

def Drive():



# Attempt to drive both cars 100Km.



# Print the brand, odometer and colour of both cars.


