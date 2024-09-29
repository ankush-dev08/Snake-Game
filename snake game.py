import time
import turtle
import random

# Screen setup
display = turtle.Screen()
display.title("Snake Game")
display.bgcolor("gray")
display.setup(width=600, height=600)

# Snake body
s = turtle.Turtle()
s.speed(0)
s.shape("square")
s.color("White")
s.fillcolor("Blue")
s.penup()
s.goto(0, 0)
s.direction = "stop"

# Food for the snake
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("Yellow")
food.fillcolor("Green")
food.penup()
food.hideturtle()
food.goto(0, 200)
food.showturtle()

# Scoreboard
sb = turtle.Turtle()
sb.speed(0)
sb.shape("square")
sb.fillcolor("gray")
sb.penup()
sb.goto(-250, 250)
sb.hideturtle()
sb.write("Your Score: 0 | Highest Score: 0", align="left", font=("Courier", 14, "normal"))

# Variables
score = 0
highest_score = 0
delay = 0.1
bodies = []

def move_up():
    if s.direction != "down":
        s.direction = "up"

def move_down():
    if s.direction != "up":
        s.direction = "down"

def move_left():
    if s.direction != "right":
        s.direction = "left"

def move_right():
    if s.direction != "left":
        s.direction = "right"

def move():
    if s.direction == "up":
        y = s.ycor()
        s.sety(y + 20)
    if s.direction == "down":
        y = s.ycor()
        s.sety(y - 20)
    if s.direction == "right":
        x = s.xcor()
        s.setx(x + 20)
    if s.direction == "left":
        x = s.xcor()
        s.setx(x - 20)

# Key mapping
display.listen()
display.onkey(move_up, "Up")
display.onkey(move_down, "Down")
display.onkey(move_left, "Left")
display.onkey(move_right, "Right")

# Main loop
while True:
    display.update()

    # Check boundaries
    if s.xcor() > 290:
        s.setx(-290)
    if s.xcor() < -290:
        s.setx(290)
    if s.ycor() > 290:
        s.sety(-290)
    if s.ycor() < -290:
        s.sety(290)

    # Food collision
    if s.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Add a new body segment
        body = turtle.Turtle()
        body.speed(0)
        body.penup()
        body.shape("square")
        body.color("Red")
        body.fillcolor("Black")
        bodies.append(body)

        # Score update
        score += 10
        if score > highest_score:
            highest_score = score
        sb.clear()
        sb.write(f"Your Score: {score} | Highest Score: {highest_score}", align="left", font=("Courier", 14, "normal"))

        delay -= 0.001

    # Move the body segments
    for index in range(len(bodies) - 1, 0, -1):
        x = bodies[index - 1].xcor()
        y = bodies[index - 1].ycor()
        bodies[index].goto(x, y)
    if len(bodies) > 0:
        x = s.xcor()
        y = s.ycor()
        bodies[0].goto(x, y)

    move()

    # Check self-collision
    for body in bodies:
        if body.distance(s) < 20:
            score = 0
            bodies.clear()
            delay = 0.1
            sb.clear()
            sb.write(f"Your Score: {score} | Highest Score: {highest_score}", align="left", font=("Courier", 14, "normal"))

    time.sleep(delay)

# End of the game
display.mainloop()
