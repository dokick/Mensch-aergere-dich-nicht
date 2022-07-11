from turtle import Turtle, exitonclick
from random import choice
from gameBoard import gameBoard, colors, targetPositions, homePositions, homeAngles
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
            gamePiece.turtle.seth(homeAngles[color])
            gamePiece.turtle.goto(homePositions[color][i])

    return players


def hasOnePlayerWon(players: dict) -> str | None:
    for color, gamePieces in players.items():
        for gamePiece in gamePieces:
            if gamePiece.getPos() not in targetPositions(color):
                return None
            return color


def permission() -> bool:
    for i in range(3):
        if dice() == 6:
            return True
    return False


def startGame(amountOfPlayers=4):
    players = setup(amountOfPlayers)
    startingColor = choice(colors)
    indexOfStartingColor = colors.index(startingColor)
    return
    while not hasOnePlayerWon(players):
        # players[startingColor][0]
        indexOfStartingColor += 1
        startingColor = colors[(indexOfStartingColor+1) % 4]
        break


def main():

    gameBoard()
    startGame()
    exitonclick()
    return


if __name__ == "__main__":
    main()
