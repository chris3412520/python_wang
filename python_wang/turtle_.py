import turtle

t = turtle.Turtle()
t.speed(10)
for i in range(36):
    for j in range(4):
        t.forward(100)
        t.left(90)
    t.right(10)
turtle.done()