import turtle

my_turtle = turtle.Turtle()
my_turtle.speed(0)

def square(length, angle):
    for i in range(4): 
        my_turtle.forward(length)
        my_turtle.right(angle)
    
for i in range(333):
    square(150, 90)
    my_turtle.right(17)
