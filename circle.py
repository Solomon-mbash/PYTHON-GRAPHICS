import turtle as t
from random import choice, randint

tim = t.Turtle()
my_screen = t.Screen()



tim.shape("turtle")
t.colormode(255)


def color_mode():
    r =randint(1,255)
    g = randint(1,255)
    b = randint(1,255)

    color = (r,g,b)

    return color
tim.pensize(1)
tim.speed("fastest")



# for drawing random walk
# for _ in range(500):
#     tim.forward(30)
#     tim.setheading(choice(direction))
#     tim.pencolor(color_mode())


# # for drawing circle
# for _ in range(4):
#     tim.setheading(tim.cu)
#     tim.circle(110)
tim.pensize(2)
def drawer(number_of_turns):
    for _ in range(int(360 / number_of_turns)):
        tim.circle(100)
        tim.pencolor(color_mode())
        current_head = tim.heading()
        tim.setheading(number_of_turns + current_head)


drawer(5)

my_screen.exitonclick()
