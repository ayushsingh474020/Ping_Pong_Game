import turtle as t
from stick import Stick
from ball import Ball
from scorecard import Scorecard
import time
import random

stick1=Stick(-280)
stick2=Stick(280)
print(stick2.segment[0].pos() , stick2.segment[1].pos() , stick2.segment[2].pos())
ball=Ball()
scorecard1=Scorecard(-50)
scorecard2=Scorecard(50)
screen=t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

def start():
    while(True):
        screen.update()
        time.sleep(0.1)
        scorecard1.update()
        scorecard2.update()
        ball.move()
        ball.collission_with_wall()
        collission_with_stick()
        if(ball.xcor()>300):
            return game_over(2)
        elif(ball.xcor()<-300):
            return game_over(1)

def game_over(player):
    ball.goto(0,0)

    if(player==1):
        scorecard2.increment()
        if(scorecard2.score==5):
            scorecard2.game_won(2)
            return
        ball.setheading(360-random.randint(105,275))

    else:
        scorecard1.increment()
        if (scorecard1.score == 5):
            scorecard1.game_won(2)
            return
        ball.setheading(random.randint(95,265))
    start()

def collission_with_stick():
    if check_condition():
        # print(ball.xcor())
        if(ball.heading()==0):
            ball.setheading(180)
        elif(ball.heading()==180.0):
            ball.setheading(0)
        elif (ball.heading() > 0 and ball.heading() < 90):
            ball.left(2 *ball.heading())
        elif (ball.heading() > 90 and ball.heading() < 180):
            ball.right(2 * (180 - ball.heading()))
        elif (ball.heading() > 180 and ball.heading() < 270):
            ball.left(2 * (ball.heading() - 180))
        else:
            ball.right(2 * (360 - ball.heading()))
        ball.increase_speed()

def check_condition():
    if (ball.xcor() <= -270):
        if (ball.ycor()>=stick1.segment[0].ycor()-35 and ball.ycor()<=stick1.segment[0].ycor()+35):
            return True
        return False
    elif (ball.xcor() >= 270):
        if (ball.ycor() >= stick2.segment[0].ycor() - 35 and ball.ycor() <= stick2.segment[0].ycor()+35):
            return True
        return False



screen.listen()
screen.onkey(start,"space")
screen.onkey(stick1.upward,"w")
screen.onkey(stick1.downward,"s")
screen.onkey(stick2.upward,"Up")
screen.onkey(stick2.downward,"Down")
screen.exitonclick()