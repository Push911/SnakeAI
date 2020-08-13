import pygame
from food import Food
from snake import Snake
from algorithms.simpleAlgorithm import SimpleAlg


class Game:
    def __init__(self):
        super(Game, self).__init__()
        self.screenWidth = 800
        self.screenHeight = 600
        self.screen = pygame.display.set_mode([self.screenWidth, self.screenHeight])
        pygame.display.set_caption("Snake AI")
        self.bodySize = 10
        self.snakeSpeed = 100
        self.gameOver = False
        self.clock = pygame.time.Clock()
        self.food = Food(self.screen)
        self.snake = Snake(self.screen)
        self.algorithm = SimpleAlg(self.screen, self.snake)
        self.gameLoop()

    def gameLoop(self):
        self.gameOver = False
        self.snake.gameClose = False
        self.food = Food(self.screen)
        self.snake = Snake(self.screen)
        self.algorithm = SimpleAlg(self.screen, self.snake)
        self.food.foodLocation()
        while not self.gameOver:
            while self.snake.gameClose:
                self.screen.fill((255, 255, 255))
                pygame.display.update()
                self.gameLoop()
                # for event in pygame.event.get():
                #     if event.type == pygame.KEYDOWN:
                #         if event.key == pygame.K_q:
                #             self.snake.gameClose = False
                #             self.gameOver = True
                #         if event.key == pygame.K_c:
                #             self.gameLoop()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.gameOver = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.snake.left()
                    elif event.key == pygame.K_RIGHT:
                        self.snake.right()
                    elif event.key == pygame.K_UP:
                        self.snake.up()
                    elif event.key == pygame.K_DOWN:
                        self.snake.down()

            self.algorithm.findPath(self.food.foodLocationX, self.food.foodLocationY)
            self.food.newFood()
            pygame.display.update()

            if self.snake.snakeLocX == self.food.foodLocationX and self.snake.snakeLocY == self.food.foodLocationY:
                self.food.foodLocation()
                self.snake.snakeLength += 1

            self.clock.tick(self.snakeSpeed)


Game()
