import turtle
t = turtle.Turtle()
t.speed(50)
canvas = t.getscreen()
canvas.bgcolor('gray')
def move(x,y):
  t.penup()
  t.goto(x,y)
  t.pendown()
mycolors = ['red','orange','peachpuff','violet','white','blue','green','yellow']
move(-100,100)
for c in mycolors:
  t.pencolor(c)
  for i in range (4):
   t.rt(90)
   t.forward(45)
  t.penup()
  t.rt(45)
  t.pendown()
move (0,-100)
for i in range(4):
  t.lt(90)
  t.forward(45)