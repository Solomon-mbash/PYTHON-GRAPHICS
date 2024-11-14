# Import necessary modules
# Import time module for time-related functions
import time
# Import ScoreBoard class from score module
from score import ScoreBoard
# Import Food class from FOOD module
from FOOD import Food
# Import Snake class from snake module
from snake import Snake
# Import Screen class from turtle module
from turtle import Screen

# Initialize game objects
# Initialize food object
food = Food()
# Initialize snake object
snake = Snake()
# Initialize screen object
screen = Screen()
# Set up screen dimensions
screen.setup(600,600)

# Set up screen background color
screen.bgcolor("orange")
# Initialize score board object
score_board = ScoreBoard()
# Turn off screen animation
screen.tracer(0)
# Start listening for keyboard events
screen.listen()

# Set up keyboard bindings for snake movement
# Bind up arrow key to snake's up movement
screen.onkey(snake.up, "Up")
# Bind down arrow key to snake's down movement
screen.onkey(snake.down, "Down")
# Bind left arrow key to snake's left movement
screen.onkey(snake.left, "Left")
# Bind right arrow key to snake's right movement
screen.onkey(snake.right, "Right")

# Initialize game loop flag
game_on = True
# Start game loop
while game_on:
    # Update screen
    screen.update()
    # Pause game loop for 0.1 seconds
    time.sleep(0.1)
    # Move snake
    snake.move()

    # Check if snake has eaten food
    if snake.head.distance(food) < 15:
        # Refresh food position
        food.refresh()
        # Increase score
        score_board.increase_score()
        # Extend snake length
        snake.extend()
    # Check if snake has hit boundary
    if snake.head.xcor() > 280 or snake.head.xcor() <-280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        # Display game over message
        score_board.game_over()
        # Set game loop flag to False
        game_on = False
    # Check if snake has hit itself
    for segment in snake.segment:
        # Skip head segment
        if segment == snake.head:
            pass
        # Check if head has hit any other segment
        elif snake.head.distance(segment) < 10:
            # Display game over message
            score_board.game_over()
            # Set game loop flag to False
            game_on = False

# Exit game on click
screen.exitonclick()