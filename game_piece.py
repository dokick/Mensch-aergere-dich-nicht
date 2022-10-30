"""
This module represents a game piece
"""
from turtle import Screen, Turtle, exitonclick

from game_board import (GAME_PIECE_COLORS, GOAL_POSITIONS, HOME_ANGLES,
                       HOME_POSITIONS, STARTING_VERTICES, SIZES,
                       VERTEX_FORE_GOAL, VERTICES_FOR_LEFT_TURN,
                       VERTICES_FOR_RIGHT_TURN)
from tools import convert_Vec2D_to_tuple


class GamePiece:
    """This class represents one game piece in the game of a player

    Attributes:
        turtle (Turtle): the turtle of a game piece
        color (str): the color of the game piece
        home_position (tuple[float]): home position of this game piece
        steps (int): steps the game piece has made
        max_steps (int): max amount of steps the game piece can make
        is_done (bool): is game piece in goal and not playable

    Methods:
        __init__(self, color: str, home_position: tuple[float, float],
                 *, speed: int = 0) -> None
        __bool__(self) -> bool
        __repr__(self) -> str
        move(self, steps: int) -> GamePiece
        get_out(self) -> GamePiece
        reset(self) -> GamePiece
        get_future_pos(self, steps: int) -> tuple[float]
        get_pos(self) -> tuple[float]
        is_on_field(self) -> bool
        is_done_(self, occupied_goal_fields: dict[tuple[float], bool]) -> bool
        is_in_goal(self) -> bool
        where_in_goal_index(self) -> int
    """

    def __init__(self, board_size: str, color: str, home_position: tuple[float, float],
                 *, speed: int = 0) -> None:
        """Initialzing attributes and setting up turtle"""
        self.board_size = board_size
        self.turtle = Turtle()
        self.color: str = color
        self.home_position = home_position
        self.steps: int = 0
        self.max_steps = 6
        self.is_done = False

        screen = Screen()
        screen.colormode(255)
        self.turtle.fillcolor(GAME_PIECE_COLORS[self.color])
        self.turtle.pencolor(255, 255, 255)
        self.turtle.speed(speed)
        self.turtle.shape("turtle")
        self.turtle.penup()

    def __bool__(self) -> bool:
        """Existence of a game piece means true"""
        return True

    def __repr__(self) -> str:
        return f"{self.color}\n{self.home_position = }\n{self.steps = }\n{self.turtle.speed() = }"

    def move(self, steps: int):
        """Moving the turtle of the game piece

        Args:
            steps (int): amount of steps the game piece goes

        Returns:
            GamePiece: self
        """
        dist = SIZES[self.board_size]
        for _ in range(steps):
            if self.get_pos() in VERTICES_FOR_LEFT_TURN(self.board_size):
                self.turtle.left(90)
            if (self.get_pos() in VERTICES_FOR_RIGHT_TURN(self.board_size)
                    or self.get_pos() == VERTEX_FORE_GOAL(self.board_size)[self.color]):
                self.turtle.right(90)
            self.turtle.forward(dist)
            self.steps += 1
        return self

    def get_out(self):
        """Puts the game piece on it's starting position

        Returns:
            GamePiece: self
        """
        self.turtle.goto(STARTING_VERTICES(self.board_size)[self.color])
        return self

    def reset(self):
        """Resets a game piece, if it got kicked out

        Returns:
            GamePiece: self
        """
        self.steps = 0
        self.turtle.goto(self.home_position)
        self.turtle.seth(HOME_ANGLES[self.color])
        return self

    def get_future_pos(self, steps: int) -> tuple[float]:
        """Calculates the furure position of the game piece's turtle

        Args:
            steps (int): amount of steps the game piece goes

        Returns:
            tuple[float]: future position of the turtle
        """
        dist = SIZES[self.board_size]
        future_pos = list(self.get_pos())
        future_heading = self.turtle.heading()
        for _ in range(steps):
            if tuple(future_pos) in VERTICES_FOR_LEFT_TURN(self.board_size):
                future_heading = (future_heading + 90) % 360
            if (tuple(future_pos) in VERTICES_FOR_RIGHT_TURN(self.board_size)
                    or tuple(future_pos) == VERTEX_FORE_GOAL(self.board_size)[self.color]):
                future_heading = (future_heading - 90) % 360

            if future_heading == 0:
                future_pos[0] += dist  # x+
            elif future_heading == 90:
                future_pos[1] += dist  # y+
            elif future_heading == 180:
                future_pos[0] -= dist  # x-
            elif future_heading == 270:
                future_pos[1] -= dist  # y-
        return tuple(future_pos)

    def get_pos(self) -> tuple[float, float]:
        """Getter for the turtle's position

        Returns:
            tuple: turtle's position (x, y)
        """
        return convert_Vec2D_to_tuple(self.turtle.pos())

    def is_on_field(self) -> bool:
        """Returns if a game piece is on the field

        On field means anywhere on the field except the home positions
        A game piece can already be on the goal and that counts as true

        Returns:
            bool: true if game piece is on field
        """
        return self.get_pos() not in HOME_POSITIONS(self.board_size)[self.color]
        # return self.get_pos() != self.home_position

    def is_done_(self, occupied_goal_fields: dict[tuple[float], bool]) -> bool:
        """Returns if a game piece shouldn't move anymore

        A goal field is occupied when all the ongoing goal fields are occupied
        and a game piece on it shouldn't move anymore

        Args:
            occupied_goal_fields (dict[tuple[float], bool]): dict of goal fields and if they are occupied

        Returns:
            bool: true if the game piece shouldn't move anymore
        """
        if self.get_pos() in occupied_goal_fields.keys():
            return occupied_goal_fields[self.get_pos()]
        return False

    def is_in_goal(self) -> bool:
        """Check method if game piece is in goal

        Returns:
            bool: true if game piece is somewhere on the goal positions
        """
        return self.get_pos() in GOAL_POSITIONS(self.board_size)[self.color]

    def where_in_goal_index(self) -> int:
        """Getting the goal position of a game piece per index

        0 is the most inner position
        3 the most outer position
        -1 if not in goal

        Returns:
            int: the index of the goal position
        """
        if self.is_in_goal():
            for idx, pos in enumerate(GOAL_POSITIONS(self.board_size)[self.color]):
                if pos == self.get_pos():
                    return idx
        return -1


def main():
    """For testing and debugging purposes"""
    size = "medium"
    game_piece = GamePiece(size, "green", (100, 100))
    print(game_piece)
    print(bool(game_piece))  # True
    print(not game_piece)  # False

    print(game_piece.get_future_pos(2))
    print(game_piece.move(2).get_pos())
    print(game_piece.reset().get_pos())
    exitonclick()


if __name__ == "__main__":
    main()
