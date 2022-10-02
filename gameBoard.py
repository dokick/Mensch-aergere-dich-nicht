from turtle import exitonclick, hideturtle, shape, speed, fillcolor, pencolor, width, penup, pendown, goto, begin_fill, end_fill, seth, circle, left, right, forward, back, write

STEP_SIZE: int = 80

COLORS: tuple[str] = ("yellow", "green", "red", "black")
GAME_PIECE_COLORS: dict[str, tuple[int]] = {"yellow": (255, 215, 0),
                                            "green": (15, 200, 11),
                                            "red": (176, 0, 0),
                                            "black": (64, 64, 64)}
"""Order of colors beginning in the top left corner and then going clockwise: yellow, green, red, black"""

vertices: tuple[tuple[float]] = ((-80.00, 80.00), (-80.00, 400.00), (80.00, 400.00),
                                 (80.00, 80.00), (400.00, 80.00), (400.00, -80.00),
                                 (80.00, -80.00), (80.00, -400.00), (-80.00, -400.00),
                                 (-80.00, -80.00), (-400.00, -80.00), (-400.00, 80.00))
"""Vertex positions where a game piece has to turn"""

vertices_for_left_turn: tuple[tuple[float]] = ((-80.00, 80.00), (80.00, 80.00),
                                               (80.00, -80.00), (-80.00, -80.00))
"""Vertex positions where a game piece has to turn left"""

vertices_for_right_turn: tuple[tuple[float]] = ((-80.00, 400.00), (80.00, 400.00), (400.00, 80.00), (400.00, -80.00),
                                                (80.00, -400.00), (-80.00, -400.00), (-400.00, -80.00), (-400.00, 80.00))
"""Vertex positions where a game piece has to turn right"""

starting_vertices: dict[str, tuple[float]] = {"yellow": (-400.00, 80.00),
                                              "green": (80.00, 400.00),
                                              "red": (400.00, -80.00),
                                              "black": (-80.00, -400.00)}
"""Vertex position accessed by color where a game piece starts"""

turning_vertices_per_color: dict[str, tuple[float]] = {"yellow": (-400.00, 0.00),
                                                       "green": (0.00, 400.00),
                                                       "red": (400.00, 0.00),
                                                       "black": (0.00, -400.00)}
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
# yellow_goal_fields = tuple([(-STEP_SIZE*(i+1), 0) for i in range(4)])
# green_goal_fields = tuple([(0, STEP_SIZE*(i+1)) for i in range(4)])
# red_goal_fields = tuple([(0, -STEP_SIZE*(i+1)) for i in range(4)])
# black_goal_fields = tuple([(STEP_SIZE*(i+1), 0) for i in range(4)])
# goal_positions = {color: pos for color, pos in zip(COLORS, (yellow_goal_fields, green_goal_fields, red_goal_fields, black_goal_fields))}
"""Vertex goal positions accessed by color"""

home_positions: dict[str, tuple[tuple[float]]] = {"yellow": ((-390.00, 390.00), (-320.00, 390.00), (-390.00, 320.00), (-320.00, 320.00)),
                                                  "green": ((320.00, 390), (390.00, 390.00), (320.00, 320.00), (390.00, 320.00)),
                                                  "red": ((320.00, -320.00), (390.00, -320.00), (320.00, -390.00), (390.00, -390.00)),
                                                  "black": ((-390.00, -320.00), (-320.00, -320.00), (-390.00, -390.00), (-320.00, -390.00))}
"""Vertex home positions accessed by color"""

HOME_ANGLES: dict[str, int] = {"yellow": 90,
                               "green": 0,
                               "red": 270,
                               "black": 180}
"""Angles accessed by color so at the beginning game pieces look in the right direction (easier setup)"""


