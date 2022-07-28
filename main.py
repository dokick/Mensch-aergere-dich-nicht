from turtle import Turtle, exitonclick
from random import choice
from gameBoard import game_board, colors, target_positions, home_positions, home_angles
from gamePiece import GamePiece
from tools import dice


# TODO: setup() abhängig von der Anzahl an Spielern machen die spielen
def setup(amountOfPlayers=4) -> dict[str, list[GamePiece]]:
    players: dict[str, list[GamePiece]] = {}
    for color in colors:
        players[color] = [GamePiece(color=color, id=i+1, speed="fastest")
                          for i in range(4)]
    # print(players)

    for color, gamePieces in players.items():
        for i, gamePiece in enumerate(gamePieces):
            gamePiece.turtle.penup()
            gamePiece.turtle.seth(home_angles[color])
            gamePiece.turtle.goto(home_positions[color][i])

    return players


def has_one_player_won(players: dict[str, list[GamePiece]]) -> str | None:
    for color, gamePieces in players.items():
        for gamePiece in gamePieces:
            if gamePiece.getPos() not in target_positions(color):
                return None
            return color


def permission() -> bool:
    for i in range(3):
        if dice() == 6:
            return True
    return False


def move(gamePiece: GamePiece):
    pass


def start_game(amountOfPlayers=4):
    players = setup(amountOfPlayers)
    currentColor = choice(colors)
    indexOfCurrentColor = colors.index(currentColor)
    currentID = {"yellow": 1, "green": 1, "red": 1, "black": 1}

    while not has_one_player_won(players):
        for gamePiece in players[currentColor]:
            if gamePiece.getID() == currentID[currentColor]:
                move(gamePiece=gamePiece)
        
        
        indexOfCurrentColor += 1
        currentColor = colors[(indexOfCurrentColor+1) % 4]
        indexOfCurrentColor = colors.index(currentColor)
        break


def main():

    game_board()
    start_game()
    exitonclick()
    return


if __name__ == "__main__":
    main()
