from gamePiece import GamePiece
from tools import dice


class Player:
    """A player

    Attributes:
        color (str): the color of the player
        game_pieces (list[GamePiece]): all game pieces of the same color assigned to a player

    Methods:
        __init__(self, *, color: str, game_pieces: list[GamePiece]) -> None
        __bool__(self) -> bool
        __repr__(self) -> str
    """

    def __init__(self, *, color: str, game_pieces: list[GamePiece]) -> None:
        self.color = color
        # if len(game_pieces) > 4:
        # raise Exception("Too much game pieces")
        self.game_pieces = game_pieces

    def __bool__(self) -> bool:
        """The existence of a player should be treated as True"""
        return True

    def __repr__(self) -> str:
        return f"{self.color =}\n {self.game_pieces = }"

    def validate_moves(self, *, steps: int, players: list) -> list[GamePiece]:
        """Validates all potential moves that the player has

        First handles if the game piece would land on a field with a game piece of the same color
        Second handles if there are enough fields that a game piece can move

        Args:
            steps (int): amount of steps the game piece goes
            players (list[Player]): information of all players

        Returns:
            list[GamePiece]: list of all game pieces that qualify for a valid move, if empty player has no valid moves
        """
        potential_game_pieces: list[GamePiece] = []

        for game_piece in self.game_pieces:
            for other_game_piece in self.game_pieces:
                if game_piece is other_game_piece:
                    continue
                if game_piece.copy().move(steps).get_pos() == other_game_piece.get_pos():
                    continue
                potential_game_pieces.append(game_piece)

        for game_piece in potential_game_pieces:
            pass  # TODO: Implementation

    def move(self):
        # TODO: Needs changes
        current_game_piece = self.get_current_game_piece()
        current_game_piece.move(dice())

    def get_current_game_piece(self) -> GamePiece:
        # TODO: Needs changes
        return self.game_pieces[0]


def main():
    player = Player(color="yellow", game_pieces=[GamePiece(
        color="yellow", id=i+1, speed="fastest") for i in range(4)])
    print(player)
    print(bool(player))  # True
    print(not player)  # False


if __name__ == "__main__":
    main()
