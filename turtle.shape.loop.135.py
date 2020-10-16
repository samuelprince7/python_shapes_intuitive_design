import turtle

my_turtle = turtle.Turtle()

def square(length, angle):
    for i in range(3): 
        my_turtle.forward(length)
        my_turtle.left(angle)
    
    my_turtle.forward(length)


for i in range(20):
    square(50, 90)
    square(50, 135) 










    
