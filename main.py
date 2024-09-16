import random
import turtle

# Screen setup
screen = turtle.Screen()
screen.title("Breakout Game")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)  # Turn off screen updates

# Paddle
paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5, outline=False)
paddle.penup()
paddle.goto(0, -250)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = -0.2

colors = ['red', 'yellow', 'blue', 'green', 'pink', 'cyan']
# Bricks
bricks = []
for i in range(3):
    for j in range(9):
        brick = turtle.Turtle()
        brick.speed(0)
        brick.shape("square")
        brick.shapesize(1, 3, 0)
        brick.color(random.choice(colors))
        brick.penup()
        brick.goto(-280 + j * 65, 230 - i * 40)
        bricks.append(brick)


# Game functions
def paddle_move_left():
    x = paddle.xcor()
    if x >= -300 + 80:
        x -= 20
        paddle.setx(x)


def paddle_move_right():
    x = paddle.xcor()
    if x <= 300 - 80:
        x += 20
        paddle.setx(x)


# Keyboard bindings
screen.listen()
screen.onkeypress(paddle_move_left, "Left")
screen.onkeypress(paddle_move_right, "Right")

# Game loop
while True:
    screen.update()

    # Ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.goto(0, 0)
        ball.dx = 0.2
        ball.dy = -0.2
    if ball.xcor() > 290 or ball.xcor() < -290:
        ball.dx *= -1

    # Paddle collision
    if (ball.ycor() < -220 and ball.xcor() > paddle.xcor() - 50
            and ball.xcor() < paddle.xcor() + 50):
        ball.sety(-220)
        ball.dy *= -1
    # Brick collision
    for brick in bricks:
        if (ball.xcor() > brick.xcor() - 30 and ball.xcor() < brick.xcor() + 30
                and ball.ycor() > brick.ycor() - 20 and ball.ycor() < brick.ycor() + 20):
            ball.dy *= -1
            brick.hideturtle()
            bricks.remove(brick)
