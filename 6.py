from turtle import *
color =["red", "yellow", "purple", "blue", "green", "orange", "pink"]
for i in range (150):
    pencolor(color[i % 7])
    forward(i)
    left(51)
