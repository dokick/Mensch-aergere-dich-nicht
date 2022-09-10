from random import randint
from turtle import Vec2D


def dice() -> int:
    """Simulates rolling a dice

    Returns:
        int: Random integer betweeen 1 and 6
    """
    return randint(1, 6)


def convert_Vec2D_to_tuple(pos: Vec2D) -> tuple[int | float]:
    """Converting a Vec2D Vector from turtle

    Used for getting the position of a turtle and not worry about compatibility issues
    It is maybe theoretically possible to get a not intended output, because we are dealing with a 2D plane and just interested in the two first elements

    Args:
        pos (Vec2D): turtle's position

    Returns:
        tuple: turtle's position (x, y)
    """
    return (pos[0], pos[1])


if __name__ == "__main__":
    print("Test passed") if dice() in [
        1, 2, 3, 4, 5, 6] else print("Test failed")
