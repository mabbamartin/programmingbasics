


from turtle import left, right, forward, exitonclick

def jump(height=20):
    forward(20)
    left(60)
    forward(height)
    right(120)
    forward(height)
    left(60)


    
    

for size in range(20, 70,5):
    jump(30)

exitonclick()