import time
from score import ScoreBoard
from FOOD import Food
from snake import Snake
from turtle import Screen


food = Food()
snake = Snake()
screen = Screen()
screen.setup(600,600)

screen.bgcolor("orange")
score_board = ScoreBoard()
screen.tracer(0)
screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# starting_position = [(0,0),(-20,0),(-40,0)]
# segment = []
#

# for position in starting_position:
#     new_segment = Turtle("square")
#     new_segment.color("white")
#     new_segment.penup()
#     new_segment.goto(position)
#     segment.append(new_segment)
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        score_board.increase_score()
        snake.extend()
    if snake.head.xcor() > 280 or snake.head.xcor() <-280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score_board.game_over()
        game_on =False
    for segment in snake.segment:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
                game_on = False
                score_board.game_over()

            # for segment_number in range(len(segment)-1,0,-1):
    #     new_x = segment[segment_number -1].xcor()
    #     new_y = segment[segment_number -1].ycor()
    #     segment[segment_number].goto(new_x,new_y)
    # segment[0].forward(20)




screen.exitonclick()