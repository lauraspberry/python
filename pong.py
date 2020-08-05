import turtle

wn = turtle.Screen()
wn.title("Pong by Laura, from @TokyoEdTech")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

#paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) #speed of animation, something we need to do. max speed
paddle_a.shape("square")
paddle_a.color("white")
#shape default is 20x20
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)


#paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0) #speed of animation, something we need to do. max speed
paddle_b.shape("square")
paddle_b.color("white")
#shape default is 20x20
paddle_b.shapesize(stretch_wid=5, stretch_len=1) #now 20 x 100
paddle_b.penup()
paddle_b.goto(350,0)

#ball
ball = turtle.Turtle()
ball.speed(0) #speed of animation, something we need to do. max speed
ball.shape("square")
ball.color("white")
#shape default is 20x20
ball.penup()
ball.goto(0,0)
#separate into x and y movement
ball.dx = 2
ball.dy = -2 #play with these numbers maybe 0.1; this means every time it moves, it moves by 2 pixels

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0  Player B: 0", align = "center", font = ("Courier", 24, "normal"))


# Function
def paddle_a_up():
	y = paddle_a.ycor()
	y += 20
	paddle_a.sety(y)

def paddle_a_down():
	y = paddle_a.ycor()
	y -= 20
	paddle_a.sety(y)

def paddle_b_up(): 
	y = paddle_b.ycor()
	y += 20
	paddle_b.sety(y)

def paddle_b_down():
	y = paddle_b.ycor()
	y -= 20
	paddle_b.sety(y)

#keyboard binding
wn.listen()
wn.onkey(paddle_a_up, key="w")
wn.onkey(paddle_a_down, key="s")
wn.onkey(paddle_b_up, key="Up")
wn.onkey(paddle_b_down, key="Down")

#main game loop
while True:
	wn.update()

	#Move the Ball
	ball.setx(ball.xcor() + ball.dx)
	ball.sety(ball.ycor() + ball.dy)

	#Border checking: compare y coord. we set height to be 600. ball itself is 20.
	if ball.ycor() > 290:
		ball.sety(290)
		ball.dy *= -1 #reverses the direction TOP

	if ball.ycor() < -290:
		ball.sety(-290)
		ball.dy *= -1 #reverses the direction BOTTOM
	
	if ball.xcor() > 390: #past the paddle and off the screen
		ball.goto(0,0)
		ball.dx *= -1
		score_a += 1
		pen.clear()
		pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align = "center", font = ("Courier", 24, "normal"))


	if ball.xcor() < -390: #past the paddle and off the screen
		ball.goto(0,0)
		ball.dx *= -1
		score_b += 1
		pen.clear()
		pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align = "center", font = ("Courier", 24, "normal"))


	#Paddle and ball collisions
	if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < (paddle_b.ycor() + 40) and ball.ycor() > (paddle_b.ycor() - 40)):
		ball.setx(340)
		ball.dx *= -1

	if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < (paddle_a.ycor() + 40) and ball.ycor() > (paddle_a.ycor() - 40)):
		ball.setx(-340)
		ball.dx *= -1
