from turtle import *

my_turtle = Turtle()
my_turtle.speed(0)
my_turtle.screen.setup(1200, 800)

# нарисовать квадрат
def draw_rect(t):
    for x in range(0, 1):
        t.circle(30)
        t.right(70)
        t.forward(100)
        t.right(470)
        t.forward(100)
        t.right(470)
        t.forward(120)
        t.circle(100, 360)
        t.backward(100)
        t.left(90)
        t.circle(-90, 35)

# рисует квадраты в цикле
for x in range(0, 1):
    draw_rect(my_turtle)
    my_turtle.right(1)

# необходимо, чтобы окно не закрывалось само, а только по клику
my_turtle.screen.exitonclick()
my_turtle.screen.mainloop()
