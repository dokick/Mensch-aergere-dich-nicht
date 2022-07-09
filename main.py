from turtle import Turtle, shape, speed, fillcolor, pencolor, width, pu, goto, pd, begin_fill, end_fill, seth, circle, lt, fd, rt, bk, write, exitonclick
import random

def gameBoard():
    shape('turtle')
    speed('fastest')
    fillcolor('#fdeb95')
    pencolor('red')
    width(20)
    pu()
    goto(-450,-450)
    pd()
    begin_fill()
    goto(-450,450)
    goto(450,450)
    goto(450,-450)
    goto(-450,-450)
    end_fill()
    pencolor('black')
    width(4)
    pu()
    goto(-430,-430)
    pd()
    goto(-430,430)
    goto(430,430)
    goto(430,-430)
    goto(-430,-430)
    pu()
    goto(-420,80)
    seth(270)
    fillcolor('white')
    for i in range(4):
        for j in range(2):
            for k in range(4):
                pd()
                begin_fill()
                circle(20)
                end_fill()
                lt(90)
                pu()
                fd(40)
                pd()
                fd(40)
                rt(90)
            pu()
            fd(20)
            lt(90)
            fd(20)
        rt(90)
        bk(40)
        rt(90)
        for l in range(2):
            pd()
            begin_fill()
            circle(20)
            end_fill()
            lt(90)
            pu()
            fd(40)
            pd()
            fd(40)
            rt(90)
        pu()
        bk(20)
        rt(90)
        bk(20)
        pd()
    pu()
    seth(0)
    fillcolor('blue')
    y=-350
    for blau in range(2):
        goto(-390,y)
        pd()
        begin_fill()
        circle(30)
        end_fill()
        pu()
        fd(70)
        pd()
        begin_fill()
        circle(30)
        end_fill()
        pu()
        y=y-70
    goto(-80,-420)
    pd()
    begin_fill()
    circle(20)
    end_fill()
    pu()
    y=-340
    for ziel_blau in range(4):
        goto(0,y)
        pd()
        begin_fill()
        circle(20)
        end_fill()
        pu()
        y=y+80
    fillcolor('yellow')
    y=360
    for gelb in range(2):
        goto(-390,y)
        pd()
        begin_fill()
        circle(30)
        end_fill()
        pu()
        fd(70)
        pd()
        begin_fill()
        circle(30)
        end_fill()
        pu()
        y=y-70
    goto(-400,60)
    pd()
    begin_fill()
    circle(20)
    end_fill()
    pu()
    x=-320
    for ziel_gelb in range(4):
        goto(x,-20)
        pd()
        begin_fill()
        circle(20)
        end_fill()
        pu()
        x=x+80
    fillcolor('green')
    y=360
    for gruen in range(2):
        goto(320,y)
        pd()
        begin_fill()
        circle(30)
        end_fill()
        pu()
        fd(70)
        pd()
        begin_fill()
        circle(30)
        end_fill()
        pu()
        y=y-70
    goto(80,380)
    pd()
    begin_fill()
    circle(20)
    end_fill()
    pu()
    y=300
    for ziel_gruen in range(4):
        goto(0,y)
        pd()
        begin_fill()
        circle(20)
        end_fill()
        pu()
        y=y-80
    fillcolor('red')
    y=-350
    for rot in range(2):
        goto(320,y)
        pd()
        begin_fill()
        circle(30)
        end_fill()
        pu()
        fd(70)
        pd()
        begin_fill()
        circle(30)
        end_fill()
        pu()
        y=y-70
    goto(400,-100)
    pd()
    begin_fill()
    circle(20)
    end_fill()
    pu()
    x=320
    for ziel_rot in range(4):
        goto(x,-20)
        pd()
        begin_fill()
        circle(20)
        end_fill()
        pu()
        x=x-80
    school='Blackadder ITC'
    home='AR DECODE'
    goto(-210,210)
    write('Mensch',move=False,align='center',font=(home,50,'normal'))
    goto(210,210)
    write('ärgere',move=False,align='center',font=(home,50,'normal'))
    goto(-210,-280)
    write('dich',move=False,align='center',font=(home,50,'normal'))
    goto(210,-280)
    write('nicht',move=False,align='center',font=(home,50,'normal'))

