import pygame
from food import Food


class Game:
    def __init__(self):
        super(Game, self).__init__()
        self.screenWidth = 800
        self.screenHeight = 600
        self.bodySize = 10
        self.screen = pygame.display.set_mode([self.screenWidth, self.screenHeight])
        self.running = True
        self.snakeLocX = self.screenWidth / 2
        self.snakeLocXchanged = 0
        self.snakeLocY = self.screenHeight / 2
        self.snakeLocYchanged = 0
        self.clock = pygame.time.Clock()
        self.snakeSpeed = 15
        self.food = Food(self.screen)
        self.snake()

    def snake(self):
        self.food.foodLocation()
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.snakeLocXchanged = -self.bodySize
                        self.snakeLocYchanged = 0
                    elif event.key == pygame.K_RIGHT:
                        self.snakeLocXchanged = self.bodySize
                        self.snakeLocYchanged = 0
                    elif event.key == pygame.K_UP:
                        self.snakeLocXchanged = 0
                        self.snakeLocYchanged = -self.bodySize
                    elif event.key == pygame.K_DOWN:
                        self.snakeLocXchanged = 0
                        self.snakeLocYchanged = self.bodySize

            self.snakeLocX += self.snakeLocXchanged
            self.snakeLocY += self.snakeLocYchanged

            if self.snakeLocX >= self.screenWidth:
                self.snakeLocX = self.screenWidth - self.bodySize
            elif self.snakeLocX < 0:
                self.snakeLocX = 0
            elif self.snakeLocY >= self.screenHeight:
                self.snakeLocY = self.screenHeight - self.bodySize
            elif self.snakeLocY <= 0:
                self.snakeLocY = 0

            self.screen.fill((255, 255, 255))
            pygame.draw.rect(self.screen, (0, 0, 255), [self.snakeLocX, self.snakeLocY, self.bodySize, self.bodySize])
            self.food.newFood()
            pygame.display.update()
            if self.snakeLocX == self.food.foodLocationX and self.snakeLocY == self.food.foodLocationY:
                self.food.foodLocation()
            self.clock.tick(self.snakeSpeed)


Game()
