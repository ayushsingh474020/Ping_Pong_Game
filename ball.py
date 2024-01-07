import turtle as t
import random
class Ball(t.Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(0.5,0.5)
        self.penup()
        self.setheading(random.randint(1,359))
        self.speed=10

    def move(self):
        self.forward(self.speed)

    def increase_speed(self):
        self.speed+=1

    def collission_with_wall(self):
        if(self.ycor()>260 or self.ycor()<-260):
            if(self.heading()==90):
                self.setheading(270)
            elif(self.heading()==270):
                self.setheading(90)
            elif(self.heading()>0 and self.heading()<90):
                self.right(2*(90-self.heading()))
            elif (self.heading() > 90 and self.heading() < 180):
                self.left(2*(180-self.heading()))
            elif (self.heading() > 180 and self.heading() < 270):
                self.right(2*(self.heading() - 180))
            else:
                self.left(2 * (360 - self.heading()))
            print(self.xcor(),self.ycor())