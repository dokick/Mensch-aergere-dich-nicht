from turtle import Turtle, exitonclick, hideturtle, shape, speed, fillcolor, pencolor, width, penup, pendown, goto, begin_fill, end_fill, seth, circle, left, right, forward, back, write

STEP_SIZE: int = 80

"""Order of colors beginning in the top left corner and then going clockwise: yellow, green, red, black"""
COLORS: tuple[str] = ("yellow", "green", "red", "black")
GAME_PIECE_COLORS: dict[str, tuple[int]] = {"yellow": (255, 215, 0),
                                            "green": (15, 200, 11),
                                            "red": (176, 0, 0),
                                            "black": (64, 64, 64)}

# TODO: Docs of what those data structures do, renaming those which are const
"""All x and y positions of the vertices where a game piece has to turn"""
vertices: tuple[tuple[float]] = ((-80.00, -400.00), (-80.00, -80.00), (-400.00, -80.00), (-400.00, 80.00), (-80.00, 80.00),
                                 (-80.00, 400.00), (80.00, 400.00), (80.00, 80.00), (400.00, 80.00), (400.00, -80.00), (80.00, -80.00), (80.00, -400.00))

# vertices_for_left_turn = tuple([(i*STEP_SIZE, j*STEP_SIZE) for i, j in zip((-1, -1, 1, 1), (-1, 1, 1, -1))])
vertices_for_left_turn: tuple[tuple[float]] = (
    (-80.00, -80.00), (-80.00, 80.00), (80.00, 80.00), (80.00, -80.00))

vertices_for_right_turn: tuple[tuple[float]] = ((-80.00, -400.00), (-400.00, -80.00), (-400.00, 80.00),
                                                (-80.00, 400.00), (80.00, 400.00), (400.00, 80.00), (400.00, -80.00), (80.00, -400.00))

starting_vertices: dict[str, tuple[float]] = {"yellow": (-400.00, 80.00),
                                              "green": (80.00, 400.00),
                                              "red": (400.00, -80.00),
                                              "black": (-80.00, -400.00)}

"""Coordinates of the vertices where game pieces of certain colors need to turn,
so they don't travel in an endless loop on the game board"""
# turning_vertices_per_color = {color: pos for color, pos in zip(COLORS, ((-STEP_SIZE*5, 0), (0, STEP_SIZE*5), (STEP_SIZE*5, 0), (0, -STEP_SIZE*5)))}
turning_vertices_per_color: dict[str, tuple[float]] = {"yellow": (-400.00, 0.00),
                                                       "green": (0.00, 400.00),
                                                       "red": (400.00, 0.00),
                                                       "black": (0.00, -400.00)}

enough_vertices_per_color: dict[str, tuple[tuple[float]]] = {"yellow": ((-400.00, 0.00), (-400.00, -80.00)),
                                                             "green": ((0.00, 400.00), (-80.00, 400.00)),
                                                             "red": ((400.00, 0.00), (400.00, 80.00)),
                                                             "black": ((0.00, -400.00), (80.00, -400.00))}

"""All goal positions per color in a dictionary"""
yellow_goal_fields = tuple([(-STEP_SIZE*(i+1), 0) for i in range(4)])
green_goal_fields = tuple([(0, STEP_SIZE*(i+1)) for i in range(4)])
red_goal_fields = tuple([(0, -STEP_SIZE*(i+1)) for i in range(4)])
black_goal_fields = tuple([(STEP_SIZE*(i+1), 0) for i in range(4)])
goal_positions = {color: pos for color, pos in zip(
    COLORS, (yellow_goal_fields, green_goal_fields, red_goal_fields, black_goal_fields))}

# goal_positions: dict[str, tuple[tuple[float]]] = {"yellow": ((-80.00, 0.00), (-160.00, 0.00), (-240.00, 0.00), (-320.00, 0.00)),
#                                                   "green": ((0.00, 80.00), (0.00, 160.00), (0.00, 240.00), (0.00, 320.00)),
#                                                   "red": ((80.00, 0.00), (160.00, 0.00), (240.00, 0.00), (320.00, 0.00)),
#                                                   "black": ((0.00, -80.00), (0.00, -160.00), (0.00, -240.00), (0.00, -320.00))}

"""All home positions per color in a dictionary"""
home_positions: dict[str, tuple[tuple[float]]] = {"yellow": ((-390.00, 390.00), (-320.00, 390.00), (-390.00, 320.00), (-320.00, 320.00)),
                                                  "green": ((320.00, 390), (390.00, 390.00), (320.00, 320.00), (390.00, 320.00)),
                                                  "red": ((320.00, -320.00), (390.00, -320.00), (320.00, -390.00), (390.00, -390.00)),
                                                  "black": ((-390.00, -320.00), (-320.00, -320.00), (-390.00, -390.00), (-320.00, -390.00))}

"""All starting angles for the colors so starting them and setting them up for the start of the game becomes easier"""
# HOME_ANGLES = {color: angle for color, angle in zip(COLORS, (90, 0, 270, 180))}
HOME_ANGLES: dict[str, int] = {"yellow": 90,
                               "green": 0,
                               "red": 270,
                               "black": 180}


# TODO: Make game board resizeable and dependent of desired size
def game_board() -> None:
    """Draws a game board"""

    shape('turtle')
    speed('fastest')
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
    # TODO: Draw the winner on the board with a big message
    pass


def main():
    """For testing and debugging purposes"""
    game_board()
    draw_winner_on_board("green")
    exitonclick()



if __name__ == "__main__":
    main()