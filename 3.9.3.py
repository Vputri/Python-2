import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
abc = turtle.Turtle()
abc.shape("turtle")
abc.color("red")
abc.penup()
size = 20
for i in range (30):
    abc.stamp()
    size = size +3
    abc.forward(size)
    abc.right(30)
    
de = turtle.Turtle()
de.shape("turtle")
de.color("blue")
de.penup()
size = 20
for i in range (30):
    de.stamp()
    size = size +3
    de.forward(size)
    de.right(30)

e = turtle.Turtle()
e.shape("turtle")
e.color("yellow")
e.penup()
size = 20
for i in range (30):
    e.stamp()
    size = size +3
    e.forward(size)
    e.right(30)
wn.mainloop()
