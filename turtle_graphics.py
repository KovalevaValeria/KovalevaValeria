import turtle
t = turtle.Pen()
turtle.bgcolor("black")
colors = ["red", "yellow", "cyan", "orange"]

for x in range(150):
    t.pencolor(colors[x%4])
    t.forward(x)
    t.right(91)

for x in range(101):
    t.pencolor(colors[x%4])
    t.forward(x)
    t.left(91)
    
for x in range(50):
    t.pencolor(colors[x%4])
    t.forward(x)
    t.right(91)
    
