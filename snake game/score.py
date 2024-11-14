# Import the Turtle class from the turtle module
from turtle import Turtle

# Define constants for alignment and font
ALIGHNMENT = "center"  # Alignment for the scoreboard text
FONT = ("Aerial", 24, "normal")  # Font for the scoreboard text

# Define a class ScoreBoard that inherits from Turtle
class ScoreBoard(Turtle):
    # Initialize the scoreboard
    def __init__(self):
        # Call the constructor of the parent class
        super().__init__()
        # Initialize the score to 0
        self.score = 0
        # Set the color of the scoreboard to white
        self.color("white")
        # Lift the pen to avoid drawing
        self.penup()
        # Hide the turtle
        self.hideturtle()
        # Move the turtle to the position (0, 230)
        self.goto(0, 230)
        # Write the initial score
        self.write(f"Score: {self.score}", move=False, align=ALIGHNMENT, font=FONT)
        # Update the scoreboard
        self.update_score()

    # Update the scoreboard with the current score
    def update_score(self):
        # Write the current score
        self.write(f"Score: {self.score}", False, align=ALIGHNMENT, font=FONT)

    # Increase the score by 1
    def increase_score(self):
        # Increment the score
        self.score += 1
        # Write the updated score
        self.write(f"Score: {self.score}", False, align=ALIGHNMENT, font=FONT)
        # Clear the previous score
        self.clear()
        # Update the scoreboard
        self.update_score()

    # Display the game over message
    def game_over(self):
        # Move the turtle to the position (0, 0)
        self.goto(0, 0)
        # Write the game over message
        self.write("GAME OVER", False, align=ALIGHNMENT, font=FONT)