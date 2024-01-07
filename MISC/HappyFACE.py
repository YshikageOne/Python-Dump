import turtle

# Set up the turtle
t = turtle.Turtle()

# Draw the face
t.circle(100)

# Draw the eyes
t.penup()
t.goto(-40, 120)
t.pendown()
t.circle(20)
t.penup()
t.goto(40, 120)
t.pendown()
t.circle(20)

# Draw the mouth
t.penup()
t.goto(-60, 80)
t.pendown()
t.right(90)
t.circle(60, 180)

# Hide the turtle
t.hideturtle()

# Keep the window open until closed
turtle.done()