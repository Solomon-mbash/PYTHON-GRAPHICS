# Import the random module for generating random numbers
import random
# Import the Turtle class from the turtle module
from turtle import Turtle

# Define a class Food that inherits from Turtle
class Food(Turtle):
    # Constructor method to initialize the Food object
    def __init__(self):
        # Call the constructor of the parent class (Turtle)
        super().__init__()
        # Set the shape of the Food object to a circle
        self.shape("circle")
        # Set the color of the Food object to blue
        self.color("blue")
        # Set the size of the Food object
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        # Lift the pen to prevent drawing
        self.penup()

    # Method to refresh the position of the Food object
    def refresh(self):
        # Generate a random x-coordinate within the range -280 to 280
        random_x = random.randint(-280,280)
        # Generate a random y-coordinate within the range -280 to 280
        random_y = random.randint(-280,280)
        # Move the Food object to the new random position
        self.goto(random_x,random_y)