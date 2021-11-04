import turtle as tl

def draw_fractal(scale):
    if scale >= 1:
        draw_fractal(scale / 3.0)
        tl.left(45)
        draw_fractal(scale / 3.0)
        tl.right(180)
        draw_fractal(scale / 3.0)
        tl.left(46)
        draw_fractal(scale / 3.0)
    else:
        tl.forward(2.5)

tl.delay(0)
scale = 400
tl.pensize(1)
tl.penup()
tl.goto(-250, -100)
tl.pendown()
tl.left(90)
draw_fractal(scale)
tl.done()
