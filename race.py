from turtle import Turtle, Screen
import random

# Set up the screen for the turtle race
screen = Screen()
screen.setup(width=500, height=400)

# Define the colors for the turtles
colors = ["red","orange", "blue","purple","cyan","green"]

# Prompt the user to guess the winning turtle's color
guess = screen.textinput(title="turtle betting!", prompt="guess the color of turtle which is going to win? ")
print(guess)

# Define the y-coordinates for each turtle's starting position
y_coordinate = [-70,-40,-10,20,50,80,110]
all_turtle = []

# Create turtles and set their initial positions and colors
for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(-230, y_coordinate[turtle_index])
    all_turtle.append(new_turtle)

# Initialize the race status
is_run = False

# Check if the user made a guess
if guess:
    is_run = True

# Start the race
while is_run:
    for turtle in all_turtle:
        # Check if a turtle has crossed the finish line
        if turtle.xcor() > 230:
            is_run = False  # Stop the race
            winn_turtle = turtle.pencolor()  # Get the winning turtle's color

            # Check if the user's guess was correct
            if winn_turtle == guess:
                print(f"you win, you choose {winn_turtle}")
            else:
                print(f"you lose!, you choose {guess}, and winner is {winn_turtle}")

        # Move the turtle forward by a random speed
        random_speed = random.randint(0,10)
        turtle.forward(random_speed)

# Wait for the user to click before closing the window
screen.exitonclick()