from turtle import Screen, Turtle, forward, pos, left, right
from gameBoard import vertices_for_left_turn, vertices_for_right_turn, game_piece_colors, home_positions
from typing import Literal
from tools import dice, convert_Vec2D_to_tuple

speeds: list[str] = ["fastest", "fast", "normal", "slow", "slowest"]


class GamePiece:

    def __init__(self, *, color: str, id: Literal[1, 2, 3, 4], speed: Literal["fastest", "fast", "normal", "slow", "slowest"]) -> None:
        self.turtle = Turtle()
        self.color: str = color
        self.id: int = id
        screen = Screen()
        screen.colormode(255)
        self.turtle.fillcolor(game_piece_colors[self.color])
        self.turtle.speed(speed=speed)
        self.turtle.shape("turtle")

    def __repr__(self) -> str:
        return f"color: {self.color}\nid: {self.id}\nspeed: {self.turtle.speed()}"

    def move(self) -> None:
        for i in range(dice()):
            if self.getPos() in vertices_for_left_turn:
                self.turtle.left(90)
            if self.getPos() in vertices_for_right_turn:
                self.turtle.right(90)
            self.turtle.forward(80)
    
    def is_on_field(self) -> bool:
        return self.getPos() not in home_positions

    def get_pos(self) -> tuple:
        return convert_Vec2D_to_tuple(self.turtle.pos())
    
    def get_ID(self) -> int:
        return self.id


def main():
    """For testing and debugging purposes"""
    gamePiece = GamePiece(color="green", id=1, speed="fastest")
    print(gamePiece)


if __name__ == "__main__":
    main()
