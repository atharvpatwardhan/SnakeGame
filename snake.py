import turtle
import time
import random
import pygame
from pygame.locals import *
pygame.init()
#music = pygame.mixer.music.load("mixkit-arcade-retro-changing-tab-206.wav")
#pygame.mixer.music.play(-1)


delay = 0.1

score = 0
high_score = 0

wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("blue")
wn.setup(width = 600, height = 600)
wn.tracer(0)

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("light blue")
head.penup()
head.goto(0,0)
head.direction = "stop"

food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("green")
food.penup()
food.goto(0,100)

segments = []

sc = turtle.Turtle()
sc.speed(0)
sc.shape("square")
sc.color("black")
sc.penup()
sc.hideturtle()
sc.goto(0,260)
sc.write("score : 0 High Score : 0",align="center",font=("ds-digital",24,"normal"))

def go_up():
    if head.direction != "down":
        head.direction = "up"
def go_down():
    if head.direction != "up":
        head.direction = "down"
def go_left():
    if head.direction != "right":
        head.direction = "left"
def go_right():
    if head.direction != "left":
        head.direction = "right"
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)
    
wn.listen()
wn.onkeypress(go_up,"w")
wn.onkeypress(go_down,"s")
wn.onkeypress(go_left,"a")
wn.onkeypress(go_right,"d")

while True:
    wn.update()

    #check collision with border area
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        #hide the segments of body
        for segment in segments:
            segment.goto(1000,1000) #out of range
        #clear the segments
        segments.clear()

        #reset score
        score = 0

        #reset delay
        delay = 0.1

        sc.clear()
        sc.write("score: {}  High score: {}".format(score, high_score), align="center", font=("ds-digital", 24, "normal"))
        music = pygame.mixer.music.load("mixkit-arcade-retro-game-over-213.wav")
        pygame.mixer.music.play()
    #check collision with food
    if head.distance(food) <20:
        # move the food to random place
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x,y)
        music = pygame.mixer.music.load("mixkit-retro-arcade-casino-notification-211.wav")
        pygame.mixer.music.play(-1)
        #add a new segment to the head
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("black")
        new_segment.penup()
        segments.append(new_segment)

        #shorten the delay
        delay -= 0.001
        #increase the score
        score += 10

        if score > high_score:
            high_score = score
        sc.clear()
        sc.write("score: {}  High score: {}".format(score,high_score), align="center", font=("ds-digital", 24, "normal")) 

    #move the segments in reverse order
    for index in range(len(segments)-1,0,-1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)
    #move segment 0 to head
    if len(segments)>0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()

    #check for collision with body
    for segment in segments:
        if segment.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            #hide segments
            for segment in segments:
                segment.goto(1000,1000)
            segments.clear()
            score = 0
            delay = 0.1

            #update the score     
            sc.clear()
            sc.write("score: {}  High score: {}".format(score,high_score), align="center", font=("ds-digital", 24, "normal"))
            music = pygame.mixer.music.load("mixkit-arcade-retro-game-over-213.wav")
            pygame.mixer.music.play(0)
    time.sleep(delay)
wn.mainloop()   