import turtle
t = turtle.Turtle()
t.speed(50)
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
      t.rt(90)
      t.forward(length)
    t.penup()
    t.rt(45)
    t.pendown()
x = -120
y = 120
for i in range(10):
  flower(20,x,y)
  x = x + 60
  y = y + 60
