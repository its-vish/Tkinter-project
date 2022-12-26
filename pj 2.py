from tkinter import Canvas
import turtle
t =turtle.Turtle()

for x in range(1000):
    t.forward(x)
    t.left(200)
    t.circle(x)
    t.pencolor("pink")
    Canvas=turtle.Screen()
    Canvas.bgcolor("black")