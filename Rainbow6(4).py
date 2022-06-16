import turtle
t=turtle.Turtle()
t.pensize(30)

clr=['red','orange','yellow','green','blue','navyBlue','violet']
def rainbow(x,clr,R):
    t.up()
    t.setheading(90)
    t.goto(x,180)
    t.down()
    t.color(clr)
    t.circle(R,180)
rainbow(0,'red',200)
rainbow(-25,'orange',175)
rainbow(-50,'yellow',150)
rainbow(-75,'green',125)
rainbow(-100,'blue',100)
rainbow(-125,'navyblue',75)
rainbow(-150,'violet',50)

