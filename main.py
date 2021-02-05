# Import
import turtle

# Instantiate Screen
screen = turtle.Screen()

# Set up the screen
screen.setup(width=600, height=600)
screen.title("A3AJAGBE SNAKE GAME")

# Create the snake
posX = 0
posY = 0
initial_length = []
for _ in range(3):
    sample = turtle.Turtle("square")
    sample.goto(x=posX, y=posY)
    posX += -20
    initial_length.append(sample)

# Keep the screen open until closed
screen.exitonclick()
