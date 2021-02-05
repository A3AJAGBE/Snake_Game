import turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.initial_length = []
        self.posX = 0
        self.posY = 0
        self.make_snake()
        self.head = self.initial_length[0]

    def make_snake(self):
        """This functions makes 3 squares as the initial length of the snake"""
        for _ in range(3):
            sample = turtle.Turtle("square")
            sample.penup()
            sample.goto(x=self.posX, y=self.posY)
            self.posX += -20
            self.initial_length.append(sample)

    def move_snake(self):
        """This function moves the snake"""
        for square in range(len(self.initial_length) - 1, 0, -1):
            new_posX = self.initial_length[square - 1].xcor()
            new_posY = self.initial_length[square - 1].ycor()
            self.initial_length[square].goto(new_posX, new_posY)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        self.head.setheading(UP)

    def down(self):
        self.head.setheading(DOWN)

    def left(self):
        self.head.setheading(LEFT)

    def right(self):
        self.head.setheading(RIGHT)
