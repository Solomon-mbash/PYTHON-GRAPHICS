# Import the necessary modules
import turtle as t
from random import *

# Function to generate a random color
def color_mode():
    # Generate random RGB values
    r = randint(1,255)
    g = randint(1,255)
    b = randint(1,255)

    # Create a color tuple
    color = (r,g,b)

    # Return the color
    return color

# Create a turtle object
turtle = t.Turtle()

# Create a screen object
my_screen = t.Screen()

# Set the color mode to 255
t.colormode(255)

# Lift the pen up to move without drawing
turtle.penup()

# Hide the turtle
turtle.hideturtle()

# Set the speed to fastest
turtle.speed("fastest")

# Set the initial heading
turtle.setheading(225)

# Move forward by 300 units
turtle.forward(300)

# Set the heading to 0
turtle.setheading(0)

# Define the number of dots
number_of_dots = 100

# Loop through the range of dots
for dots_counts in range(1, number_of_dots + 1):
    # Create a dot with a random color
    turtle.dot(20,color_mode())

    # Move forward by 50 units
    turtle.forward(50)

    # Check if the current dot count is a multiple of 10
    if dots_counts % 10 == 0:
        # Set the heading to 90
        turtle.setheading(90)

        # Move forward by 50 units
        turtle.forward(50)

        # Set the heading to 180
        turtle.setheading(180)

        # Move forward by 500 units
        turtle.forward(500)

        # Set the heading to 0
        turtle.setheading(0)

# Exit the program on click
my_screen.exitonclick()