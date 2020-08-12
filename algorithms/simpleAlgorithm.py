class SimpleAlg:
    def __init__(self, screen, snake):
        self.screen = screen
        self.snake = snake

    def findPath(self, foodLocX, foodLocY):
        if self.snake.snakeLocX < foodLocX:
            self.snake.right()
        elif self.snake.snakeLocX > foodLocX:
            self.snake.left()
        elif self.snake.snakeLocY < foodLocY:
            self.snake.down()
        elif self.snake.snakeLocY > foodLocY:
            self.snake.up()
        self.snake.snakePosition()
