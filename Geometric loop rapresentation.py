import turtle
import random
screen = turtle.Screen()
screen.bgcolor("black")
bob = turtle.Turtle()
n = 10.0
bob.speed(0)
bob.hideturtle()
colors = ["red","orange","brown","yellow","green","blue","purple"]
k = 0
figure = int(input("numero di lati: "))
while 1:
	if k == 7:
		k = 0
	r = colors[k]
	bob.lt(5)
	bob.color(r)
	for i in range(figure):
		bob.lt(360/figure)
		bob.fd(n)
		n += 0.5
	k += 1
