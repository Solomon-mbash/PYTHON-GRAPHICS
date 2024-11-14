import turtle as t
from random import *




def color_mode():
    r =randint(1,255)
    g = randint(1,255)
    b = randint(1,255)

    color = (r,g,b)

    return color

turtle = t.Turtle()
my_screen = t.Screen()
t.colormode(255)
turtle.penup()
turtle.hideturtle()
turtle.speed("fastest")
turtle.setheading(225)
turtle.forward(300)
turtle.setheading(0)   
number_of_dots = 100

for dots_counts in range(1, number_of_dots + 1):
    turtle.dot(20,color_mode())
    turtle.forward(50)

    if dots_counts % 10 == 0:
        turtle.setheading(90)
        turtle.forward(50)
        turtle.setheading(180)
        turtle.forward(500)
        turtle.setheading(0)




my_screen.exitonclick()