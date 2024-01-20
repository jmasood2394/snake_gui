from turtle import Turtle
from random import randint


class Food(Turtle):
    """ Class to create food on the screen """
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("yellow")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.goto(x=randint(-280, 280), y=randint(-280, 280))