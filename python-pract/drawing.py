import turtle
import math
import random

wh = turtle.Screen()
wh.bgcolor('black')

Red = turtle.Turtle()
Red.speed(0)
Red.color('grey')

def drawCircles(t, size):
  for i in range(10):
    t.circle(size)
    size = size - 4

def drawSpecial(t, size, repeat):
  for i in range(repeat):
    drawCircles(t, size)
    t.right(360 / repeat)

drawSpecial(Red, 100, 10)

Green = turtle.Turtle()
Green.speed(0)
Green.color('purple')
rotate = int(90)

drawSpecial(Green, 100, 10)

Blue = turtle.Turtle()
Blue.speed(0)
Blue.color('white')
rotate = int(90)

drawSpecial(Blue, 100,10)