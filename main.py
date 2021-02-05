# Import
import turtle
import time

# Instantiate Screen
screen = turtle.Screen()

# Set up the screen
screen.setup(width=600, height=600)
screen.title("A3AJAGBE SNAKE GAME")
screen.tracer(0)

# Create the snake
posX = 0
posY = 0
initial_length = []
for _ in range(3):
    sample = turtle.Turtle("square")
    sample.penup()
    sample.goto(x=posX, y=posY)
    posX += -20
    initial_length.append(sample)

# Move the snake
start_game = True
while start_game:
    screen.update()
    # per second
    time.sleep(0.1)

    # This for loop will improve snake movement
    for square in range(len(initial_length) - 1, 0, -1):
        new_posX = initial_length[square - 1].xcor()
        new_posY = initial_length[square - 1].ycor()
        initial_length[square].goto(new_posX, new_posY)
    initial_length[0].forward(20)


# Keep the screen open until closed
screen.exitonclick()
