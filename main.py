from turtle import Turtle, exitonclick
from random import choice
from gameBoard import game_board, colors, target_positions, home_positions, home_angles
from gamePiece import GamePiece
from tools import dice


# TODO: setup() abhängig von der Anzahl an Spielern machen die spielen
def setup(amount_of_players=4) -> dict[str, list[GamePiece]]:
    players: dict[str, list[GamePiece]] = {}
    for color in colors:
        players[color] = [GamePiece(color=color, id=i+1, speed="fastest")
                          for i in range(4)]
    # print(players)

    for color, game_pieces in players.items():
        for i, game_piece in enumerate(game_pieces):
            game_piece.turtle.penup()
            game_piece.turtle.seth(home_angles[color])
            game_piece.turtle.goto(home_positions[color][i])

    return players


def has_one_player_won(players: dict[str, list[GamePiece]]) -> str | None:
    for color, game_pieces in players.items():
        for game_piece in game_pieces:
            if game_piece.get_pos() not in target_positions(color):
                return None
            return color


def permission() -> bool:
    """Gives a game piece the permission to leave home and get on field
    
    Returns:
    bool: true if the dice got a 6 in thrree throws
    """
    for i in range(3):
        if dice() == 6:
            return True
    return False


def move(game_piece: GamePiece):
    pass


def start_game(amount_of_players=4):
    players = setup(amount_of_players)
    current_color = choice(colors)
    index_of_current_color = colors.index(current_color)
    current_ID = {"yellow": 1, "green": 1, "red": 1, "black": 1}

    while not has_one_player_won(players):
        for game_piece in players[current_color]:
            if game_piece.get_ID() == current_ID[current_color]:
                move(game_piece=game_piece)
        
        
        index_of_current_color += 1
        current_color = colors[(index_of_current_color+1) % 4]
        index_of_current_color = colors.index(current_color)
        break


def main():

    game_board()
    start_game()
    exitonclick()
    return


if __name__ == "__main__":
    main()
