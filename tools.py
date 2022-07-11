from random import randint
from turtle import Vec2D


def dice():
    # Simulates rolling a dice by returning a random integer between 1 and 6
    return randint(1, 6)


def convertVec2DToTuple(pos: Vec2D) -> tuple:
    # Converting Vec2D Vector from turtle into a tuple
    return (pos[0], pos[1])
