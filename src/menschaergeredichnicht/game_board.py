"""
This module draws the game board
and generates all necessary position coordinates inside of dicts or tuples

Functions:
    clockwise_pattern(x: float, y: Optional[float] = None) -> tuple[tuple[float, float],
                                                                 tuple[float, float],
                                                                 tuple[float, float],
                                                                 tuple[float, float]]
    clockwise_pattern_as_list(x: float, y: Optional[float] = None) -> list[list[float]]
    game_board(size: str = "medium") -> None
    draw_winner_on_board(color: str)
    has_to_turn_left(x: float, y: float, /, size: str) -> bool
    has_to_turn_right(x: float, y: float, /, size: str, color: str) -> bool
    starting_vertices(size: str) -> dict[str, tuple[float, float]]
    vertex_fore_goal(size: str) -> dict[str, tuple[float, float]]
    two_vertices_fore_goal(size: str) -> dict[str,
                                              tuple[tuple[float, float],
                                                    tuple[float, float]]]
    goal_positions(size: str) -> dict[str,
                                      tuple[tuple[float, float],
                                            tuple[float, float],
                                            tuple[float, float],
                                            tuple[float, float]]]
    get_goal_factors(color: str) -> tuple[float, float]
    home_positions(size: str) -> dict[str,
                                      tuple[tuple[float, float],
                                            tuple[float, float],
                                            tuple[float, float],
                                            tuple[float, float]]]
"""

from turtle import (back, begin_fill, circle, end_fill, exitonclick, fillcolor,
                    forward, goto, hideturtle, left, pencolor, pendown,
                    pensize, penup, right, seth, shape, speed, write)
from typing import Optional

SIZES: dict[str, int] = {"x-small": 48,
                         "small": 64,
                         "medium": 80,
                         "large": 96,
                         "x-large": 112}
"""Distance between two fields, should be divisible by 8"""

COLORS = ("yellow", "green", "red", "black")
"""Order of colors beginning in the top left corner and then going clockwise:
yellow, green, red, black"""
GAME_PIECE_COLORS: dict[str, tuple[int, int, int]] = dict(zip(COLORS, ((255, 215, 0),
                                                                       (15, 200, 11),
                                                                       (176, 0, 0),
                                                                       (64, 64, 64))))

HOME_ANGLES = dict(zip(COLORS, (90, 0, 270, 180)))
"""Angles accessed by color so at the beginning game pieces
look in the right direction (easier setup)"""

MATRIX: tuple[tuple[int, int],
              tuple[int, int],
              tuple[int, int],
              tuple[int, int]] = ((-1, 1), (1, 1), (1, -1), (-1, -1))


def clockwise_pattern(x: float, y: Optional[float] = None, /) -> tuple[tuple[float, float],
                                                                       tuple[float, float],
                                                                       tuple[float, float],
                                                                       tuple[float, float]]:
    """Creates tuple with the following pattern
    ((-x, y), (y, x), (x, -y), (-y, -x))

    Args:
        x (float): first number
        y (Optional[float], optional): second number. Defaults to None.

    Returns:
        tuple[tuple[float, float],
              tuple[float, float],
              tuple[float, float],
              tuple[float, float]]: number pattern
    """
    if y is None:
        y = x

    tmp = []
    for i, j in MATRIX:
        tmp.append((i*x, j*y))
        x, y = y, x
    return tuple(tmp)


def clockwise_pattern_as_list(x: float, y: Optional[float] = None, /) -> list[list[float]]:
    """Creates list with the following pattern
    [[-x, y], [y, x], [x, -y], [-y, -x]]

    Args:
        x (float): first number
        y (Optional[float], optional): second number. Defaults to None.

    Returns:
        list[list[float]]: number pattern
    """
    if y is None:
        y = x

    tmp = []
    for i, j in MATRIX:
        tmp.append([i*x, j*y])
        x, y = y, x
    return tmp


def game_board(size: str = "medium") -> None:
    """Draws a game board

    Args:
        size (str, optional): size of game board. look into SIZES for sizes. Defaults to "medium".
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

    shape("turtle")
    speed(0)

    # background
    fillcolor("#fdeb95")
    pencolor("red")
    pen_width = 20
    pensize(pen_width)
    penup()
    outer_outline = dist*5 + dist//4 + 10 + 10 + pen_width//2
    goto(-outer_outline, -outer_outline)
    pendown()
    begin_fill()
    for pos in clockwise_pattern(outer_outline):
        goto(pos)
    end_fill()
    pencolor("black")
    pensize(4)
    penup()
    inner_outline = dist*5 + dist//4 + 10
    goto(-inner_outline, -inner_outline)
    pendown()
    for pos in clockwise_pattern(inner_outline):
        goto(pos)
    penup()

    # game fields
    goto(-(dist*5 + dist//4), dist)
    seth(270)
    fillcolor("white")
    for i in range(4):
        for _ in range(2):
            pendown()
            for __ in range(4):
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
    home_fields = dict(zip(COLORS, clockwise_pattern(dist*5 + dist//4, dist*5 - dist//8)))
    start_fields = dict(zip(COLORS, clockwise_pattern(dist*5 + dist//4, dist)))
    goal_fields = dict(zip(COLORS, clockwise_pattern(dist*4 + dist//4, 0)))
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

    school = "Blackadder ITC"
    # home = "AR DECODE"
    off = 0
    for idx, (word, pos) in enumerate(zip(("Mensch", "ärgere", "nicht", "dich"),
                                          clockwise_pattern(dist*2 + dist//2))):
        if idx == 2:
            off = dist//4
        goto(pos[0], pos[1] - off)
        write(word, move=False, align="center", font=(
            school, dist//2 + dist//8, "normal"))
    hideturtle()


def draw_winner_on_board(color: str):
    """Draws winner on the game board

    Args:
        color (str): color that won
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


