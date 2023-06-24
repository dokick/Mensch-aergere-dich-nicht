"""
This module represents a player

Classes:
    Player
"""

from itertools import chain, product
from turtle import exitonclick
from typing import Optional

from game_board import (HOME_ANGLES, goal_positions, home_positions,
                        two_vertices_fore_goal)
from game_piece import GamePiece


class Player:
    """A player

    Attributes:
        color (str): color of the player
        game_pieces (list[GamePiece]): all game pieces of the same color
                                       assigned to a player

    Methods:
        __init__(self, *, board_size: str, color: str, game_pieces: list[GamePiece]) -> None
        __bool__(self) -> bool
        __repr__(self) -> str
        get_valid_game_pieces(self, steps: int) -> list[GamePiece]
        pick_game_piece(self, steps: int) -> GamePiece
        move(self, steps: int) -> Optional[GamePiece]
        check_if_done(self) -> None
        place_game_piece_on_start(self) -> Optional[GamePiece]
    """

    def __init__(self, *, board_size: str, color: str, game_pieces: list[GamePiece]) -> None:
        """Initializing attributes

        Args:
            board_size (str): size of game board. look into SIZES for sizes
            color (str): color of player
            game_pieces (list[GamePiece]): game pieces that belong to player
        """
        self.board_size = board_size
        self.color = color
        self.game_pieces = game_pieces

    def __bool__(self) -> bool:
        """Existence of a player should be treated as True"""
        return True

    def __str__(self) -> str:
        return f"{self.color =}\n{self.game_pieces = }"

    def __repr__(self) -> str:
        return f"Player(board_size={self.board_size}, color={self.color}, game_pieces={self.game_pieces})"

    def get_valid_game_pieces(self, steps: int) -> list[GamePiece]:
        """Validates all potential moves that the player has

        First handles if there are enough fields that a game piece can move
        Second handles if the game piece would land
        on a field with a game piece of the same color

        This is handled all in one function to ensure order,
        because if checked out of order the case could happen
        that a future position is calculated that doesn't exist,
        because there weren't enough fields left

        Args:
            steps (int): amount of steps the game piece goes

        Returns:
            list[GamePiece]: list of all game pieces that qualify for
                             a valid move, if empty player has no valid moves
        """
        # TODO: needs to be tested
        # if all game pieces are on home pos then all of them are valid
        are_home_pieces_valid = True
        for game_piece in self.game_pieces:
            if not game_piece.in_home():
                are_home_pieces_valid = False
                break

        if are_home_pieces_valid:
            return self.game_pieces

        valid_game_pieces: list[GamePiece] = []

        for game_piece in self.game_pieces:
            gp_pos = game_piece.get_pos()
            # filter of game piece being done or at home
            if game_piece.is_done or game_piece.in_home():
                continue

            # filter of having enough steps before goal
            invalid_fore_goal = False
            for idx, pos in enumerate(chain(goal_positions(self.board_size)[self.color],
                                            two_vertices_fore_goal(self.board_size)[self.color])):
                if pos != gp_pos:
                    continue
                if idx < steps:
                    invalid_fore_goal = True
                    break
            if invalid_fore_goal:
                continue

            # filter of player hitting own game pieces
            invalid_hitting_self = False
            for other_game_piece in self.game_pieces:
                if game_piece is other_game_piece:
                    continue
                if game_piece.get_future_pos(steps) == other_game_piece.get_pos():
                    invalid_hitting_self = True
                    break
            if invalid_hitting_self:
                continue

            valid_game_pieces.append(game_piece)

        return valid_game_pieces

    def pick_game_piece(self, steps: int) -> Optional[GamePiece]:
        """Gets all the valid game pieces and picks a final game piece

        Deciding mechanisms can be implemented here

        Args:
            steps (int): amount of steps the game piece goes

        Returns:
            GamePiece | None: game piece that gets finally picked for the move
                              or None if no game pieces are available
        """
        game_pieces = self.get_valid_game_pieces(steps)
        if not game_pieces:
            return None

        if steps < 4:
            for game_piece in game_pieces:
                if game_piece.in_goal() >= steps:
                    return game_piece

        pick = game_pieces[0]
        for game_piece in game_pieces:
            if game_piece.steps > pick.steps:
                pick = game_piece
        return pick

    def move(self, steps: int) -> Optional[GamePiece]:
        """Makes the move for a player

        First is there even a game piece.
        Second handle done situation if in goal.

        Args:
            steps (int): amount of steps the game piece goes

        Returns:
            GamePiece | None: game piece that got the move,
                              used to handle rules of the game
                              or None if no game pieces are available
        """
        current_game_piece = self.pick_game_piece(steps)
        if not current_game_piece:
            return
        current_game_piece = current_game_piece.move(steps)

        if current_game_piece.in_goal():
            self.check_if_done()

        return current_game_piece

    def check_if_done(self) -> None:
        """Checks the situation on the goal positions and marks done if needed

        First is it already done.
        Second is it on goal, if yes where.
        Third mark as done if it meets conditions
        """
        break_counter = 0
        for idx, (goal_pos, game_piece) in enumerate(product(goal_positions(self.board_size)[self.color], self.game_pieces)):
            # print(game_piece.get_pos() == goal_pos)
            if game_piece.get_pos() == goal_pos:
                game_piece.is_done = True
                break_counter = 0
                continue

            break_counter += 1

            # print(f"{break_counter = }")
            if break_counter == 4:
                break

            # print((idx + 1) % 4)
            if (idx + 1) % 4 == 0:
                # print("Inside of idx modulo 4")
                break_counter = 0

    def place_game_piece_on_start(self) -> Optional[GamePiece]:
        """Puts a game piece of the assigned color on the starting vertex"""
        game_pieces_at_home: list[GamePiece] = []
        for game_piece in self.game_pieces:
            if game_piece.in_home():
                game_pieces_at_home.append(game_piece)
        # print(game_pieces_at_home)
        if game_pieces_at_home:
            game_pieces_at_home[0].get_out()
            return game_pieces_at_home[0]


def main() -> None:
    """For testing and debugging purposes"""
    size = "medium"
    color1 = "yellow"
    player1 = Player(board_size = size,
                     color=color1,
                     game_pieces=[GamePiece(size,
                                            color1,
                                            home_positions(size)[color1][i])
                                            for i in range(4)])
    for game_piece in player1.game_pieces:
        game_piece.turtle.goto(game_piece.home_position)
    print(player1)
    print(bool(player1))  # True
    print(not player1)  # False

    color2 = "red"
    player2 = Player(board_size=size,
                     color=color2,
                     game_pieces=[GamePiece(size,
                                            color2,
                                            home_positions(size)[color2][i])
                                            for i in range(4)])
    yellow_start = (-400, 80)
    # pl2_gp = player2.game_pieces[0]
    # pl2_gp.turtle.goto(yellow_start)
    # pl2_gp.turtle.stamp()

    # pl1_gp = player1.move(3)
    # print(pl1_gp.get_pos())
    # print(pl2_gp.get_pos())


if __name__ == "__main__":
    main()
