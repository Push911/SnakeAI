class SimpleAlg:
    def __init__(self, screen, snake):
        self.screen = screen
        self.snake = snake
        self.direction = 0

    def findPath(self, foodLocX, foodLocY):
        if self.snake.snakeLocX < foodLocX:
            self.direction = 0
        if self.snake.snakeLocX > foodLocX:
            self.direction = 1
        if self.snake.snakeLocY < foodLocY:
            self.direction = 2
        if self.snake.snakeLocY > foodLocY:
            self.direction = 3
        self.rules()

    def rules(self):
        self.bounds()
        self.possibleMoves()
        self.move()

    def possibleMoves(self):
        if self.direction is 0 and self.snake.snakeLocX + self.snake.bodySize not in \
                [snakePos[0] for snakePos in self.snake.snakeList]:
            self.direction = 0
        elif self.direction is 1 and self.snake.snakeLocX - self.snake.bodySize not in \
                [snakePos[0] for snakePos in self.snake.snakeList]:
            self.direction = 1
        elif self.direction is 2 and self.snake.snakeLocY + self.snake.bodySize not in \
                [snakePos[1] for snakePos in self.snake.snakeList]:
            self.direction = 2
        elif self.direction is 3 and self.snake.snakeLocY - self.snake.bodySize not in \
                [snakePos[1] for snakePos in self.snake.snakeList]:
            self.direction = 3
        else:
            self.direction += 1
            if self.direction is 4:
                self.direction = 0
            self.rules()
        self.bounds()

    def bounds(self):
        if self.direction is 0 and self.snake.snakeLocX + self.snake.bodySize == self.screen.get_width():
            self.direction += 1
        elif self.direction is 1 and self.snake.snakeLocX - self.snake.bodySize == 0:
            self.direction += 1
        elif self.direction is 2 and self.snake.snakeLocY + self.snake.bodySize == self.screen.get_height():
            self.direction += 1
        elif self.direction is 3 and self.snake.snakeLocY - self.snake.bodySize == 0:
            self.direction = 0

    def move(self):
        if self.direction is 0:
            self.snake.right()
        elif self.direction is 1:
            self.snake.left()
        elif self.direction is 2:
            self.snake.down()
        elif self.direction is 3:
            self.snake.up()
        self.snake.snakePosition()
