import turtle
size = 50
t = turtle.Turtle()
t.speed(0)

t.penup()
t.setposition(0, 60)
t.pendown()
style = ('Arial', 15, 'italic')
t.write('X-view display - find muon track with 3 planes', font=style, align='center')



def triangle(up, x, y, inten):
  t.penup()
  t.setposition(x,y)
  t.setheading(0)
  if(up):
    t.pendown()
    t.forward(size)
    t.left(120)
    t.forward(size)
    t.left(120)
    t.forward(size)
  else:
    t.pendown()
    t.left(60)
    t.forward(size)
    t.left(120)
    t.forward(size)
    t.left(120)
    t.forward(size)
 

for y in range(0,-300,-100):

	for x in range(-100,100,size):
		triangle(False, x, y, 20)
		triangle(True, x, y,20)

