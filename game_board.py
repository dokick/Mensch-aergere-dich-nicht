"""
This module draws the game board
and generates all necessary position coordinates inside of dicts or tuples

Functions:
    create_pattern(x: float,
                   y: float | None = None,
                   /, *, mutable = False) -> tuple[tuple[float, float]]
    game_board(size: str = "medium") -> None
    draw_winner_on_board(color: str)
    VERTICES_FOR_LEFT_TURN(size: str) -> tuple[tuple[float, float]]
    VERTICES_FOR_RIGHT_TURN(size: str) -> tuple[tuple[float, float]]
    STARTING_VERTICES(size: str) -> dict[str, tuple[float, float]]
    VERTEX_FORE_GOAL(size: str) -> dict[str, tuple[float, float]]
    TWO_VERTICES_FORE_GOAL(size: str) -> dict[str,
                                              tuple[tuple[float, float],
                                                    tuple[float, float]]]
    GOAL_POSITIONS(size: str) -> dict[str,
                                      tuple[tuple[float, float],
                                            tuple[float, float],
                                            tuple[float, float],
                                            tuple[float, float]]]
    HOME_POSITIONS(size: str) -> dict[str,
                                      tuple[tuple[float, float],
                                            tuple[float, float],
                                            tuple[float, float],
                                            tuple[float, float]]]
"""

from turtle import (back, begin_fill, circle, end_fill, exitonclick, fillcolor,
                    forward, goto, hideturtle, left, pencolor, pendown,
                    pensize, penup, right, seth, shape, speed, write)

SIZES: dict[str, int] = {"small": 64,
                         "medium": 80,
                         "large": 96}
"""Distance between two fields, should be divisible by 8"""

COLORS = ("yellow", "green", "red", "black")
"""Order of colors beginning in the top left corner and then going clockwise:
yellow, green, red, black"""
GAME_PIECE_COLORS: dict[str, tuple[int, int, int]] = {color: rgb
                                                      for color, rgb
                                                      in zip(COLORS,
                                                             ((255, 215, 0),
                                                              (15, 200, 11),
                                                              (176, 0, 0),
                                                              (64, 64, 64)))}

HOME_ANGLES = {color: angle
               for color, angle
               in zip(COLORS, (90, 0, 270, 180))}
"""Angles accessed by color so at the beginning game pieces
look in the right direction (easier setup)"""

MATRIX: tuple[tuple[int, int]] = ((-1, 1), (1, 1), (1, -1), (-1, -1))


# def create_pattern(x: float, y: float | None = None, /, *, mutable = False) -> tuple[tuple[float, float]] | list[list[float]]:
def create_pattern(x: float,
                   y: float | None = None,
                   /, *, mutable=False) -> tuple[tuple[float, float]]:
    """Creates tuple or list with the following pattern
    ((-x, y), (y, x), (x, -y), (-y, -x))

    Returns:
        tuple[tuple[float, float]]: pos pattern
    """
    if y is None:
        y = x

    used_type = tuple
    if mutable:
        used_type = list

    tmp = []
    for i, j in MATRIX:
        tmp.append(used_type((i*x, j*y)))
        x, y = y, x
    return used_type(tmp)


