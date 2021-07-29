import turtle
import random

a = turtle.Turtle()
b = turtle.Turtle()
c = turtle.Turtle()
d = turtle.Turtle()
set_lines = turtle.Turtle()

#set lines
set_lines.hideturtle()
set_lines.pu()
set_lines.rt(90)
set_lines.fd(200)
set_lines.lt(90)
set_lines.fd(200)
set_lines.lt(90)
set_lines.pd()
for i in range(9):
    set_lines.pd()
    set_lines.fd(25)
    set_lines.pu()
    set_lines.fd(25)
    



#set the start
a.shape("turtle")
b.shape("turtle")
c.shape("turtle")
d.shape("turtle")
a.color("purple")
b.color("green")
c.color("blue")
d.color("orange")
a.penup()
b.pu()
c.pu()
d.pu()
a.lt(90)
a.fd(60)
b.rt(90)
b.fd(60)
c.lt(90)
c.fd(180)
d.rt(90)
d.fd(180)
a.rt(-90)
b.lt(-90)
c.rt(-90)
d.lt(-90)
a.fd(300)
b.fd(300)
c.fd(300)
d.fd(300)
a.lt(180)
b.rt(180)
c.lt(180)
d.rt(180)
a.speed(0)
b.speed(0)
c.speed(0)
d.speed(0)
a.pd()
b.pd()
c.pd()
d.pd()

#start
a2 = 0
b2 = 0
c2 = 0
d2 = 0

for i in range(250):
    a1 = random.randint(2,5)
    b1 = random.randint(2,5)
    c1 = random.randint(2,5)
    d1 = random.randint(2,5)
    a.fd(a1)
    b.fd(b1)
    c.fd(c1)
    d.fd(d1)
    a2 += a1
    b2 += b1
    c2 += c1
    d2 += d1
    if a2 >= 500:
        print("a won")
        b.hideturtle()
        c.hideturtle()
        d.hideturtle()
        break
    elif b2 >= 500:
        print("b won")
        a.hideturtle()
        c.hideturtle()
        d.hideturtle()
        break
    elif c2 >= 500:
        print("c won")
        a.hideturtle()
        b.hideturtle()
        d.hideturtle()
        break
    elif d2 >= 500:
        print("d won")
        a.hideturtle()
        b.hideturtle()
        c.hideturtle()
        break
    else:
        print(a2,b2,c2,d2)
input()
    
    
