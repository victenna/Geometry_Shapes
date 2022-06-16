import	turtle
turtle.bgcolor('lightblue')
import random
import time
turtle.tracer(2)
t1=turtle.Turtle()
t1.hideturtle()
t1.color('white')
t1.goto(0,0)

for j in range (-11,12):
    t1.pensize(1)
    if j==0:
        t1.pensize(3)
    t1.penup()
    t1.goto(-220,20*j)
    t1.goto(220,20*j)
    t1.penup()
    t1.goto(-220,20*j)
    t1.pendown()
    t1.goto(220,20*j)

for i in range (-11,12):
    t1.pensize(1)
    if i==0:
        t1.pensize(3)
    t1.penup()
    t1.goto(20*i,-220)
    t1.goto(20*i,220)
    t1.penup()
    t1.goto(20*i,-220)
    t1.pendown()
    t1.goto(20*i,220)

coord=((40,40),(120,40),(160,80),(80,160),(40,40))

turtle.addshape('poly',coord)
t3=turtle.Turtle(shape='poly')
t3.up()
t3.hideturtle()
t3.goto(0,0)
t3.showturtle()
t3.color('blue')
t3.tilt(90)

Q=4
t2=turtle.Turtle()
t2.hideturtle()
t2.color('black')
Text_font=('times New Roman', 15,'bold')
t2.up()
for n in range(Q):
    t2.up()
    t2.goto(0,0)
    t2.setheading(360/Q*n)
    t2.fd(200)
    t2.down()
    t2.write('200',font=Text_font)
    t2.fd(40)
    if n==0:
        t2.write('X',font=Text_font)
    if n==1:
        t2.write('Y',font=Text_font)
t2.up()
t2.goto(-220,-160)
t2.down()
t2.write('Polygon area, Shoelace Formula',font=('times New Roman',25,'bold'))

X=[40,120,160,80,40]
Y=[40,40,80,160,40]

Sum1=0
Sum2=0
for i in range(4):
    Sum1=Sum1+X[i]*Y[i+1]
    Sum2=Sum2+Y[i]*X[i+1]
Area=(Sum1-Sum2)/2
print(Area)
