from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.shapesize(0.5)
        self.color("red")
        self.speed("fastest")
        self.generate_location()

    def generate_location(self):
        """This function generate a random location for the food."""
        posX = random.randint(-280, 280)
        posY = random.randint(-280, 280)
        self.goto(x=posX, y=posY)