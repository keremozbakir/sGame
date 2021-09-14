from turtle import Screen
from snake import Snake
from food import Food
import time
from scoreboard import Scoreboard

scoreboard = Scoreboard()
food = Food()
screen = Screen()
screen.setup(width=680, height=600)
screen.bgcolor("black")
screen.title("my snake game")
screen.tracer(0)
screen.listen()
snake = Snake()

game_is_on = True

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_is_on:
    screen.update()
    time.sleep(0.1)
    # snake.create_snake()
    snake.move_snake()
    if snake.head.distance(food) < 15:
        print("collusion!!")
        food.refresh()
        snake.extend()
        scoreboard.add_point()
    if snake.head.xcor() > 335 or snake.head.xcor() < -338 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        print("game over bitch")
        print("your score is {scoreboard.score}")

        scoreboard.game_over()
        game_is_on = False
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10 :
            scoreboard.game_over()
            game_is_on = False


screen.exitonclick()
