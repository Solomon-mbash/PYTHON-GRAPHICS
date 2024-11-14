# Import the necessary modules
import turtle as t
from random import choice, randint

# Create a new turtle object and a screen object
tim = t.Turtle()
my_screen = t.Screen()

# Set the turtle's shape and the color mode
tim.shape("turtle")
t.colormode(255)

# Define a function to generate a random color
def color_mode():
    # Generate random values for red, green, and blue
    r = randint(1, 255)
    g = randint(1, 255)
    b = randint(1, 255)

    # Return the color as a tuple
    color = (r, g, b)
    return color

# Set the turtle's pen size and speed
tim.pensize(1)
tim.speed("fastest")

# Set the turtle's pen size again (this may be unnecessary)
tim.pensize(2)

# Define a function to draw a shape with a specified number of turns
def drawer(number_of_turns):
    # Calculate the number of iterations needed to complete a full circle
    for _ in range(int(360 / number_of_turns)):
        # Draw a circle with a radius of 100
        tim.circle(100)
        # Set the pen color to a random color
        tim.pencolor(color_mode())
        # Get the current heading of the turtle
        current_head = tim.heading()
        # Set the turtle's heading to the current heading plus the number of turns
        tim.setheading(number_of_turns + current_head)

# Call the drawer function with 5 turns
drawer(5)

# Exit the program when the user clicks on the screen
my_screen.exitonclick()