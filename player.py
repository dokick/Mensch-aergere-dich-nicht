from gamePiece import GamePiece
from gameBoard import goal_positions, home_positions, enough_vertices_per_color


class Player:
    """A player

    Attributes:
        color (str): the color of the player
        game_pieces (list[GamePiece]): all game pieces of the same color assigned to a player

    Methods:
        __init__(self, *, color: str, game_pieces: list[GamePiece]) -> None
        __bool__(self) -> bool
        __repr__(self) -> str
        get_valid_game_pieces(self, *, steps: int) -> list[GamePiece]
        move(self, steps: int) -> None
        pick_game_piece(self, game_pieces: list[GamePiece]) -> GamePiece
    """

    def __init__(self, *, color: str, game_pieces: list[GamePiece]) -> None:
        self.color = color
        self.game_pieces = game_pieces

    def __bool__(self) -> bool:
        """Existence of a player should be treated as True"""
        return True

    def __repr__(self) -> str:
        return f"{self.color =}\n {self.game_pieces = }"

    def get_valid_game_pieces(self, steps: int) -> list[GamePiece]:
        """Validates all potential moves that the player has

        First handles if there are enough fields that a game piece can move
        Second handles if the game piece would land on a field with a game piece of the same color

        This is handled all in one function to ensure order,
        because if checked out of order the case could happen
        that a future position is calculated that doesn't exist,
        because there weren't enough fields left

        Args:
            steps (int): amount of steps the game piece goes
            players (list[Player]): information of all players

        Returns:
            list[GamePiece]: list of all game pieces that qualify for a valid move, if empty player has no valid moves
        """
        # TODO: Implementation if a game piece is done
        potential_game_pieces: list[GamePiece] = []

        for game_piece in self.game_pieces:
            if game_piece.get_pos() not in goal_positions[self.color] or game_piece.get_pos() not in enough_vertices_per_color[self.color]:
                potential_game_pieces.append(game_piece)

            if game_piece.get_pos() == goal_positions[self.color][1] and steps > 1:
                continue
            elif game_piece.get_pos() == goal_positions[self.color][2] and steps > 2:
                continue
            elif game_piece.get_pos() == goal_positions[self.color][3] and steps > 3:
                continue
            elif game_piece.get_pos() == enough_vertices_per_color[self.color][0] and steps > 4:
                continue
            elif game_piece.get_pos() == enough_vertices_per_color[self.color][1] and steps > 5:
                continue
            potential_game_pieces.append(game_piece)

        final_game_pieces: list[GamePiece] = []

        for game_piece in potential_game_pieces:
            for other_game_piece in self.game_pieces:
                if game_piece is other_game_piece:
                    continue
                if game_piece.get_future_pos(steps) == other_game_piece.get_pos():
                    continue
                final_game_pieces.append(game_piece)

    def pick_game_piece(self, steps: int) -> GamePiece | None:
        """Gets all the valid game pieces and picks a final game piece

        Deciding mechanisms can be implemented here

        Args:
            steps (int): amount of steps the game piece goes

        Returns:
            GamePiece: the game piece that gets finally picked for the move
        """
        game_pieces = self.get_valid_game_pieces(steps)
        if not game_pieces:
            return None

        if steps < 4:
            for game_piece in game_pieces:
                if game_piece.where_in_goal_index() >= steps:
                    return game_piece

        pick = game_pieces[0]
        for game_piece in game_pieces:
            if game_piece.steps > pick.steps:
                pick = game_piece
        return pick

    def move(self, steps: int) -> GamePiece:
        """Makes the move for a player

        Args:
            steps (int): amount of steps the game piece goes
        """
        current_game_piece = self.pick_game_piece(steps)
        if not current_game_piece:
            return
        return current_game_piece.move(steps)


def main():
    color = "yellow"
    player = Player(color=color, game_pieces=[
                    GamePiece(color, home_positions[color][i]) for i in range(4)])
    print(player)
    print(bool(player))  # True
    print(not player)  # False


if __name__ == "__main__":
    main()