blue=list(range(4))
yellow=list(range(4))
green=list(range(4))
red=list(range(4))
for colors in [blue,yellow,green,red]:
    for i in range(4):
        colors[i]=Turtle()
        colors[i].speed('fastest')
        colors[i].pu()
        #colors[i].ht()
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

#beginner_positions
blue[0].goto(-390,-320)
blue[1].goto(-320,-320)
blue[2].goto(-390,-390)
blue[3].goto(-320,-390)
yellow[0].goto(-390,390)
yellow[1].goto(-320,390)
yellow[2].goto(-390,320)
yellow[3].goto(-320,320)
green[0].goto(320,390)
green[1].goto(390,390)
green[2].goto(320,320)
green[3].goto(390,320)
red[0].goto(320,-320)
red[1].goto(390,-320)
red[2].goto(320,-390)
red[3].goto(390,-390)

#vertices(eckpunkte)
#beginning by blue
pos1=(-80,-400)
pos2=(-80.00,-80.00)
pos3=(-400,-80)
pos4=(-400,80)
pos5=(-80,80)
pos6=(-80,400)
pos7=(80,400)
pos8=(80,80)
pos9=(400,80)
pos10=(400,-80)
pos11=(80,-80)
pos12=(80,-400)

def dice():
    x=random.randint(1,6)
    print(x)
    return 6

def permission():
    results=[]
    for i in range(3):
        results.append(dice())
    print(results)
    if 6 in results:
        return True
    return False
#---------------------------Work----------------------------
def start(color,n,figure_color):
    if permission():
        if figure_color=='blue':
            color[n].goto(pos1)
        if figure_color=='yellow':
            color[n].goto(pos4)
        if figure_color=='green':
            color[n].goto(pos7)
        if figure_color=='red':
            color[n].goto(pos10)
        return True
    return False

def move(color,n):
    came_out=True
    #blue
    if color[n].pos()==(-390,-320) or color[n].pos()==(-320,-320) or color[n].pos()==(-390,-390) or color[n].pos()==(-320,-390):
        came_out=start(color,n,'blue')
    #yellow
    if color[n].pos()==(-390,390) or color[n].pos()==(-320,390) or color[n].pos()==(-390,320) or color[n].pos()==(-320,320):
        came_out=start(color,n,'yellow')
    #green
    if color[n].pos()==(320,390) or color[n].pos()==(390,390) or color[n].pos()==(320,320) or color[n].pos()==(390,320):
        came_out=start(color,n,'green')
    #red
    if color[n].pos()==(320,-320) or color[n].pos()==(390,-320) or color[n].pos()==(320,-390) or color[n].pos()==(390,-390):
        came_out=start(color,n,'red')
    if came_out:
        for i in range(dice()):
            print('Aktuell:',color[n].pos())
            print('Pos2:',pos2)
            print(color[n].pos()==pos2)
            print('Pos1:',pos1)
            print(color[n].pos()==pos1)
            if color[n].pos()==pos2 or color[n].pos()==pos5 or color[n].pos()==pos8 or color[n].pos()==pos11:
                color[n].lt(90)
            if color[n].pos()==pos1 or color[n].pos()==pos3 or color[n].pos()==pos4 or color[n].pos()==pos6 or color[n].pos()==pos7 or color[n].pos()==pos9 or color[n].pos()==pos10 or color[n].pos()==pos12:
                color[n].rt(90)
            color[n].fd(80)
#---------------------------Work----------------------------
def main():
    gameBoard()
    exitonclick()
    return
    nB=0
    nY=0
    nG=0
    nR=0
    colors=('blue','yellow','green','red')
    #current_player=random.choice(colors)
    current_player='blue'
    print(current_player)
    while True:
        if current_player=='blue':
            move(blue,nB)
            break
            current_player='yellow'
        if current_player=='yellow':
            move(yellow,nY)
            current_player='green'
        if current_player=='green':
            move(green,nG)
            current_player='red'
        if current_player=='red':
            move(red,nR)
            current_player='blue'
if __name__ == "__main__":
    main()