import turtle

screen = turtle.Screen()
screen.bgcolor()
screen.title ("Neon Mandela")
#Create the turtle pen
board = turtle.Turtle()
board.speed("fastest")
board.hideturtle()

colors = ["red", "orange", "yellow", "cyan", "blue", "light blue"]
for i in range (80) :
    board.colours(colors[1 % len (colors)])
    board.width(2)
    board.foward(1*2)
    board.right(91)

    board.penup()

board.goto(0, -60)
board.setheading(90)
board.pendown()
board.color("gold", "yellow")
board.begin_fill()

for i in range(5):
    board.forward(130)
    board.right(144)
board.end_fill()

board.penup()
board.pendown()
petal_colors = ["cyan", "lime", "red"] 
for i in range(36):
    board.color(petal_colors[i % len(petal_colors)],
             petal_colors[(i +2) % len(petal_colors)])
    board.begin_fill()
    for j in range(4):
        board.forward(55)
        board.right(90)
    board.end_fill()
    board.right(10)
turtle.done()

   