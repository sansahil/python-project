import turtle

pen = turtle.Turtle
pen.shape("triangle")
pen.speed(10)


window = tuple.screen()

window.bgcolor("white")
rainbow =['red','orange','yellow','green','blue','indigo','violet','white']


size = 250
pen.penup()
pen.goto(0,-360)

for color in rainbow:

    pen.color(color)
    pen.fillcolor(color)
    pen.begin_fill()
    pen.circle(size)
    pen.end_fill()
    size -= 20


tuple.done()    
