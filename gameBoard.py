from turtle import Turtle, exitonclick, hideturtle, shape, speed, fillcolor, pencolor, width, penup, pendown, goto, begin_fill, end_fill, seth, circle, left, right, forward, back, write

# All x and y positions of the vertices where a game piece has to turn
vertices: tuple[tuple[int]] = ((-80, -400), (-80, -80), (-400, -80), (-400, 80), (-80, 80),
                               (-80, 400), (80, 400), (80, 80), (400, 80), (400, -80), (80, -80), (80, -400))

vertices_for_left_turn: tuple[tuple[int]] = (
    (-80, -80), (-80, 80), (80, 80), (80, -80))

vertices_for_right_turn: tuple[tuple[int]] = ((-80, -400), (-400, -80), (-400, 80),
                                              (-80, 400), (80, 400), (400, 80), (400, -80), (80, -400))

starting_vertices: dict[str, tuple[int]] = {
    "yellow": (-400, 80), "green": (80, 400), "red": (400, -80), "black": (-80, -400)}

# Coordinates of the vertices where game pieces of certain colors need to turn so they dont travel in an endless loop on the game board
turning_vertices_per_color: dict[str, tuple[int]] = {
    "yellow": (-400, 0), "green": (0, 400), "red": (400, 0), "black": (0, -400)}

# All target positions per color in a dictionary
target_positions: dict[str, tuple[tuple[int]]] = {"yellow": ((-320, 0), (-240, 0), (-160, 0), (-80, 0)), "green": (
    (0, 320), (0, 240), (0, 160), (0, 80)), "red": ((320, 0), (240, 0), (160, 0), (80, 0)), "black": ((0, -320), (0, -240), (0, -160), (0, -80))}

# All starting positions per color in a dictionary
home_positions: dict[str, tuple[tuple[int]]] = {"yellow": ((-390, 390), (-320, 390), (-390, 320), (-320, 320)), "green": ((320, 390), (390, 390), (320, 320), (390, 320)),
                                                "red": ((320, -320), (390, -320), (320, -390), (390, -390)), "black": ((-390, -320), (-320, -320), (-390, -390), (-320, -390))}

# All starting angles for the colors so starting them and setting them up for the start of the game becomes easier
home_angles: dict[str, int] = {"yellow": 90,
                               "green": 0, "red": 270, "black": 180}

# Order of colors beginning in the top left corner and then going clockwise: yellow, green, red, black
colors: tuple[str] = ("yellow", "green", "red", "black")
game_piece_colors: dict[str, tuple[int]] = {"yellow": (244, 249, 85), "green": (
    15, 200, 11), "red": (176, 0, 0), "black": (64, 64, 64)}


def game_board():
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
    write('??rgere', move=False, align='center', font=(school, 50, 'normal'))
    goto(-210, -280)
    write('dich', move=False, align='center', font=(school, 50, 'normal'))
    goto(210, -280)
    write('nicht', move=False, align='center', font=(school, 50, 'normal'))
    hideturtle()


def main():
    """For testing and debugging purposes"""
    game_board()

    exitonclick()


if __name__ == "__main__":
    main()
