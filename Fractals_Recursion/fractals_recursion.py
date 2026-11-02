import turtle
import time
import random

t = turtle.Turtle()

l_list = [200*(2**n) for n in range(0,-6, -1)]
clr_list = ['red', 'blue', 'green', 'orange', 'purple', 'yellow']

def square(x, y, level):

  l = l_list[level]
  t.color(clr_list[level])

  
  t.penup()
  t.goto(x, y)

  t.pendown()
  t.setheading(random.randint(-20, 20))


  t.begin_fill()
  for _ in range(4):
     t.forward(l)
     t.left(90)
     
  
  t.end_fill()

  if level < 5:   
        square(x + 9/8*l, y - 3/4*l, level + 1)
        square(x - 5/8*l, y - 3/4*l, level + 1)

  
    

def branch(sz, level):
  if level > 0:

    if level ==1:
       t.color('green')
    else:
        t.color('brown')

    t.pensize(level)
    t.forward(sz)

    if level == 1:
       t.color('red')
       t.dot(5)


    t.right(20)
    branch(0.8*sz, level -1)   
    t.left(2*20)
    branch(0.8*sz, level -1)
    t.right(20)
    t.penup()
    t.forward(-sz)
    t.pendown()

ts = t.screen 

def animate():
   t.clear()
   ts.tracer(0)
   square(-100, 60, 0)
   ts.update()
   ts.ontimer(animate, 500)



# Calling the functions

t.goto(0, 0)

square(-100, 100, 0)


t.speed(0)
t.clear()
t.penup()
t.goto(0, -150)
t.pendown()
t.setheading(90)

branch(100, 8)