# TODO: Make game board resizeable and dependent of desired size
def game_board() -> None:
    """Draws a game board"""

    shape('turtle')
    speed(0)
    fillcolor('#fdeb95')
    pencolor('red')
    width(20)
    penup()
    goto(-450, -450)
    pendown()
    begin_fill()
    goto(-450, 450)
    goto(450, 450)
    goto(450, -450)
    goto(-450, -450)
    end_fill()
    pencolor('black')
    width(4)
    penup()
    goto(-430, -430)
    pendown()
    goto(-430, 430)
    goto(430, 430)
    goto(430, -430)
    goto(-430, -430)
    penup()
    goto(-420, 80)
    seth(270)
    fillcolor('white')
    for i in range(4):
        for j in range(2):
            for k in range(4):
                pendown()
                begin_fill()
                circle(20)
                end_fill()
                left(90)
                penup()
                forward(40)
                pendown()
                forward(40)
                right(90)
            penup()
            forward(20)
            left(90)
            forward(20)
        right(90)
        back(40)
        right(90)
        for l in range(2):
            pendown()
            begin_fill()
            circle(20)
            end_fill()
            left(90)
            penup()
            forward(40)
            pendown()
            forward(40)
            right(90)
        penup()
        back(20)
        right(90)
        back(20)
        penup()
    penup()
    seth(0)
    fillcolor('black')
    y = -350
    for blau in range(2):
        goto(-390, y)
        pendown()
        begin_fill()
        circle(30)
        end_fill()
        penup()
        forward(70)
        pendown()
        begin_fill()
        circle(30)
        end_fill()
        penup()
        y = y-70
    goto(-80, -420)
    pendown()
    begin_fill()
    circle(20)
    end_fill()
    penup()
    y = -340
    for ziel_blau in range(4):
        goto(0, y)
        pendown()
        begin_fill()
        circle(20)
        end_fill()
        penup()
        y = y+80
    fillcolor('yellow')
    y = 360
    for gelb in range(2):
        goto(-390, y)
        pendown()
        begin_fill()
        circle(30)
        end_fill()
        penup()
        forward(70)
        pendown()
        begin_fill()
        circle(30)
        end_fill()
        penup()
        y = y-70
    goto(-400, 60)
    pendown()
    begin_fill()
    circle(20)
    end_fill()
    penup()
    x = -320
    for ziel_gelb in range(4):
        goto(x, -20)
        pendown()
        begin_fill()
        circle(20)
        end_fill()
        penup()
        x = x+80
    fillcolor('green')
    y = 360
    for gruen in range(2):
        goto(320, y)
        pendown()
        begin_fill()
        circle(30)
        end_fill()
        penup()
        forward(70)
        pendown()
        begin_fill()
        circle(30)
        end_fill()
        penup()
        y = y-70
    goto(80, 380)
    pendown()
    begin_fill()
    circle(20)
    end_fill()
    penup()
    y = 300
    for ziel_gruen in range(4):
        goto(0, y)
        pendown()
        begin_fill()
        circle(20)
        end_fill()
        penup()
        y = y-80
    fillcolor('red')
    y = -350
    for rot in range(2):
        goto(320, y)
        pendown()
        begin_fill()
        circle(30)
        end_fill()
        penup()
        forward(70)
        pendown()
        begin_fill()
        circle(30)
        end_fill()
        penup()
        y = y-70
    goto(400, -100)
    pendown()
    begin_fill()
    circle(20)
    end_fill()
    penup()
    x = 320
    for ziel_rot in range(4):
        goto(x, -20)
        pendown()
        begin_fill()
        circle(20)
        end_fill()
        penup()
        x = x-80
    school = 'Blackadder ITC'
    home = 'AR DECODE'
    goto(-210, 210)
    write('Mensch', move=False, align='center', font=(school, 50, 'normal'))
    goto(210, 210)
    write('ärgere', move=False, align='center', font=(school, 50, 'normal'))
    goto(-210, -280)
    write('dich', move=False, align='center', font=(school, 50, 'normal'))
    goto(210, -280)
    write('nicht', move=False, align='center', font=(school, 50, 'normal'))
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


def main():
    """For testing and debugging purposes"""
    game_board()
    for color in COLORS:
        draw_winner_on_board(color)
    exitonclick()


if __name__ == "__main__":
    main()
