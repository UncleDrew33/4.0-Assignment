import turtle
t = turtle.Turtle()
t.speed(100)
canvas = t.getscreen()
canvas.bgcolor('gray')
mycolors = ['red','orange','peachpuff','violet','white','blue','green','yellow']
def flower(length,x,y):
  t.penup()
  t.goto(x,y)
  t.pendown()
  for c in mycolors:
    t.pencolor(c)
    for i in range (4):
      t.rt(45)
      t.forward(length)
    t.penup()
    t.rt(45)
    t.pendown()
x = -50
y = 50
for i in range(10):
  flower(20,x,y)
  x = x + 90
  y = y 
