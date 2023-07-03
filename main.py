from turtle import Turtle,Screen
import random

screen = Screen()

screen.setup(width=500, height=400)
user_guess = screen.textinput(title="What Your Bet", prompt="Which Color do you wanna bet ?")
colours = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
x_axis = -230
y_axis = -100

is_race_on = False
turtle_position = []

for turtle_color in colours:
    tim = Turtle(shape='turtle')
    tim.color(turtle_color)
    tim.penup()
    tim.goto(x= x_axis, y=y_axis)
    turtle_position.append(tim)
    y_axis += 40

if user_guess:
    is_race_on = True

while is_race_on:
    for turtle in turtle_position:
        random_forward = random.randint(0, 10)
        turtle.forward(random_forward)

        if turtle.xcor() > 230:
            winning_turtle = turtle.pencolor()
            is_race_on = False
            if user_guess == winning_turtle:
                print(f"You Win, {winning_turtle} is the winner")
            else:
                print(f"You Lose, {winning_turtle} is the winner")

screen.exitonclick()