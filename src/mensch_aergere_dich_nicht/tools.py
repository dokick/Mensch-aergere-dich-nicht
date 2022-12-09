"""
This module is just a collection of useful functions.

Functions:
    convert_Vec2D_to_tuple(pos: Vec2D) -> tuple[float, float]
    dice() -> int
"""

from random import randint
from turtle import Vec2D


# pylint: disable-next=invalid-name
def convert_Vec2D_to_tuple(pos: Vec2D) -> tuple[float, float]:
    """Converting a Vec2D Vector from turtle

    Used for getting the position of a turtle
    and not worry about compatibility issues
    We are rounding to the last 2 digits,
    because the turtle GUI can scramble up numbers

    Args:
        pos (Vec2D): turtle's position (x, y)

    Returns:
        tuple[float, float]: turtle's position (x, y)
    """
    return tuple((round(i, 2) for i in pos))


def dice() -> int:
    """Simulates rolling a dice

    Returns:
        int: Random integer betweeen 1 and 6
    """
    return randint(1, 6)


if __name__ == "__main__":
    # pylint: disable-next=expression-not-assigned
    print("Test passed") if dice() in [
        1, 2, 3, 4, 5, 6] else print("Test failed")
