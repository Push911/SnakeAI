import turtle
import random
import gym
import math
import time

ROWS = 20
SCREENDIM = ROWS * ROWS


class Environment(gym.Env):
    def __init__(self, human=False, env_info={"state_space": None}):
        super(Environment, self).__init__()
        self.done = False
        self.reward = 0
        self.actionSpace = 4
        self.stateSpace = 12
        self.total, self.highestScore = 0, 0
        self.human = human
        self.envInfo = env_info

        self.screen = turtle.Screen()
        self.screen.title("Snake AI")
        self.screen.bgcolor("white")
        self.screen.tracer(0)
        self.screen.setup(width=SCREENDIM+32, height=SCREENDIM+32)

        self.snake = turtle.Turtle()
        self.snake.shape("square")
        self.snake.speed(0)
        # penup - no drawing while moving
        self.snake.penup()
        self.snake.color("green")
        self.snake.goto(0, 0)
        self.snake.direction = "stop"
        self.snakeList = []
        self.bodySize = 20
        self.drawSnake()

        self.food = turtle.Turtle()
        self.food.speed(0)
        self.food.shape("square")
        self.food.color("red")
        self.food.penup()
        self.newFood(first=True)

        self.distance = math.sqrt((self.snake.xcor() - self.food.xcor()) ** 2 + (self.snake.ycor() - self.food.ycor()) ** 2)
        self.previousDistance = 0

        self.score = turtle.Turtle()
        self.score.speed(0)
        self.score.color("black")
        self.score.penup()
        self.score.hideturtle()
        self.score.goto(0, 100)
        self.score.write(f"Total score: {self.total}. Highest score: {self.highestScore}", align="center")

        self.screen.listen()
        self.screen.onkey(self.up, "Up")
        self.screen.onkey(self.down, "Down")
        self.screen.onkey(self.right, "Right")
        self.screen.onkey(self.left, "Left")

    @staticmethod
    def foodLocation():
        foodX = random.randint(-ROWS / 2, ROWS / 2)
        foodY = random.randint(-ROWS / 2, ROWS / 2)
        return foodX, foodY

    def moveSnake(self):
        if self.snake.direction == "stop":
            self.reward = 0
        if self.snake.direction == "up":
            y = self.snake.ycor()
            self.snake.sety(y + 20)
        if self.snake.direction == "down":
            y = self.snake.ycor()
            self.snake.sety(y - 20)
        if self.snake.direction == "right":
            x = self.snake.xcor()
            self.snake.setx(x + 20)
        if self.snake.direction == "left":
            x = self.snake.xcor()
            self.snake.setx(x - 20)

    def up(self):
        if self.snake.direction != "down":
            self.snake.direction = "up"

    def down(self):
        if self.snake.direction != "up":
            self.snake.direction = "down"

    def right(self):
        if self.snake.direction != "left":
            self.snake.direction = "right"

    def left(self):
        if self.snake.direction != "right":
            self.snake.direction = "left"

    def newFood(self, first=False):
        if first or self.snake.distance(self.food) < 20:
            while True:
                self.food.x, self.food.y = self.foodLocation()
                self.food.goto(round(self.food.x * 20), round(self.food.y * 20))
                if not self.checkFood():
                    break

            if not first:
                self.updateScore()
                self.drawSnake()

            return True

    def updateScore(self):
        self.total += 1
        if self.total >= self.highestScore:
            self.highestScore = self.total
        self.score.clear()
        self.score.write(f"Total score: {self.total}. Highest score: {self.highestScore}", align="center")

    def resetScore(self):
        self.score.clear()
        self.total = 0
        self.score.write(f"Total score: {self.total}. Highest score: {self.highestScore}", align="center")

    def drawSnake(self):
        body = turtle.Turtle()
        body.speed(0)
        body.shape("square")
        body.color("black")
        body.penup()
        self.snakeList.append(body)

    def moveSnakeBody(self):
        if len(self.snakeList) > 0:
            for i in range(len(self.snakeList) - 1, 0, -1):
                x = self.snakeList[i - 1].xcor()
                y = self.snakeList[i - 1].ycor()
                self.snakeList[i].goto(x, y)
            self.snakeList[0].goto(self.snake.xcor(), self.snake.ycor())

    def calculateDistance(self):
        self.previousDistance = self.distance
        self.distance = math.sqrt((self.snake.xcor() - self.food.xcor()) ** 2 + (self.snake.ycor() - self.food.ycor()) ** 2)

    def checkSnakeBody(self):
        if len(self.snakeList) > 1:
            for body in self.snakeList[1:]:
                if body.distance(self.snake) < 20:
                    self.resetScore()
                    return True

    def checkFood(self):
        if len(self.snakeList) > 0:
            for body in self.snakeList[:]:
                if body.distance(self.food) < 20:
                    return True

    def checkBounds(self):
        if self.snake.xcor() > (SCREENDIM / 2) or self.snake.xcor() < -(SCREENDIM / 2) or self.snake.ycor() > (SCREENDIM / 2) or self.snake.ycor() < -(SCREENDIM / 2):
            self.resetScore()
            return True

    def reset(self):
        if self.human:
            time.sleep(1)
        for body in self.snakeList:
            body.goto(1000, 1000)

        self.snakeList = []
        self.snake.goto(0, 0)
        self.snake.direction = "stop"
        self.reward = 0
        self.total = 0
        self.done = False

        state = self.getState()

        return state

    def main(self):
        rewardGiven = False
        self.screen.update()
        self.moveSnake()

        if self.newFood():
            self.reward = 10
            rewardGiven = True

        self.moveSnakeBody()
        self.calculateDistance()

        if self.checkSnakeBody():
            self.reward = -100
            rewardGiven = True
            self.done = True
            if self.human:
                self.reset()

        if self.checkBounds():
            self.reward = -100
            rewardGiven = True
            self.done = True
            if self.human:
                self.reset()

        if not rewardGiven:
            if self.distance < self.previousDistance:
                self.reward = 1
            else:
                self.reward = -1

        if self.human:
            time.sleep(0.2)
            state = self.getState()

    def step(self, action):
        if action == 0:
            self.up()
        if action == 1:
            self.right()
        if action == 2:
            self.down()
        if action == 3:
            self.left()

        self.main()
        state = self.getState()
        return state, self.reward, self.done, {}

    def getState(self):
        self.snake.x, self.snake.y = self.snake.xcor() / ROWS, self.snake.ycor() / ROWS
        self.snake.scaledX, self.snake.scaledY = self.snake.x / ROWS + 0.5, self.snake.y / ROWS + 0.5
        self.food.scaledX, self.food.scaledY = self.food.x / ROWS + 0.5, self.food.y / ROWS + 0.5

        if self.snake.y >= ROWS / 2:
            boundUp, boundDown = 1, 0
        elif self.snake.y <= -ROWS / 2:
            boundUp, boundDown = 0, 1
        else:
            boundUp, boundDown = 0, 0

        if self.snake.x >= ROWS / 2:
            boundRight, boundLeft = 1, 0
        elif self.snake.x <= -ROWS / 2:
            boundRight, boundLeft = 0, 1
        else:
            boundRight, boundLeft = 0, 0

        bodyUp, bodyRight, bodyDown, bodyLeft = [], [], [], []

        if len(self.snakeList) > 3:
            for body in self.snakeList[3:]:
                if body.distance(self.snake) == 20:
                    if body.ycor() < self.snake.ycor():
                        bodyDown.append(1)
                    elif body.ycor() > self.snake.ycor():
                        bodyUp.append(1)

                    if body.xcor() < self.snake.xcor():
                        bodyLeft.append(1)
                    elif body.xcor() > self.snake.xcor():
                        bodyRight.append(1)

        if len(bodyUp) > 0:
            bodyUp = 1
        else:
            bodyUp = 0

        if len(bodyRight) > 0:
            bodyRight = 1
        else:
            bodyRight = 0

        if len(bodyDown) > 0:
            bodyDown = 1
        else:
            bodyDown = 0

        if len(bodyLeft) > 0:
            bodyLeft = 1
        else:
            bodyLeft = 0

        if self.envInfo["state_space"] == "coordinates":
            state = [self.food.scaledX, self.food.scaledY, self.snake.scaledX, self.snake.scaledY,
                     int(boundUp or bodyUp), int(boundRight or bodyRight),
                     int(boundDown or bodyDown), int(boundLeft or bodyLeft),
                     int(self.snake.direction == "up"), int(self.snake.direction == "right"),
                     int(self.snake.direction == "down"), int(self.snake.direction == "left")]
        elif self.envInfo["state_space"] == "no direction":
            state = [int(self.snake.y < self.food.y), int(self.snake.x < self.food.x),
                     int(self.snake.y > self.food.y), int(self.snake.x > self.food.x),
                     int(boundUp or bodyUp), int(boundRight or bodyRight),
                     int(boundDown or bodyDown), int(boundLeft or bodyLeft), 0, 0, 0, 0]
        elif self.envInfo["state_space"] == "no body knowledge":
            state = [int(self.snake.y < self.food.y), int(self.snake.x < self.food.x),
                     int(self.snake.y > self.food.y), int(self.snake.x > self.food.x),
                     boundUp, boundRight, boundDown, boundLeft,
                     int(self.snake.direction == "up"), int(self.snake.direction == "right"),
                     int(self.snake.direction == "down"), int(self.snake.direction == "left")]
        else:
            state = [int(self.snake.y < self.food.y), int(self.snake.x < self.food.x),
                     int(self.snake.y > self.food.y), int(self.snake.x > self.food.x),
                     int(boundUp or bodyUp), int(boundRight or bodyRight),
                     int(boundDown or bodyDown), int(boundLeft or bodyLeft),
                     int(self.snake.direction == "up"), int(self.snake.direction == "right"),
                     int(self.snake.direction == "down"), int(self.snake.direction == "left")]
        return state

    def bye(self):
        self.screen.bye()


if __name__ == "__main__":
    human = True
    env = Environment(human=human)

    if human:
        while True:
            env.main()
