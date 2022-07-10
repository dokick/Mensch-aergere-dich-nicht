from turtle import Turtle, forward, pos, left, right
from gameBoard import verticesForLeftTurn, verticesForRightTurn
from typing import Literal
from tools import dice, convertVec2DToTuple

speeds: str = ["fastest", "fast", "normal", "slow", "slowest"]


class GamePiece:
    turtle = Turtle()

    def __init__(self, *, color: str, speed: Literal["fastest", "fast", "normal", "slow", "slowest"]) -> None:
        self.color = color
        self.speed = speed
        self.turtle.speed(speed=speed)

    def __repr__(self) -> str:
        return f"{self.color} colored game piece with {self.speed} speed"

    def move(self):
        for i in range(dice()):
            if self.getPos() in verticesForLeftTurn:
                self.turtle.left(90)
            if self.getPos() in verticesForRightTurn:
                self.turtle.right(90)
            self.turtle.forward(80)

    def getPos(self):
        return convertVec2DToTuple(self.turtle.pos())


def main():
    """For testing and debugging purposes"""
    gamePiece = GamePiece("green", "fastest")
    print(gamePiece)


if __name__ == "__main__":
    main()
