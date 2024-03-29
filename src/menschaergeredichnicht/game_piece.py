"""This module represents a game piece"""
# pylint: disable-next=no-name-in-module
from turtle import Screen, Turtle, exitonclick

from game_board import (GAME_PIECE_COLORS, HOME_ANGLES, SIZES,
                        get_goal_factors, has_to_turn_left, has_to_turn_right,
                        home_positions, starting_vertices)
from tools import convert_Vec2D_to_tuple


class GamePiece:
    """This class represents one game piece in the game of a player

    Attributes:
        turtle (Turtle): turtle of game piece
        color (str): color of game piece
        home_position (tuple[float, float]): home position of game piece
        steps (int): steps the game piece has made
        is_done (bool): is game piece in goal and not playable

    Methods:
        __init__(self, board_size: str, color: str, home_position: tuple[float, float],
                 *, speed: int = 0) -> None
        __bool__(self) -> bool
        __repr__(self) -> str
        move(self, steps: int) -> GamePiece
        get_out(self) -> GamePiece
        reset(self) -> GamePiece
        get_future_pos(self, steps: int) -> tuple[float, float]
        get_pos(self) -> tuple[float, float]
        in_home(self) -> bool
        in_goal(self) -> int
    """

    def __init__(self, board_size: str, color: str, home_position: tuple[float, float],
                 *, speed: int = 0) -> None:
        """Initializing attributes and setting up turtle

        Args:
            board_size (str): size of game board. look into SIZES for sizes
            color (str): color of game piece
            home_position (tuple[float, float]): home pos of game board
            speed (int, optional): speed of game piece. Defaults to 0.
        """
        self.board_size = board_size
        self.turtle = Turtle(shape="turtle")
        self.color: str = color
        self.home_position = home_position
        self.steps: int = 0
        self.is_done = False

        screen = Screen()
        screen.colormode(255)
        self.turtle.fillcolor(GAME_PIECE_COLORS[self.color])
        self.turtle.pencolor(255, 255, 255)
        self.turtle.speed(speed)
        self.turtle.penup()

    def __bool__(self) -> bool:
        """Existence of a game piece means true"""
        return True

    def __str__(self) -> str:
        return f"{self.color = }\n{self.home_position = }\n{self.steps = }\n{self.is_done = }"

    def __repr__(self) -> str:
        return f"GamePiece({self.board_size}, {self.color}, {self.home_position}, speed={self.turtle.speed()})"

    def move(self, steps: int):
        """Moving the turtle of the game piece

        Args:
            steps (int): number of steps the game piece goes

        Returns:
            GamePiece: self
        """
        dist = SIZES[self.board_size]
        for _ in range(steps):
            x_pos, y_pos = self.get_pos()
            if has_to_turn_left(x_pos, y_pos, self.board_size):
                self.turtle.left(90)
            if has_to_turn_right(x_pos, y_pos, self.board_size, self.color):
                self.turtle.right(90)
            self.turtle.forward(dist)
            self.steps += 1
        return self

    def get_out(self):
        """Puts the game piece on it's starting position

        Returns:
            GamePiece: self
        """
        self.turtle.goto(starting_vertices(self.board_size)[self.color])
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

    def get_future_pos(self, steps: int) -> tuple[float, float]:
        """Calculates the future position of the game piece's turtle

        Args:
            steps (int): amount of steps the game piece goes

        Returns:
            tuple[float, float]: future position of the turtle
        """
        dist = SIZES[self.board_size]
        x_pos, y_pos = self.get_pos()
        future_heading = self.turtle.heading()
        for _ in range(steps):
            if has_to_turn_left(x_pos, y_pos, self.board_size):
                future_heading = (future_heading + 90) % 360
            if has_to_turn_right(x_pos, y_pos, self.board_size, self.color):
                future_heading = (future_heading - 90) % 360

            if future_heading == 0:
                x_pos += dist
            elif future_heading == 90:
                y_pos += dist
            elif future_heading == 180:
                x_pos -= dist
            elif future_heading == 270:
                y_pos -= dist
        return x_pos, y_pos

    def get_pos(self) -> tuple[float, float]:
        """Getter for the turtle's position

        Returns:
            tuple[float, float]: turtle's position (x, y)
        """
        return convert_Vec2D_to_tuple(self.turtle.pos())

    def in_home(self) -> bool:
        """Returns if a game piece is home

        Returns:
            bool: true if game piece is home
        """
        return self.get_pos() in home_positions(self.board_size)[self.color]
        # return self.get_pos() == self.home_position

    def in_goal(self) -> int:
        """Check method if game piece is in goal

        0 is the most inner position.
        3 the most outer position.
        -1 if not in goal

        Returns:
            int: index of the goal position
        """
        dist = SIZES[self.board_size]
        x_pos, y_pos = self.get_pos()
        factor_x, factor_y = get_goal_factors(self.color)
        x_set = {factor_x*i for i in range(1, 5)}
        y_set = {factor_y*i for i in range(1, 5)}
        if x_pos / dist in x_set and y_pos / dist in y_set:
            if len(y_set) == 1:
                return int(abs(x_pos) / dist) - 1
            return int(abs(y_pos) / dist) - 1
        return -1


def main():
    """For testing and debugging purposes"""
    size = "medium"
    dist = SIZES[size]
    home_position = (-dist*5, dist)
    game_piece = GamePiece(size, "yellow", home_position)
    print(game_piece)
    print(bool(game_piece))  # True
    print(not game_piece)  # False

    game_piece.turtle.goto(-80, 0)
    print(game_piece.in_goal())

    return
    game_piece.turtle.goto(home_position)
    game_piece.turtle.seth(90)
    print(game_piece.get_pos())
    print(game_piece.get_future_pos(2))
    print(game_piece.move(2).get_pos())
    game_piece.turtle.stamp()
    print(game_piece.reset().get_pos())
    exitonclick()


if __name__ == "__main__":
    main()
