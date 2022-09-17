from turtle import Screen, Turtle, forward, pos, left, right
from typing import Literal
from gameBoard import vertices_for_left_turn, vertices_for_right_turn, GAME_PIECE_COLORS, home_positions, target_positions, turning_vertices_per_color
from tools import convert_Vec2D_to_tuple

SPEEDS: list[str] = ["fastest", "fast", "normal", "slow", "slowest"]


class GamePiece:
    # TODO: Docs
    """This class represents one game piece in the game

    Attributes:
        turtle (Turtle): the turtle of a game piece
        color (str): the color of the game piece
        id (int): id of the game piece so they can be distinguished

    Methods:
        __init__(self, *, color: str, id: Literal[1, 2, 3, 4], speed: Literal["fastest", "fast", "normal", "slow", "slowest"]) -> None
        __repr__(self) -> str
        move(self, steps: int) -> None
        is_on_field(self) -> bool
        is_playable(self) -> bool
        get_pos(self) -> tuple
        get_ID(self) -> int
    """

    def __init__(self, *, color: str, id: Literal[1, 2, 3, 4], speed: Literal["fastest", "fast", "normal", "slow", "slowest"]) -> None:
        self.turtle = Turtle()
        self.color: str = color
        self.id: int = id
        self.steps: int = 0

        screen = Screen()
        screen.colormode(255)
        self.turtle.fillcolor(GAME_PIECE_COLORS[self.color])
        self.turtle.speed(speed=speed)
        self.turtle.shape("turtle")
        self.turtle.penup()

    def __repr__(self) -> str:
        return f"color: {self.color}\nid: {self.id}\nspeed: {self.turtle.speed()}"

    def move(self, steps: int):
        # TODO: Docs
        """

        Args:
            steps (int): amount of steps the game piece goes
        """
        for i in range(steps):
            if self.get_pos() in vertices_for_left_turn:
                self.turtle.left(90)
            if self.get_pos() in vertices_for_right_turn or self.get_pos() == turning_vertices_per_color[self.color]:
                self.turtle.right(90)
            self.turtle.forward(80)
            self.steps += 1
        return self

    def copy(self):
        """Makes a copy of the game piece

        Returns:
            GamePiece: copy of self
        """
        tmp = GamePiece(color=self.color, id=self.id, speed=self.turtle.speed())
        tmp.turtle = self.turtle # TODO: This could lead to problems, a better approach would be to calculate the future position to avoid copying an object
        return tmp

    def is_on_field(self) -> bool:
        """Returns if a game piece is on the field

        On field means anywhere on the field except the home positions
        A game piece can already be on the target and that counts as true

        Returns:
            bool: true if game piece is on field, else false
        """
        return self.get_pos() not in home_positions

    def is_playable(self) -> bool:
        # TODO: Renaming or refactoring cause it doesn't check fully if the game piece is playable
        """Checks if game piece is not in home positions and not in target positions

        Returns:
            bool: true if game piece is playable
        """
        not_home = self.is_on_field()
        in_target = self.get_pos() == target_positions[self.color][4-self.id]
        return not_home and not in_target

    def get_pos(self) -> tuple[int | float]:
        """Getter for the turtle's position

        Returns:
            tuple: turtle's position (x, y)
        """
        return convert_Vec2D_to_tuple(self.turtle.pos())

    def get_ID(self) -> int:
        """Getter for game piece's id

        Returns:
            int: game piece's id
        """
        # TODO: I would like to get rid of this feature
        return self.id


def main():
    """For testing and debugging purposes"""
    game_piece = GamePiece(color="green", id=1, speed="fastest")
    print(game_piece)


if __name__ == "__main__":
    main()
