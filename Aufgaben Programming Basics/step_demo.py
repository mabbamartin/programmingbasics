


from turtle import left, right, forward, exitonclick

def jump(height = 20):
    forward(height)
    left(90)
    forward(height)
    right(90)

for size in range(20, 70,5):
    jump()

exitonclick()



