import turtle
t1=turtle.Turtle()
wn=turtle.Screen()
import time
turtle.bgcolor('black')
s=turtle.Shape('compound')
turtle.hideturtle()
turtle.up()
turtle.tracer(5)
poly1=[(60,-20),(20,40),(-40,60),(-40,-20),(-20,-80),(40,-80),(60,-20)]
    
s.addcomponent(poly1,'blue')    
wn.addshape('POLY',s)
t= turtle.Turtle(shape = 'POLY')

t.showturtle()
t.tilt(90)
t.color('black')
t.penup()

t1.pensize(3)
t1.color('white')
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
t2=turtle.Turtle()
t2.hideturtle()
t2.color('white')
Text_font=('times New Roman', 15,'bold')
t2.up()
for n in range(4):
    t2.up()
    t2.goto(0,0)
    t2.setheading(90*n)
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
t2.write('Draw Polygon using begin_poly',font=('times New Roman',25,'bold')) 
