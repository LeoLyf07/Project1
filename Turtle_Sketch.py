
import turtle as t
import time
t.bgcolor("White")
t.speed(2)
t.title("Sumit") # this line will change the canvas name 
t.pensize(20)
# t.color("Yellow","pink")
t.begin_fill() # it will fill the background of our drawing when it compltes
t.color("Yellow","Brown")
for i in range(16):
    t.forward(100)
    t.right(45)
    t.left(34)
    t.backward(120)
for i in range(16):
    t.forward(100)
    t.right(45)
    t.left(34)
    t.backward(120)

t.hideturtle()
t.end_fill()
# time.sleep(3) remove comment to make your canvas auto hide in 3 sec
t.done()
