import turtle
t = turtle.Turtle()
s = turtle.Screen()

turtleImg = 'C:\python\images\Rock.gif'

s.addshape(turtleImg)
t.shape(turtleImg)
t.penup()
#t.shape("classic")
a = int(input("숫자를 입력하세요 : "))
t.circle(a/2)
t.forward(a/2)
t.left(90)
t.forward(a)
t.left(90)
t.forward(a)
t.left(90)
t.forward(a)
t.left(90)
t.forward(a/2)