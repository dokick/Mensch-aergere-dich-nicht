from turtle import Turtle, exitonclick
from random import choice
from gameBoard import game_board, COLORS, target_positions, home_positions, home_angles, enough_vertices_per_color
from gamePiece import GamePiece
from tools import dice


######################################### helper functions #########################################


def did_player_hit_other_players(*, player_being_checked: GamePiece, players: dict[str, list[GamePiece]]) -> GamePiece:
    """Helper function for the implementation of the game mechanic that players can hit other players

    Args:
        player_being_checked (GamePiece): the game piece that made a move
        players (dict): information of all players

    Returns:
        GamePiece: Returns the game piece that got hit by another player
    """
    for color, game_pieces in players.items():
        if color == player_being_checked.color:
            continue
        for game_piece in game_pieces:
            if player_being_checked.get_pos() == game_piece.get_pos():
                return game_piece


def is_game_piece_in_goal(player_being_checked: GamePiece) -> bool:
    """Helper function for getting if game piece is in goal positions

    Args:
        player_being_checked (GamePiece): game piece that makes the move

    Returns:
        bool: true if the game piece that made a move is already in one of the goal positions
    """
    return player_being_checked in target_positions


def has_color_one_player_outside(*, current_game_piece: GamePiece, players: dict[str, list[GamePiece]]) -> bool:
    """Checks if a player of one color has one of its game pieces on the board playing

    Args:
        current_game_piece (GamePiece): the game piece that makes the move
        players (dict): information of all players

    Returns:
        bool: true if at least one game piece of the color is on the board and playable
    """
    for game_piece in players[current_game_piece.color]:
        if game_piece.is_playable():
            return True
    return False


def has_one_player_won(players: dict[str, list[GamePiece]]) -> str | None:
    """Checks if a color has won yet

    Args:
        players (dict): information of all players

    Returns:
        str | None: the color of the winning player or None if no one has won yet
    """
    for color, game_pieces in players.items():
        for game_piece in game_pieces:
            if game_piece.get_pos() not in target_positions[color]:
                return None
            return color

######################################### End of helper functions #########################################


def permission() -> bool:
    """Gives a game piece the permission to leave home and get on field

    Returns:
        bool: true if the dice got a 6 in three throws
    """
    for i in range(3):
        if dice() == 6:
            return True
    return False


def validate_move(*, current_game_piece: GamePiece, steps: int, players: dict[str, list[GamePiece]]) -> bool:
    """Validates a move (is the move possible)

    Args:
        current_game_piece (GamePiece): game piece that makes the move
        steps (int): amount of steps the game piece goes
        players (dict): information of all players

    Returns:
        bool: true if move is valid
    """
    # TODO: Implementation
    temporary_game_piece = current_game_piece.copy()
    temporary_game_piece.move(steps)
    for game_piece in players[current_game_piece.color]:
        if game_piece.get_pos() == temporary_game_piece.get_pos():
            return False
    return True


def move(*, current_game_piece: GamePiece, players: dict[str, list[GamePiece]]):
    """Simulates and also handles the move in the game

    Args:
        current_game_piece (GamePiece): the game piece that makes a move
        players (dict): information of all players
    """
    # if color has no game piece to play with, player has to get a new game piece on the board
    # TODO: Refactor (next 4 lines shouldn't be here)
    if not has_color_one_player_outside(current_game_piece=current_game_piece, players=players):
        if permission():
            current_game_piece.move(dice())
            return

    steps = dice()
    if validate_move(current_game_piece=current_game_piece, steps=steps, players=players):
        current_game_piece.move(steps)

# TODO: setup() abhängig von der Anzahl an Spielern machen die spielen


def setup(amount_of_players=4) -> tuple[dict[str, list[GamePiece]], str]:
    """A setup function so the game can start with initial values

    Args:
        amount_of_players (int): the amount of players in the game (not implemented yet)

    Returns:
        tuple: first a dict with all the players, second the color that starts the game
    """
    players: dict[str, list[GamePiece]] = {}
    for color in COLORS:
        players[color] = [GamePiece(color=color, id=i+1, speed="fastest")
                          for i in range(4)]
    # print(players)

    for color, game_pieces in players.items():
        for i, game_piece in enumerate(game_pieces):
            game_piece.turtle.penup()
            game_piece.turtle.seth(home_angles[color])
            game_piece.turtle.goto(home_positions[color][i])

    current_color = choice(COLORS)

    return players, current_color


def start_game(amount_of_players=4):
    """Starts the game

    Args:
        amount_of_players (int): the amount of players that are playing (not implemented yet)
    """
    players, current_color = setup(amount_of_players)
    index_of_current_color = COLORS.index(current_color)
    current_ID = {"yellow": 1, "green": 1, "red": 1, "black": 1}

    while not has_one_player_won(players):
        current_game_piece = players[current_color][current_ID[current_color]]
        move(current_game_piece=current_game_piece, players=players)

        # for game_piece in players[current_color]:
        #     if game_piece.get_ID() == current_ID[current_color]:
        #         move(game_piece=game_piece)

        if is_game_piece_in_goal(current_game_piece):
            current_ID[current_game_piece.color] += 1

        index_of_current_color += 1
        current_color = COLORS[(index_of_current_color+1) % 4]
        break


def main():
    game_board()
    start_game()
    exitonclick()


if __name__ == "__main__":
    main()
