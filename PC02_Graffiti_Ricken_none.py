#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: Devon
May 29, 2020
'''

from turtle import * #import the library of commands that you'd like to use

colormode(255)

# Create a panel to draw on. 
panel = Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
#panel.bgcolor("lightsteelblue")
panel.bgpic(image)

#=======Add your code here======

t=Turtle()

# Drawing the right Ear
t.penup()
t.left(90)
t.forward(200)
t.right(90)
t.forward(30)
t.pendown()
t.circle(30)
t.penup()

#Drawing the left Ear

t.left(90)
t.forward(60)
t.left(90)
t.forward(100)
t.pendown()
t.circle(30)
t.penup()

# Drawing Nose
t.left(90)
t.forward(180)
t.left(90)
t.forward(100)
t.pendown()
t.begin_fill()
t.circle(10)
t.end_fill()
t.penup()

# Drawing Whiskers
t.left(180)
t.forward(35)
x1=t.xcor()
y1=t.ycor()
t.right(45)
t.pensize(10)
t.pendown()
t.forward(50)
t.penup()
t.goto(x1,y1)
t.left(45)
t.pendown()
t.forward(50)
t.penup()
t.goto(x1,y1)
t.left(45)
t.pendown()
t.forward(50)
t.penup()
t.goto(x1,y1)

#Drawing right Whiskers
t.right(225)
t.forward(55)
x2=t.xcor()
y2=t.ycor()
t.left(45)
t.pendown()
t.forward(50)
t.penup()
t.goto(x2,y2)
t.right(45)
t.pendown()
t.forward(50)
t.penup()
t.goto(x2,y2)
t.right(45)
t.pendown()
t.forward(50)
t.penup()
t.goto(x2,y2)


# Drawing a new tie
t.goto(0,0)
t.right(45)
t.forward(30)
t.color("yellow")
t.pendown()
t.begin_fill()
t.left(45)
t.forward(20)
t.right(90)
t.forward(20)
t.right(90)
t.forward(20)
t.right(90)
t.forward(20)
t.end_fill()
t.penup()
t.right(135)
t.forward(30)
t.right(25)
t.pendown()
t.begin_fill()
t.forward(60)
t.left(45)
t.forward(15)
t.left(95)
t.forward(15)
t.left(70)
t.forward(45)
t.end_fill()





