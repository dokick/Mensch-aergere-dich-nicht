from turtle import Screen, Turtle, forward, pos, left, right, exitonclick
from gameBoard import GAME_PIECE_COLORS, home_positions, goal_positions, starting_vertices, vertices_for_left_turn, vertices_for_right_turn, turning_vertices_per_color
from tools import convert_Vec2D_to_tuple


class GamePiece:
    """This class represents one game piece in the game of a player

    Attributes:
        turtle (Turtle): the turtle of a game piece
        color (str): the color of the game piece
        home_position (tuple[int | float]): home position of this game piece
        steps (int): steps the game piece has made

    Methods:
        __init__(self, color: str, home_position: tuple[int | float], *, speed: str = "fastest") -> None
        __bool__(self) -> bool
        __repr__(self) -> str
        move(self, steps: int) -> GamePiece
        get_out(self) -> GamePiece
        get_future_pos(self, steps: int) -> tuple[int | float]
        is_on_field(self) -> bool
        is_done(self, occupied_goal_fields: dict[tuple[int | float], bool]) -> bool
        is_in_goal(self) -> bool
        where_in_goal_index(self) -> int
        reset(self) -> GamePiece
        get_pos(self) -> tuple[int | float]
    """

    def __init__(self, color: str, home_position: tuple[int | float], *, speed: str = "fastest") -> None:
        """Initialzing attributes and setting up turtle"""
        self.turtle = Turtle()
        self.color: str = color
        self.home_position = home_position
        self.steps: int = 0

        screen = Screen()
        screen.colormode(255)
        self.turtle.fillcolor(GAME_PIECE_COLORS[self.color])
        self.turtle.speed(speed=speed)
        self.turtle.shape("turtle")
        self.turtle.penup()

    def __bool__(self) -> bool:
        """Existence of a game piece means true"""
        return True

    def __repr__(self) -> str:
        return f"{self.color = }\n{self.home_position = }\n{self.steps = }\n{self.turtle.speed() = }"

    def move(self, steps: int):
        """Moving the turtle of the game piece

        Args:
            steps (int): amount of steps the game piece goes

        Returns:
            GamePiece: self
        """
        for i in range(steps):
            if self.get_pos() in vertices_for_left_turn:
                self.turtle.left(90)
            if self.get_pos() in vertices_for_right_turn or self.get_pos() == turning_vertices_per_color[self.color]:
                self.turtle.right(90)
            self.turtle.forward(80)
            self.steps += 1
        return self

    def get_out(self):
        """Puts the game piece on it's starting position

        Returns:
            GamePiece: self
        """
        self.turtle.goto(starting_vertices[self.color])
        return self

    def get_future_pos(self, steps: int) -> tuple[int | float]:
        """Method for calculating the furure position of the game piece's turtle

        Args:
            steps (int): amount of steps the game piece goes

        Returns:
            tuple[int | float]: future position of the turtle 
        """
        future_pos = list(self.get_pos())
        future_heading = self.turtle.heading()
        for i in range(steps):
            if future_pos in vertices_for_left_turn:
                future_heading = (future_heading + 90) % 360
            if future_pos in vertices_for_right_turn or future_pos == turning_vertices_per_color[self.color]:
                future_heading = (future_heading - 90) % 360

            if future_heading == 0:
                future_pos[0] += 80  # x+
            elif future_heading == 90:
                future_pos[1] += 80  # y+
            elif future_heading == 180:
                future_pos[0] -= 80  # x-
            elif future_heading == 270:
                future_pos[1] -= 80  # y-
        return (future_pos[0], future_pos[1])

    def is_on_field(self) -> bool:
        """Returns if a game piece is on the field

        On field means anywhere on the field except the home positions
        A game piece can already be on the target and that counts as true

        Returns:
            bool: true if game piece is on field
        """
        return self.get_pos() not in home_positions[self.color]

    def is_done(self, occupied_goal_fields: dict[tuple[int | float], bool]) -> bool:
        """Returns if a game piece shouldn't move anymore

        A goal field is occupied when all the ongoing goal fields are occupied
        and a game piece is on it that shouldn't move anymore

        Args:
            occupied_goal_fields (dict[tuple[int | float], bool]): dict of the goal fields and if they are occupied

        Returns:
            bool: true if the game piece shouldn't move anymore
        """
        if self.get_pos() in occupied_goal_fields.keys():
            return occupied_goal_fields[self.get_pos()]
        return False


    def is_in_goal(self) -> bool:
        """Check method if game piece is in goal

        Returns:
            bool: true if game piece is somewhere in the goal positions
        """
        return self.get_pos() in goal_positions

    def where_in_goal_index(self) -> int:
        """Getting the goal position of a game piece per index

        Zero is the most inner position
        Three the most outer position

        Returns:
            int: the index of the goal position
        """
        if self.is_in_goal():
            for idx, coord in enumerate(goal_positions[self.color]):
                if coord == self.get_pos():
                    return idx

    def reset(self):
        """Resets a game piece, if it got kicked out

        Returns:
            GamePiece: self
        """
        self.steps = 0
        self.turtle.goto(self.home_position)
        return self

    def get_pos(self) -> tuple[int | float]:
        """Getter for the turtle's position

        Returns:
            tuple: turtle's position (x, y)
        """
        return convert_Vec2D_to_tuple(self.turtle.pos())


def main():
    """For testing and debugging purposes"""
    game_piece = GamePiece("green", (100, 100))
    print(game_piece)
    print(bool(game_piece))  # True
    print(not game_piece)  # False

    print(game_piece.get_future_pos(2))
    print(game_piece.move(2).get_pos())
    print(game_piece.reset().get_pos())
    exitonclick()


if __name__ == "__main__":
    main()
