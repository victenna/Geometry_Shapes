import turtle
import math as m
t=turtle.Turtle()
wn=turtle.Screen()
s=turtle.Shape('compound')
#wn.setup(700,700)
t.up()
x0,y0=0,0
t.goto(x0,y0)
t.down()
r=200
a1=int(r * m.sin(2 * m.pi / 5))
a2=int(r * m.cos(2 * m.pi / 5))
a3=int(r * m.sin(m.pi / 5))
a4=int(r * m.cos(m.pi / 5))
Poly=[(x0-a1,y0-a2),(x0+a1,y0-a2),(x0-a3,y0+a4),(x0,y0-r),(x0+a3,y0+a4)]

x1=int(r * m.cos( m.pi / 10))
y1=int(r * m.sin( m.pi / 10))
x0+x1,y0+y1

x2=int(r * m.cos( 5*m.pi / 10))
y2=int(r * m.sin(5*m.pi / 10))
x0+x2,y0+y2

x3=int(r * m.cos( 9*m.pi / 10))
y3=int(r * m.sin(9*m.pi / 10))
x0+x3,y0+y3

x4=int(r * m.cos( 13*m.pi / 10))
y4=int(r * m.sin(13*m.pi / 10))
x0+x4,y0+y4

x5=int(r * m.cos( 17*m.pi / 10))
y5=int(r * m.sin(17*m.pi / 10))
x0+x5,y0+y5

Poly=[(x0+x1,y0+y1),(x0+x2,y0+y2),(x0+x3,y0+y3),(x0+x4,y0+y4),(x0+x5,y0+y5)]

s.addcomponent(Poly,'gold')
wn.addshape('star',s)
star=turtle.Turtle(shape='star')
star.showturtle()