def game_board(size: str = "medium") -> None:
    """Draws a game board

    Args:
        size (str): small, medium or large
    """

    dist: int = SIZES[size]

    def draw_one_unit():
        """Draws one field/unit.
        That includes the circle and the leading line"""
        begin_fill()
        circle(dist//4)
        end_fill()
        left(90)
        penup()
        forward(dist//2)
        pendown()
        forward(dist//2)
        right(90)

    shape('turtle')
    speed(0)

    # background
    fillcolor('#fdeb95')
    pencolor('red')
    pen_width = 20
    pensize(pen_width)
    penup()
    outer_outline = dist*5 + dist//4 + 10 + 10 + pen_width//2
    goto(-outer_outline, -outer_outline)
    pendown()
    begin_fill()
    for pos in create_pattern(outer_outline):
        goto(pos)
    end_fill()
    pencolor('black')
    pensize(4)
    penup()
    inner_outline = dist*5 + dist//4 + 10
    goto(-inner_outline, -inner_outline)
    pendown()
    for pos in create_pattern(inner_outline):
        goto(pos)
    penup()

    # game fields
    goto(-(dist*5 + dist//4), dist)
    seth(270)
    fillcolor('white')
    for i in range(4):
        for j in range(2):
            pendown()
            for _ in range(4):
                draw_one_unit()
            penup()
            forward(dist//4)
            left(90)
            forward(dist//4)
        right(90)
        back(dist//2)
        right(90)
        pendown()
        draw_one_unit()
        draw_one_unit()
        penup()
        back(dist//4)
        right(90)
        back(dist//4)

    # home, start & goal fields
    home_fields = {color: pos for color, pos in zip(COLORS, create_pattern(
        dist*5 + dist//4, dist*5 - dist//8))}
    start_fields = {color: pos for color, pos in zip(
        COLORS, create_pattern(dist*5 + dist//4, dist))}
    goal_fields = {color: pos for color, pos in zip(
        COLORS, create_pattern(dist*4 + dist//4, 0))}
    hdg = 270
    for color in COLORS:
        fillcolor(color)
        seth(hdg)
        hdg -= 90

        # home fields
        goto(home_fields[color])
        for i in range(2):
            if i == 1:
                left(90)
                forward((dist//4 + dist//8)*2 + 10)
                right(90)
                back((dist//4 + dist//8)*2 + 10)
            pendown()
            begin_fill()
            circle(dist//4 + dist//8)
            end_fill()
            penup()
            forward((dist//4 + dist//8)*2 + 10)
            pendown()
            begin_fill()
            circle(dist//4 + dist//8)
            end_fill()
            penup()

        # start field
        goto(start_fields[color])
        pendown()
        begin_fill()
        circle(dist//4)
        end_fill()
        penup()

        # goal fields
        goto(goal_fields[color])
        for _ in range(4):
            pendown()
            begin_fill()
            circle(dist//4)
            end_fill()
            penup()
            left(90)
            forward(dist)
            right(90)

    school = 'Blackadder ITC'
    home = 'AR DECODE'
    off = 0
    for idx, (word, pos) in enumerate(zip(('Mensch', 'ärgere', 'nicht', 'dich'),
                                          create_pattern(dist*2 + dist//2))):
        if idx == 2:
            off = dist//4
        goto(pos[0], pos[1] - off)
        write(word, move=False, align='center', font=(
            school, dist//2 + dist//8, 'normal'))
    hideturtle()


def draw_winner_on_board(color: str):
    """Draws winner on the game board

    Args:
        color (str): the color that won
    """
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


def VERTICES_FOR_LEFT_TURN(size: str) -> tuple[tuple[float, float]]:
    """Vertex positions where a game piece has to turn left

    Args:
        size (str): small, medium or large

    Returns:
        tuple[tuple[float, float]]: vertices for left turn
    """
    dist = SIZES[size]
    return create_pattern(dist)
# VERTICES_FOR_LEFT_TURN = create_pattern(STEP_SIZE)


def VERTICES_FOR_RIGHT_TURN(size: str) -> tuple[tuple[float, float]]:
    """Vertex positions where a game piece has to turn right

    Args:
        size (str): small, medium or large

    Returns:
        tuple[tuple[float, float]]: vertices for right turn
    """
    dist = SIZES[size]
    return (create_pattern(dist, dist*5) + create_pattern(dist*5, dist))
# VERTICES_FOR_RIGHT_TURN = (create_pattern(STEP_SIZE, STEP_SIZE*5)
#                            + create_pattern(STEP_SIZE*5, STEP_SIZE))


def STARTING_VERTICES(size: str) -> dict[str, tuple[float, float]]:
    """Vertex position accessed by color where a game piece starts

    Args:
        size (str): small, medium or large

    Returns:
        dict[str, tuple[float, float]]: vertices for starting point
    """
    dist = SIZES[size]
    return {color: pos
            for color, pos
            in zip(COLORS, create_pattern(dist*5, dist))}
# STARTING_VERTICES = {color: pos
#                      for color, pos
#                      in zip(COLORS, create_pattern(STEP_SIZE*5, STEP_SIZE))}


def VERTEX_FORE_GOAL(size: str) -> dict[str, tuple[float, float]]:
    """Vertex position accessed by color infront of the goal positon,
    so a game piece doesn't travel in an endless loop on the game board

    Args:
        size (str): small, medium or large

    Returns:
        dict[str, tuple[float, float]]: the vertices infront of the goal pos
    """
    dist = SIZES[size]
    return {color: pos
            for color, pos
            in zip(COLORS, create_pattern(dist*5, 0))}
# VERTEX_FORE_GOAL = {color: pos
#                     for color, pos
#                     in zip(COLORS, create_pattern(STEP_SIZE*5, 0))}


def TWO_VERTICES_FORE_GOAL(size: str) -> dict[str,
                                              tuple[tuple[float, float],
                                                    tuple[float, float]]]:
    """Vertex positions accessed by color that are two steps infront of the goal.
    Used to ensure that there are enough vertices a game piece can travel

    Args:
        size (str): small, medium or large

    Returns:
        dict[str,
             tuple[tuple[float, float],
                   tuple[float, float]]]: vertices two steps infront of goal pos
    """
    dist = SIZES[size]
    rev_evpc = list(reversed(create_pattern(dist*5, dist, mutable=True)))
    for idx, val in enumerate(rev_evpc):
        rev_evpc[idx][0], rev_evpc[idx][1] = rev_evpc[idx][1], rev_evpc[idx][0]
    swapped_evpc = tuple(rev_evpc)
    return {color: (one_fore_goal, two_fore_goal)
            for color, one_fore_goal, two_fore_goal
            in zip(COLORS,
                   create_pattern(dist*5, 0),
                   swapped_evpc)}
# rev_evpc = list(reversed(create_pattern(STEP_SIZE*5, STEP_SIZE, mutable=True)))
# for idx, val in enumerate(rev_evpc):
#     rev_evpc[idx][0], rev_evpc[idx][1] = rev_evpc[idx][1], rev_evpc[idx][0]
# swapped_evpc = tuple(rev_evpc)
# TWO_VERTICES_FORE_GOAL = {color: (one_fore_goal, two_fore_goal)
#                           for color, one_fore_goal, two_fore_goal
#                           in zip(COLORS,
#                                  create_pattern(STEP_SIZE*5, 0),
#                                  swapped_evpc)}


def GOAL_POSITIONS(size: str) -> dict[str,
                                      tuple[tuple[float, float],
                                            tuple[float, float],
                                            tuple[float, float],
                                            tuple[float, float]]]:
    """Vertex goal positions accessed by color

    Args:
        size (str): small, medium or large

    Returns:
        dict[str,
             tuple[tuple[float, float],
                   tuple[float, float],
                   tuple[float, float],
                   tuple[float, float]]]: goal pos
    """
    dist = SIZES[size]
    return {color: (inner, second, third, outer)
            for color, inner, second, third, outer
            in zip(COLORS,
                   create_pattern(dist, 0),
                   create_pattern(dist*2, 0),
                   create_pattern(dist*3, 0),
                   create_pattern(dist*4, 0))}
# GOAL_POSITIONS = {color: (inner, second, third, outer)
#                   for color, inner, second, third, outer
#                   in zip(COLORS,
#                          create_pattern(STEP_SIZE, 0),
#                          create_pattern(STEP_SIZE*2, 0),
#                          create_pattern(STEP_SIZE*3, 0),
#                          create_pattern(STEP_SIZE*4, 0))}


def HOME_POSITIONS(size: str) -> dict[str,
                                      tuple[tuple[float, float],
                                            tuple[float, float],
                                            tuple[float, float],
                                            tuple[float, float]]]:
    """Vertex home positions accessed by color

    Args:
        size (str): small, medium or large

    Returns:
        dict[str,
             tuple[tuple[float, float],
                   tuple[float, float],
                   tuple[float, float],
                   tuple[float, float]]]: vertices for home pos
    """
    dist = SIZES[size]
    return {color: (fir, sec, thi, fou)
            for color, fir, sec, thi, fou
            in zip(COLORS,
                   create_pattern(dist*5 - dist//8),
                   create_pattern(dist*4, dist*5 - dist//8),
                   create_pattern(dist*5 - dist//8, dist*4),
                   create_pattern(dist*4))}
# HOME_POSITIONS = {color: (fir, sec, thi, fou)
#                   for color, fir, sec, thi, fou
#                   in zip(COLORS,
#                   create_pattern(STEP_SIZE*5 - STEP_SIZE//8),
#                   create_pattern(STEP_SIZE*4, STEP_SIZE*5 - STEP_SIZE//8),
#                   create_pattern(STEP_SIZE*5 - STEP_SIZE//8, STEP_SIZE*4),
#                   create_pattern(STEP_SIZE*4))}


def main():
    """For testing and debugging purposes"""
    print(HOME_POSITIONS("small"))
    game_board("large")
    for color in COLORS:
        draw_winner_on_board(color)
    exitonclick()


if __name__ == "__main__":
    main()
