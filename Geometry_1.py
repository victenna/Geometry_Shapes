import	turtle
import random
import time
wn=turtle.Screen()
turtle.tracer(2)
t1=turtle.Turtle()
t1.hideturtle()
t1.color('white')
t1.goto(0,0)
t1.pensize(2)
t2=turtle.Turtle()
t2.hideturtle()
t2.color('white')
turtle.bgcolor('black')

Text_font=('times New Roman', 15,'bold')
t2.up()
t3=turtle.Turtle()
t3.hideturtle()
t3.pensize(5)
t3.up()
t3.color('gold')
coord=[(60,-20),(20,40),(-40,60),(-40,-20),(-20,-80),(40,-80),(60,-20)]
Q=4
t3.up()
t3.goto(0,0)
    
t3.up()
t3.goto(coord[0])
t3.down()
t1.hideturtle()
t2.hideturtle()
t3.hideturtle()
for i in range (len(coord)):
    t3.left(0)
    t3.goto(coord[i])

for n in range(Q):
    t2.up()
    t2.goto(0,0)
    t2.setheading(360/Q*n)
    t2.fd(200)
    t2.down()
    t2.write('100',font=Text_font)
    t2.fd(40)
    if n==0:
        t2.write('X',font=Text_font)
    if n==1:
        t2.write('Y',font=Text_font)
    

t2.up()
t2.goto(-200,300)
t2.down()
t2.write('Draw Polygon using Lists',font=('times New Roman',25,'bold')) 

t1.pensize(3)
t1.hideturtle()
t1.pendown()
t1.goto(-350,0)
t1.fd(700)
t1.up()
t1.goto(0,-350)
t1.setheading(90)
t1.down()
t1.fd(650)
t1.pensize(1)
t1.up()
t1.goto(0,0)
t1.setheading(0)
t1.down()
for j in range (-11,12):
    t1.penup()
    t1.goto(-220,20*j)
    t1.goto(220,20*j)
    t1.penup()
    t1.goto(-220,20*j)
    t1.pendown()
    t1.goto(220,20*j)

for i in range (-11,12):
    t1.penup()
    t1.goto(20*i,-220)
    t1.goto(20*i,220)
    t1.penup()
    t1.goto(20*i,-220)
    t1.pendown()
    t1.goto(20*i,220)
