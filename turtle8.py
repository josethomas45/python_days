import turtle

# Create a turtle object
t = turtle.Turtle()

# Set the turtle's appearance
t.shape("turtle")
t.color("green")

# Move to the starting position
t.penup()
t.goto(-50, -50)
t.pendown()

# Draw a pentagon
for _ in range(5):
    t.forward(100)
    t.right(72)

# Finish the turtle graphics
turtle.done()
