from turtle import *

width = 600
height = 420

setup(width, height)
bgcolor('yellow')
speed(1)

up()
goto(- width / 2, height / 6)
down()

def rect(colorName, dirrection):
    color ( colorName )
    begin_fill ()

    for length in [width, height / 3, width, height / 3]:
        forward ( length )
        dirrection ( 90 )
    end_fill ()

rect('black', left)

rect('red', right)

mainloop()