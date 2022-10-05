"""
Module-Structure:

- create_with_matrix(x: float, y: float = None, /)
- game_board(size: str = "medium")
- draw_winner_on_board(color: str)
- data structures for game mechanics
"""

from turtle import exitonclick, hideturtle, shape, speed, fillcolor, pencolor, pensize, penup, pendown, goto, begin_fill, end_fill, seth, circle, left, right, forward, back, write


MATRIX = ((-1, 1), (1, 1), (1, -1), (-1, -1))


def create_with_matrix(x: float, y: float = None, /) -> tuple[tuple[float]]:
    """Creates tuple with the following pattern ((-x, y), (y, x), (x, -y), (-y, -x))"""
    if y is None:
        y = x
    tmp = []
    for i, j in MATRIX:
        tmp.append((i*x, j*y))
        x, y = y, x
    return tuple(tmp)


def game_board(size: str = "medium") -> None:
    """Draws a game board
    
    Args:
        size (str): small, medium or large
    """

    def draw_one_unit():
        """Draws one field/unit. That includes the circle and the leading line"""
        begin_fill()
        circle(STEP_SIZE//4)
        end_fill()
        left(90)
        penup()
        forward(STEP_SIZE//2)
        pendown()
        forward(STEP_SIZE//2)
        right(90)

    shape('turtle')
    speed(0)

    # background
    fillcolor('#fdeb95')
    pencolor('red')
    w = 20
    pensize(w)
    penup()
    outer_outline = STEP_SIZE*5 + STEP_SIZE//4 + 10 + 10 + w//2
    goto(-outer_outline, -outer_outline)
    pendown()
    begin_fill()
    for pos in create_with_matrix(outer_outline):
        goto(pos)
    end_fill()
    pencolor('black')
    pensize(4)
    penup()
    inner_outline = STEP_SIZE*5 + STEP_SIZE//4 + 10
    goto(-inner_outline, -inner_outline)
    pendown()
    for pos in create_with_matrix(inner_outline):
        goto(pos)
    penup()

    # game fields
    goto(-(STEP_SIZE*5 + STEP_SIZE//4), STEP_SIZE)
    seth(270)
    fillcolor('white')
    for i in range(4):
        for j in range(2):
            pendown()
            for _ in range(4):
                draw_one_unit()
            penup()
            forward(STEP_SIZE//4)
            left(90)
            forward(STEP_SIZE//4)
        right(90)
        back(STEP_SIZE//2)
        right(90)
        pendown()
        draw_one_unit()
        draw_one_unit()
        penup()
        back(STEP_SIZE//4)
        right(90)
        back(STEP_SIZE//4)

    # home, start & goal fields
    dict1 = {color: pos for color, pos in zip(COLORS, create_with_matrix(
        STEP_SIZE*5 + STEP_SIZE//4, STEP_SIZE*5 - STEP_SIZE//8))}
    dict2 = {color: pos for color, pos in zip(
        COLORS, create_with_matrix(STEP_SIZE*5 + STEP_SIZE//4, STEP_SIZE))}
    dict3 = {color: pos for color, pos in zip(
        COLORS, create_with_matrix(STEP_SIZE*4 + STEP_SIZE//4, 0))}
    h = 270
    for color in COLORS:
        fillcolor(color)
        seth(h)
        h -= 90

        # home fields
        goto(dict1[color])
        for i in range(2):
            if i == 1:
                left(90)
                forward((STEP_SIZE//4 + STEP_SIZE//8)*2 + 10)
                right(90)
                back((STEP_SIZE//4 + STEP_SIZE//8)*2 + 10)
            pendown()
            begin_fill()
            circle(STEP_SIZE//4 + STEP_SIZE//8)
            end_fill()
            penup()
            forward((STEP_SIZE//4 + STEP_SIZE//8)*2 + 10)
            pendown()
            begin_fill()
            circle(STEP_SIZE//4 + STEP_SIZE//8)
            end_fill()
            penup()

        # start field
        goto(dict2[color])
        pendown()
        begin_fill()
        circle(STEP_SIZE//4)
        end_fill()
        penup()

        # goal fields
        goto(dict3[color])
        for _ in range(4):
            pendown()
            begin_fill()
            circle(STEP_SIZE//4)
            end_fill()
            penup()
            left(90)
            forward(STEP_SIZE)
            right(90)

    school = 'Blackadder ITC'
    home = 'AR DECODE'
    off = 0
    for idx, (word, pos) in enumerate(zip(('Mensch', 'ärgere', 'nicht', 'dich'), create_with_matrix(STEP_SIZE*2 + STEP_SIZE//2))):
        if idx == 2:
            off = STEP_SIZE//4
        goto(pos[0], pos[1] - off)
        write(word, move=False, align='center', font=(
            school, STEP_SIZE//2 + STEP_SIZE//8, 'normal'))
    hideturtle()


def draw_winner_on_board(color: str):
    hideturtle()
    speed(0)
    pencolor(color)
    penup()
    goto(0, 100)
    write(color.upper(), move=False, align="center",
          font=("Arial", 150, "normal"))
    pencolor("black")
    goto(0, -300)
    write("WON", move=False, align="center", font=("Arial", 150, "normal"))


STEP_SIZE: int = 80
"""Distance between two fields, should be divisible by 8"""

COLORS: tuple[str] = ("yellow", "green", "red", "black")
"""Order of colors beginning in the top left corner and then going clockwise: yellow, green, red, black"""
GAME_PIECE_COLORS = {color: rgb for color, rgb in zip(COLORS, ((255, 215, 0), (15, 200, 11), (176, 0, 0), (64, 64, 64)))}

HOME_ANGLES = {color: angle for color, angle in zip(COLORS, (90, 0, 270, 180))}
"""Angles accessed by color so at the beginning game pieces look in the right direction (easier setup)"""

vertices_for_left_turn = create_with_matrix(STEP_SIZE)
"""Vertex positions where a game piece has to turn left"""

vertices_for_right_turn = create_with_matrix(STEP_SIZE, STEP_SIZE*5) + create_with_matrix(STEP_SIZE*5, STEP_SIZE)
"""Vertex positions where a game piece has to turn right"""

starting_vertices = {color: pos for color, pos in zip(COLORS, create_with_matrix(STEP_SIZE*5, STEP_SIZE))}
"""Vertex position accessed by color where a game piece starts"""

turning_vertices_per_color = {color: pos for color, pos in zip(COLORS, create_with_matrix(STEP_SIZE*5, 0))}
"""Vertex position accessed by color infront of the goal positon,
so a game piece doesn't travel in an endless loop on the game board"""

enough_vertices_per_color: dict[str, tuple[tuple[float]]] = {"yellow": ((-400.00, 0.00), (-400.00, -80.00)),
                                                             "green": ((0.00, 400.00), (-80.00, 400.00)),
                                                             "red": ((400.00, 0.00), (400.00, 80.00)),
                                                             "black": ((0.00, -400.00), (80.00, -400.00))}
"""Vertex positions accessed by color that are two steps infront of the goal.
Used to ensure that there are enough vertices a game piece can travel"""

goal_positions: dict[str, tuple[tuple[float]]] = {"yellow": ((-80.00, 0.00), (-160.00, 0.00), (-240.00, 0.00), (-320.00, 0.00)),
                                                  "green": ((0.00, 80.00), (0.00, 160.00), (0.00, 240.00), (0.00, 320.00)),
                                                  "red": ((80.00, 0.00), (160.00, 0.00), (240.00, 0.00), (320.00, 0.00)),
                                                  "black": ((0.00, -80.00), (0.00, -160.00), (0.00, -240.00), (0.00, -320.00))}
"""Vertex goal positions accessed by color"""

home_positions: dict[str, tuple[tuple[float]]] = {"yellow": ((-390.00, 390.00), (-320.00, 390.00), (-390.00, 320.00), (-320.00, 320.00)),
                                                  "green": ((320.00, 390), (390.00, 390.00), (320.00, 320.00), (390.00, 320.00)),
                                                  "red": ((320.00, -320.00), (390.00, -320.00), (320.00, -390.00), (390.00, -390.00)),
                                                  "black": ((-390.00, -320.00), (-320.00, -320.00), (-390.00, -390.00), (-320.00, -390.00))}
"""Vertex home positions accessed by color"""


def main():
    """For testing and debugging purposes"""
    game_board()
    for color in COLORS:
        draw_winner_on_board(color)
    exitonclick()


if __name__ == "__main__":
    main()
