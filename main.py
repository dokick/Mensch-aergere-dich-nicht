from turtle import Turtle, exitonclick
import random
from gameBoard import gameBoard

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