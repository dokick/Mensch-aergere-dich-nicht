from turtle import Screen, Turtle, forward, pos, left, right
from gameBoard import verticesForLeftTurn, verticesForRightTurn, gamePieceColors, homePositions
from typing import Literal
from tools import dice, convertVec2DToTuple

speeds: list[str] = ["fastest", "fast", "normal", "slow", "slowest"]


class GamePiece:

    def __init__(self, *, color: str, id: Literal[1, 2, 3, 4], speed: Literal["fastest", "fast", "normal", "slow", "slowest"]) -> None:
        self.turtle = Turtle()
        self.color: str = color
        self.id: int = id
        screen = Screen()
        screen.colormode(255)
        self.turtle.fillcolor(gamePieceColors[self.color])
        self.turtle.speed(speed=speed)
        self.turtle.shape("turtle")

    def __repr__(self) -> str:
        return f"color: {self.color}\nid: {self.id}\nspeed: {self.turtle.speed()}"

    def move(self):
        for i in range(dice()):
            if self.getPos() in verticesForLeftTurn:
                self.turtle.left(90)
            if self.getPos() in verticesForRightTurn:
                self.turtle.right(90)
            self.turtle.forward(80)
    
    def isOnField(self) -> bool:
        return self.getPos() not in homePositions

    def getPos(self):
        return convertVec2DToTuple(self.turtle.pos())


def main():
    """For testing and debugging purposes"""
    gamePiece = GamePiece(color="green", id=1, speed="fastest")
    print(gamePiece)


if __name__ == "__main__":
    main()
