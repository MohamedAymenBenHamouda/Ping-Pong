import turtle

wind  = turtle.Screen() #initialiser ecran
wind.title("ping pong") #ajouter titre de la fenetre 
wind.bgcolor("black")  #ajouter le couleur de ecran
wind.setup(width=800, height=600) #ajouter le taille de la fenetre
wind.tracer(0)


raq1 = turtle.Turtle()
raq1.speed(0)
raq1.shape("square")
raq1.color("blue")
raq1.shapesize(stretch_wid=5, stretch_len=1)
raq1.penup()
raq1.goto(-350, 0)


raq2 = turtle.Turtle()
raq2.speed(0)
raq2.shape("square")
raq2.color("red")
raq2.shapesize(stretch_wid=5, stretch_len=1)
raq2.penup()
raq2.goto(350, 0)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2.5
ball.dy = 2.5

score1 = 0  
score2 = 0



score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("Player 1: 0 Player 2: 0", align="center", font=("Courier",24,"normal"))


def raq1_up():
    y = raq1.ycor()
    y+=20
    raq1.sety(y)

def raq1_down():
    y = raq1.ycor()
    y-=20
    raq1.sety(y)


def raq2_up():
    y = raq2.ycor()
    y+=20
    raq2.sety(y)

def raq2_down():
    y = raq2.ycor()
    y-=20
    raq2.sety(y)

wind.listen()
wind.onkeypress(raq1_up, "w")
wind.onkeypress(raq1_down, "s")
wind.onkeypress(raq2_up, "Up")
wind.onkeypress(raq2_down, "Down")

while True:
    wind.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() <-290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() >390:
        ball.goto(0, 0)
        ball.dx *= -1
        score1 += 1
        score.clear()
        score.write("Player 1: {} Player 2: {}".format(score1, score2), align="center", font=("Courier",24,"normal"))


    if ball.xcor() <-390:
        ball.goto(0, 0)
        ball.dx *= -1
        score2 += 1
        score.clear()
        score.write("Player 1: {} Player 2: {}".format(score1, score2), align="center", font=("Courier",24,"normal"))


    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < raq2.ycor() + 40 and ball.ycor() > raq2.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < raq1.ycor() + 40 and ball.ycor() > raq1.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1