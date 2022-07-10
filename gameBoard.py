from turtle import Turtle, exitonclick, shape, speed, fillcolor, pencolor, width, penup, pendown, goto, begin_fill, end_fill, seth, circle, left, right, forward, back, write

# All x and y positions of the vertices where a game piece has to turn
vertices: tuple = ((-80, -400), (-80, -80), (-400, -80), (-400, 80), (-80, 80),
                   (-80, 400), (80, 400), (80, 80), (400, 80), (400, -80), (80, -80), (80, -400))

verticesForLeftTurn: tuple = ((-80, -80), (-80, 80), (80, 80), (80, -80))

verticesForRightTurn: tuple = ((-80, -400), (-400, -80), (-400, 80),
                               (-80, 400), (80, 400), (400, 80), (400, -80), (80, -400))

startingVertices: dict = {
    "yellow": (-400, 80), "green": (80, 400), "red": (400, -80), "black": (-80, -400)}

# All target positions per color in a dictionary
targetPositions = {"yellow": (), "green": (), "red": (), "black": ()}

# All starting positions per color in a dictionary
homePositions = {"yellow": ((-390, 390), (-320, 390), (-390, 320), (-320, 320)), "green": ((320, 390), (390, 390), (320, 320), (390, 320)),
                 "red": ((320, -320), (390, -320), (320, -390), (390, -390)), "black": ((-390, -320), (-320, -320), (-390, -390), (-320, -390))}

# Order of colors beginning in the top left corner and then going clockwise: yellow, green, red, black
colors: tuple = ("yellow", "green", "red", "black")


def gameBoard():
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
    fillcolor('blue')
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
    write('Mensch', move=False, align='center', font=(home, 50, 'normal'))
    goto(210, 210)
    write('ärgere', move=False, align='center', font=(home, 50, 'normal'))
    goto(-210, -280)
    write('dich', move=False, align='center', font=(home, 50, 'normal'))
    goto(210, -280)
    write('nicht', move=False, align='center', font=(home, 50, 'normal'))


def main():
    """For testing and debugging purposes"""
    gameBoard()


if __name__ == "__main__":
    main()