def has_to_turn_left(x: float, y: float, /, size: str) -> bool:
    """Checks if game piece has to turn left

    Args:
        x (float): x pos
        y (float): y pos
        size (str): size of game board. look into SIZES for sizes

    Returns:
        bool: true if game piece has to turn left on vertex (x, y)
    """
    dist = SIZES[size]
    return abs(x) == dist and abs(y) == dist


def has_to_turn_right(x: float, y: float, /, size: str, color: str) -> bool:
    """Checks if game piece has to turn right

    Args:
        x (float): x pos
        y (float): y pos
        size (str): size of game board. look into SIZES for sizes
        color (str): color of game piece

    Returns:
        bool: true if game piece has to turn right on vertex (x, y)
    """
    dist = SIZES[size]
    color_factors_dict = dict(zip(COLORS, clockwise_pattern(5, 0)))
    factor_x, factor_y = color_factors_dict[color]
    return ((abs(x) == dist * 5 and abs(y) == dist)
            or (abs(x) == dist and abs(y) == dist * 5)
            or (x == factor_x*dist and y == factor_y*dist))


def starting_vertices(size: str) -> dict[str, tuple[float, float]]:
    """Vertex position accessed by color where a game piece starts

    Args:
        size (str): size of game board. look into SIZES for sizes

    Returns:
        dict[str, tuple[float, float]]: vertices for starting point
    """
    dist = SIZES[size]
    return dict(zip(COLORS, clockwise_pattern(dist*5, dist)))


def vertex_fore_goal(size: str) -> dict[str, tuple[float, float]]:
    """Vertex position accessed by color infront of the goal positon,
    so a game piece doesn't travel in an endless loop on the game board

    Args:
        size (str): size of game board. look into SIZES for sizes

    Returns:
        dict[str, tuple[float, float]]: vertex infront of goal pos
    """
    dist = SIZES[size]
    return dict(zip(COLORS, clockwise_pattern(dist*5, 0)))


def two_vertices_fore_goal(
    size: str) -> dict[str, tuple[tuple[float, float], tuple[float, float]]]:
    """Vertex positions accessed by color that are two steps infront of the goal.
    Used to ensure that there are enough vertices a game piece can travel

    Args:
        size (str): size of game board. look into SIZES for sizes

    Returns:
        dict[str,
             tuple[tuple[float, float],
                   tuple[float, float]]]: vertices two steps infront of goal pos
    """
    dist = SIZES[size]
    rev_vert_4_goal = list(reversed(clockwise_pattern_as_list(dist*5, dist)))
    for idx, pos in enumerate(rev_vert_4_goal):
        pos[0], pos[1] = pos[1], pos[0]
        rev_vert_4_goal[idx] = tuple(rev_vert_4_goal[idx])

    swapped_vert_fore_goal: tuple[tuple[float, float],
                                  tuple[float, float],
                                  tuple[float, float],
                                  tuple[float, float]] = tuple(rev_vert_4_goal)
    return {color: (one_fore_goal, two_fore_goal)
            for color, one_fore_goal, two_fore_goal
            in zip(COLORS,
                   clockwise_pattern(dist*5, 0),
                   swapped_vert_fore_goal)}


def goal_positions(
    size: str) -> dict[str, tuple[tuple[float, float],
                                  tuple[float, float],
                                  tuple[float, float],
                                  tuple[float, float]]]:
    """Vertex goal positions accessed by color

    Order's inside out

    Args:
        size (str): size of game board. look into SIZES for sizes

    Returns:
        dict[str,
             tuple[tuple[float, float],
                   tuple[float, float],
                   tuple[float, float],
                   tuple[float, float]]]: goal pos
    """
    dist = SIZES[size]
    return {color: tuple((factor_x*i*dist, factor_y*i*dist)
                         for i in range(1, 5))
            for color, (factor_x, factor_y)
            in zip(COLORS, clockwise_pattern(1, 0))}
    # return {color: (inner, second, third, outer)
    #         for color, inner, second, third, outer
    #         in zip(COLORS,
    #                clockwise_pattern(dist, 0),
    #                clockwise_pattern(dist*2, 0),
    #                clockwise_pattern(dist*3, 0),
    #                clockwise_pattern(dist*4, 0))}


def get_goal_factors(color: str) -> tuple[float, float]:
    """Goal factors for calculating the goal pos

    Args:
        color (str): color of game piece

    Returns:
        tuple[float, float]: factors
    """
    return dict(zip(COLORS, clockwise_pattern(1, 0)))[color]


def home_positions(size: str) -> dict[str,
                                      tuple[tuple[float, float],
                                            tuple[float, float],
                                            tuple[float, float],
                                            tuple[float, float]]]:
    """Vertex home positions accessed by color

    Args:
        size (str): size of game board. look into SIZES for sizes

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
                   clockwise_pattern(dist*5 - dist//8),
                   clockwise_pattern(dist*4, dist*5 - dist//8),
                   clockwise_pattern(dist*5 - dist//8, dist*4),
                   clockwise_pattern(dist*4))}


def main():
    """For testing and debugging purposes"""
    game_board("large")
    for color in COLORS:
        draw_winner_on_board(color)
    exitonclick()


if __name__ == "__main__":
    main()
