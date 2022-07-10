from turtle import Turtle, exitonclick
from random import choice
from gameBoard import gameBoard, vertices, colors, targetPositions
from gamePiece import GamePiece
from tools import dice


def setup() -> dict:
    players = {}
    for color in colors:
        players[color] = [GamePiece(color=color, speed="fastest")
                          for i in range(4)]
    print(players)
    return players


def hasOnePlayerWon(players: dict) -> str | None:
    for color, gamePieces in players.items():
        for gamePiece in gamePieces:
            if gamePiece.getPos() not in targetPositions(color):
                return None
            return color


def startGame():
    players = setup()
    startingColor = choice(colors)
    indexOfStartingColor = colors.index(startingColor)
    while not hasOnePlayerWon(players):
        indexOfStartingColor += 1
        startingColor = colors[(indexOfStartingColor+1) % 4]


def permission() -> bool:
    for i in range(3):
        if dice() == 6:
            return True
    return False


blue = list(range(4))
yellow = list(range(4))
green = list(range(4))
red = list(range(4))
for color in [blue, yellow, green, red]:
    for i in range(4):
        color[i] = Turtle()
        color[i].speed('fastest')
        color[i].pu()
        # colors[i].ht()
for figure in blue:
    figure.fillcolor('blue')
    figure.seth(180)
for figure in yellow:
    figure.fillcolor('yellow')
    figure.seth(90)
for figure in green:
    figure.fillcolor('green')
    figure.seth(0)
for figure in red:
    figure.fillcolor('red')
    figure.seth(270)


def start(color, n, figure_color):
    if permission():
        if figure_color == 'blue':
            color[n].goto(pos1)
        if figure_color == 'yellow':
            color[n].goto(pos4)
        if figure_color == 'green':
            color[n].goto(pos7)
        if figure_color == 'red':
            color[n].goto(pos10)
        return True
    return False


def move(color, n):
    came_out = True
    # blue
    if color[n].pos() == (-390, -320) or color[n].pos() == (-320, -320) or color[n].pos() == (-390, -390) or color[n].pos() == (-320, -390):
        came_out = start(color, n, 'blue')
    # yellow
    if color[n].pos() == (-390, 390) or color[n].pos() == (-320, 390) or color[n].pos() == (-390, 320) or color[n].pos() == (-320, 320):
        came_out = start(color, n, 'yellow')
    # green
    if color[n].pos() == (320, 390) or color[n].pos() == (390, 390) or color[n].pos() == (320, 320) or color[n].pos() == (390, 320):
        came_out = start(color, n, 'green')
    # red
    if color[n].pos() == (320, -320) or color[n].pos() == (390, -320) or color[n].pos() == (320, -390) or color[n].pos() == (390, -390):
        came_out = start(color, n, 'red')
    if came_out:
        for i in range(dice()):
            print('Aktuell:', color[n].pos())
            print('Pos2:', pos2)
            print(color[n].pos() == pos2)
            print('Pos1:', pos1)
            print(color[n].pos() == pos1)
            if color[n].pos() == pos2 or color[n].pos() == pos5 or color[n].pos() == pos8 or color[n].pos() == pos11:
                color[n].lt(90)
            if color[n].pos() == pos1 or color[n].pos() == pos3 or color[n].pos() == pos4 or color[n].pos() == pos6 or color[n].pos() == pos7 or color[n].pos() == pos9 or color[n].pos() == pos10 or color[n].pos() == pos12:
                color[n].rt(90)
            color[n].fd(80)


def main():
    gameBoard()
    exitonclick()
    return
    nB = 0
    nY = 0
    nG = 0
    nR = 0
    colors = ('blue', 'yellow', 'green', 'red')
    # current_player=random.choice(colors)
    current_player = 'blue'
    print(current_player)
    while True:
        if current_player == 'blue':
            move(blue, nB)
            break
            current_player = 'yellow'
        if current_player == 'yellow':
            move(yellow, nY)
            current_player = 'green'
        if current_player == 'green':
            move(green, nG)
            current_player = 'red'
        if current_player == 'red':
            move(red, nR)
            current_player = 'blue'


if __name__ == "__main__":
    main()
