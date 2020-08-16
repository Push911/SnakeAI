from gameLogic import Logic


class SimpleAlg:
    def __init__(self, screen, snake):
        self.screen = screen
        self.snake = snake
        self.logic = Logic(self.screen, self.snake)
        self.direction = 0

    def findPath(self, foodLoc):
        if self.snake.snakeLoc[0] < foodLoc[0]:
            self.direction = 0
        if self.snake.snakeLoc[0] > foodLoc[0]:
            self.direction = 1
        if self.snake.snakeLoc[1] < foodLoc[1]:
            self.direction = 2
        if self.snake.snakeLoc[1] > foodLoc[1]:
            self.direction = 3
        self.rules()

    def rules(self):
        self.bounds()
        self.possibleMoves()
        self.move()

    def possibleMoves(self):
        if self.direction is 0 and self.snake.snakeLoc[0] + self.snake.bodySize not in \
                [snakePos[0] for snakePos in self.snake.snakeList]:
            self.direction = 0
        elif self.direction is 1 and self.snake.snakeLoc[0] - self.snake.bodySize not in \
                [snakePos[0] for snakePos in self.snake.snakeList]:
            self.direction = 1

        elif self.direction is 2 and self.snake.snakeLoc[1] + self.snake.bodySize not in \
                [snakePos[1] for snakePos in self.snake.snakeList]:
            self.direction = 2
        elif self.direction is 3 and self.snake.snakeLoc[1] - self.snake.bodySize not in \
                [snakePos[1] for snakePos in self.snake.snakeList]:
            self.direction = 3
        else:
            self.direction += 1
            if self.direction is 4:
                self.direction = 0
            self.possibleMoves()
        self.bounds()

    def bounds(self):
        if self.direction is 0 and self.snake.snakeLoc[0] + self.snake.bodySize == self.screen.get_width():
            self.direction += 1
        elif self.direction is 1 and self.snake.snakeLoc[0] - self.snake.bodySize == 0:
            self.direction += 1
        elif self.direction is 2 and self.snake.snakeLoc[1] + self.snake.bodySize == self.screen.get_height():
            self.direction += 1
        elif self.direction is 3 and self.snake.snakeLoc[1] - self.snake.bodySize == 0:
            self.direction = 0

    def move(self):
        # self.snake.steps += 1
        if self.direction is 0:
            self.snake.right()
        elif self.direction is 1:
            self.snake.left()
        elif self.direction is 2:
            self.snake.down()
        elif self.direction is 3:
            self.snake.up()
        self.snake.snakePosition()
