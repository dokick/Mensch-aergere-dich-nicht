from random import randint
from turtle import Vec2D


def dice() -> int:
    # Simulates rolling a dice by returning a random integer between 1 and 6
    return randint(1, 6)


def convert_Vec2D_to_tuple(pos: Vec2D) -> tuple:
    # Converting Vec2D Vector from turtle into a tuple
    return (pos[0], pos[1])


if __name__ == "__main__":
    print("Test passed") if dice() in [
        1, 2, 3, 4, 5, 6] else print("Test failed")
