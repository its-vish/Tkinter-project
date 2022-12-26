from turtle import *
t1=Turtle()
color=["red","blue","yellow","purple","black","indigo","violet","pink"]
import random

t1.up()
t1.goto(-200,10)
t1.down()
t1.width(40)
t1.hideturtle()
t1.speed(0)
t1.dot()

t1.backward(50)
for i in range(900):
    colorchoice=random.choice(color)
    t1.color(colorchoice)
    # size
    t1.forward(400)
    #angle
    t1.left(181)
