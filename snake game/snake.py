from time import sleep
from tkinter.constants import RIGHT
from turtle import Turtle
STARTING_POSITION = [(0,0),(-20,0),(-40,0)]
MOVE_FORWARD = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHTS = 0

class Snake:
    def __init__(self):

        self.segment = []
        self.create_snake()
        self.head = 20
        self.move()
        self.head = self.segment[0]


    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("green")
        new_segment.penup()
        new_segment.goto(position)
        self.segment.append(new_segment)
    def extend(self):
        self.add_segment(self.segment[1].position())

    def move(self):
        for segment_number in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[segment_number - 1].xcor()
            new_y = self.segment[segment_number - 1].ycor()
            self.segment[segment_number].goto(new_x, new_y)
        self.segment[0].forward(MOVE_FORWARD)
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHTS:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHTS)