import turtle as t
POSITIONS=[-20,0,20]
class Stick:
    def __init__(self,dist_x):
        self.segment=[]
        for i in POSITIONS:
            seg=t.Turtle()
            seg.color("white")
            seg.shape("square")
            seg.penup()
            seg.goto((dist_x,i))
            self.segment.append(seg)

    def move(self):
        for i in range(3):
            self.segment[i].forward(20)

    def upward(self):
        for i in range (3):
            self.segment[i].setheading(90)
        self.move()

    def downward(self):
        for i in range (3):
            self.segment[i].setheading(270)
        self.move()
