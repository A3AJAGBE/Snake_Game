# Import
import turtle
from snake import Snake
import time

# Instantiate Screen
screen = turtle.Screen()

# Set up the screen
screen.setup(width=600, height=600)
screen.title("A3AJAGBE SNAKE GAME")
screen.tracer(0)

# Instantiate Snake
snake = Snake()

# Snake Direction
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


start_game = True
while start_game:
    screen.update()
    # per second
    time.sleep(0.1)
    snake.move_snake()


# Keep the screen open until closed
screen.exitonclick()
