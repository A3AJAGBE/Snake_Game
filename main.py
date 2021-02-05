# Import
import turtle
from snake import Snake
from snake_food import Food
from scoreboard import Scoreboard
import time

# Instantiate Screen
screen = turtle.Screen()

# Set up the screen
screen.setup(width=600, height=600)
screen.title("A3AJAGBE SNAKE GAME")
screen.tracer(0)

# Instantiate Snake
snake = Snake()
HEAD = snake.head

# Instantiate Food
food = Food()

# Instantiate Scoreboard
scoreboard = Scoreboard()

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

    # Detect snake collision with food
    if HEAD.distance(food) < 15:
        snake.grow()
        food.generate_location()
        scoreboard.increase_score()

    # Detect collision with wall
    if HEAD.xcor() > 280 or HEAD.xcor() < -280 or HEAD.ycor() > 280 or HEAD.ycor() < -280:
        start_game = False
        scoreboard.game_over()

    # Detect collision with tail
    for square in snake.initial_length[1:-1]:
        if HEAD.distance(square) < 10:
            start_game = False
            scoreboard.game_over()

# Keep the screen open until closed
screen.exitonclick()
