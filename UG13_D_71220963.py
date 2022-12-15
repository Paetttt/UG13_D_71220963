import turtle
lol=turtle.Turtle()
lol.pensize(20)

lol.color("white")
lol.screen.bgcolor("purple")
lol.penup()
lol.setpos(50,180)
lol.pendown()

lol.forward(30)
lol.backward(30)

lol.circle(-40,-185)
lol.circle(40,-250)

lol.up()
lol.goto(200,-40)
lol.pendown()
lol.circle(50,180)
lol.right(180)
lol.circle(50,180)
lol=turtle.Screen().exitonclick()