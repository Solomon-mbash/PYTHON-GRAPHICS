from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500, height=400)
colors = ["red","orange", "blue","purple","yellow","green"]
guess = screen.textinput(title="turtle betting!", prompt="guess the color of tutrle which is going to win? ")
print(guess)
y_coordinate = [-70,-40,-10,20,50,80,110]
all_turtle = []

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(-230, y_coordinate[turtle_index])
    all_turtle.append(new_turtle)

is_run = False

if guess:
    is_run = True



while is_run:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_run = False
            winn_turtle = turtle.pencolor()

            if winn_turtle == guess:
                print(f"you win, you choose {winn_turtle}")
            else:
                print(f"you lose!, you choose {guess}, and winner is {winn_turtle}")

        random_speed = random.randint(0,10)
        turtle.forward(random_speed)


screen.exitonclick()




# tim = Turtle(shape="turtle")
# tim.penup()
# tim.color(colors[0])
# tim.goto(-230,100)

# tom = Turtle(shape="turtle")
# tom.penup()
# tom.color(colors[1])
# tom.goto(-230,-50)

# Bon = Turtle(shape="turtle")
# Bon.penup()
# Bon.color(colors[2])
# Bon.goto(-230,50)

# nao = Turtle(shape="turtle")
# nao.penup()
# nao.color(colors[3])
# nao.goto(-230,20)

# sara = Turtle(shape="turtle")
# sara.penup()
# sara.color(colors[5])
# sara.goto(-230,-20)