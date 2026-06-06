import turtle
import random
import time

# স্ক্রিন সেটআপ
win = turtle.Screen()
win.title("ফ্ল্যাপি বার্ড গেইม")
win.bgcolor("skyblue")
win.setup(width=500, height=700)
win.tracer(0)

# গ্র্যাভিটি বা অভিকর্ষজ টান
gravity = -0.3

# প্লেয়ার (বার্ড) তৈরি
bird = turtle.Turtle()
bird.speed(0)
bird.shape("circle")
bird.color("yellow")
bird.penup()
bird.goto(-100, 0)
bird.dy = 0  # বার্ডের ওয়াই অক্ষ বরাবর গতি

# ওপরের পাইপ
pipe_top = turtle.Turtle()
pipe_top.speed(0)
pipe_top.shape("square")
pipe_top.color("green")
pipe_top.shapesize(stretch_wid=18, stretch_len=3)
pipe_top.penup()
pipe_top.goto(300, 250)

# নিচের পাইপ
pipe_bottom = turtle.Turtle()
pipe_bottom.speed(0)
pipe_bottom.shape("square")
pipe_bottom.color("green")
pipe_bottom.shapesize(stretch_wid=18, stretch_len=3)
pipe_bottom.penup()
pipe_bottom.goto(300, -250)

pipe_speed = 3
gap = 150  # পাইপ দুটির মাঝখানের ফাঁকা জায়গা

# স্কোর ট্র্যাকিং
score = 0
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.hideturtle()
score_pen.goto(0, 300)
score_pen.write("Score: 0", align="center", font=("Arial", 20, "bold"))

# বার্ডকে ওপরে লাফ দেওয়ানোর ফাংশন
def go_up():
    bird.dy = 6  # প্রতি ক্লিকে বার্ড একটু ওপরে উঠবে

# কিবোর্ড বাইন্ডিং (Spacebar চাপলে লাফ দেবে)
win.listen()
win.onkeypress(go_up, "space")

# মূল গেইম লুপ
game_over = False

while not game_over:
    win.update()
    time.sleep(0.01)

    # বার্ডের ওপর গ্র্যাভিটির প্রভাব
    bird.dy += gravity
    y = bird.ycor()
    y += bird.dy
    bird.sety(y)

    # পাইপ বাম দিকে নিয়ে যাওয়া
    x = pipe_top.xcor()
    x -= pipe_speed
    pipe_top.setx(x)
    pipe_bottom.setx(x)

    # পাইপ স্ক্রিনের বাইরে চলে গেলে আবার ডান দিক থেকে নতুন পজিশনে আসবে
    if pipe_top.xcor() < -300:
        new_y = random.randint(-80, 80)
        pipe_top.setposition(300, 250 + new_y)
        pipe_bottom.setposition(300, -250 + new_y)
        
        # স্কোর বাড়ানো
        score += 1
        score_pen.clear()
        score_pen.write(f"Score: {score}", align="center", font=("Arial", 20, "bold"))

    # মেঝ বা ছাদের সাথে ধাক্কা লাগলে গেইম ওভার
    if bird.ycor() < -330 or bird.ycor() > 330:
        game_over = True

    # পাইপের সাথে পাখির ধাক্কা লাগার লজিক (Collision Detection)
    # চেক করা হচ্ছে পাখিটি পাইপের এক্স অক্ষের ভেতরে আছে কিনা
    if (bird.xcor() + 10 > pipe_top.xcor() - 30) and (bird.xcor() - 10 < pipe_top.xcor() + 30):
        # ওপরের বা নিচের পাইপের ওয়াই অক্ষের সাথে ধাক্কা লেগেছে কিনা
        if (bird.ycor() + 10 > pipe_top.ycor() - 180) or (bird.ycor() - 10 < pipe_bottom.ycor() + 180):
            game_over = True

# গেইম ওভার স্ক্রিন
score_pen.goto(0, 0)
score_pen.color("red")
score_pen.write("GAME OVER", align="center", font=("Arial", 30, "bold"))
win.update()

# উইন্ডো আটকে রাখার জন্য
turtle.done()