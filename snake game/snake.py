# Import necessary modules
from time import sleep
from tkinter.constants import RIGHT
from turtle import Turtle

# Define constants
STARTING_POSITION = [(0,0),(-20,0),(-40,0)]  # Initial positions of the snake segments
MOVE_FORWARD = 20  # Distance to move the snake forward
UP = 90  # Angle for moving up
DOWN = 270  # Angle for moving down
LEFT = 180  # Angle for moving left
RIGHTS = 0  # Angle for moving right

# Define the Snake class
class Snake:
    # Initialize the snake
    def __init__(self):
        # Initialize an empty list to store the snake segments
        self.segment = []
        # Create the initial snake segments
        self.create_snake()
        # Initialize the head of the snake
        self.head = self.segment[0]  # Corrected the initialization of the head

    # Create the initial snake segments
    def create_snake(self):
        # Iterate over the starting positions and create a segment at each position
        for position in STARTING_POSITION:
            self.add_segment(position)

    # Add a new segment to the snake
    def add_segment(self, position):
        # Create a new turtle object for the segment
        new_segment = Turtle("square")
        # Set the color of the segment
        new_segment.color("green")
        # Lift the pen to move the segment without drawing
        new_segment.penup()
        # Move the segment to the specified position
        new_segment.goto(position)
        # Add the segment to the list of segments
        self.segment.append(new_segment)

    # Extend the snake by adding a new segment
    def extend(self):
        # Add a new segment at the position of the second segment
        self.add_segment(self.segment[-1].position())  # Corrected the position of the new segment

    # Move the snake
    def move(self):
        # Iterate over the segments in reverse order
        for segment_number in range(len(self.segment) - 1, 0, -1):
            # Get the position of the previous segment
            new_x = self.segment[segment_number - 1].xcor()
            new_y = self.segment[segment_number - 1].ycor()
            # Move the current segment to the position of the previous segment
            self.segment[segment_number].goto(new_x, new_y)
        # Move the head of the snake forward
        self.segment[0].forward(MOVE_FORWARD)

    # Move the snake up
    def up(self):
        # Check if the snake is not moving down
        if self.head.heading() != DOWN:
            # Set the heading of the snake to up
            self.head.setheading(UP)

    # Move the snake down
    def down(self):
        # Check if the snake is not moving up
        if self.head.heading() != UP:
            # Set the heading of the snake to down
            self.head.setheading(DOWN)

    # Move the snake left
    def left(self):
        # Check if the snake is not moving right
        if self.head.heading() != RIGHTS:
            # Set the heading of the snake to left
            self.head.setheading(LEFT)

    # Move the snake right
    def right(self):
        # Check if the snake is not moving left
        if self.head.heading() != LEFT:
            # Set the heading of the snake to right
            self.head.setheading(RIGHTS)