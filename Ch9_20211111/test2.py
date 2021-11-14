import turtle
def draw_square(tur):
    for i in range(1,5):
        tur.forward(100)
        tur.right(90)
window = turtle.Screen()
window.bgcolor("grey")
sean = turtle.Turtle()
sean.shape("turtle")
sean.color("green")
draw_square(sean)

amy = turtle.Turtle()
amy.shape('arrow')
amy.goto(0,30)
amy.color('red')
amy.circle(60)
window.exitonclick()
