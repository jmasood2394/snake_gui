import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# Initialize the screen
screen = Screen()
screen.setup(width=600, height=600, startx=2848, starty=200)
screen.bgcolor('black')
screen.title('Snake')
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

# Response to user keys
screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)


is_active = True
while is_active:
    # Refresh the screen every 0.1s
    screen.update()
    time.sleep(0.1)

    # Move Snake
    snake.move()

    if screen.onkey(key='q', fun=None):
        is_active = False


    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.display_score()

    # detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.game_over()
        is_active = False

    # detect collision with any segment of the snake
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            is_active = False
            score.game_over()

screen.exitonclick()
