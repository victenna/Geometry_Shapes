import turtle
t=turtle.Turtle()
t.hideturtle()
t.pensize(1)
t.speed(10)
t.color('red')
d=200
angle=140

for i in range(1,100):

    t.fd(d)
    t.left(angle)
    d=d-1



    
