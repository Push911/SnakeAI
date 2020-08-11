import pygame
from food import Food
from snake import Snake


class Game:
    def __init__(self):
        super(Game, self).__init__()
        self.screenWidth = 800
        self.screenHeight = 600
        self.bodySize = 10
        self.screen = pygame.display.set_mode([self.screenWidth, self.screenHeight])
        pygame.display.set_caption("Snake AI")
        self.running = True
        self.clock = pygame.time.Clock()
        self.snakeSpeed = 15
        self.food = Food(self.screen)
        self.snakeLength = 1
        self.snakeList = []
        self.sn = Snake(self.screen)
        self.snake()

    def snake(self):
        self.food.foodLocation()
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.sn.snakeLocXchanged = -self.sn.bodySize
                        self.sn.snakeLocYchanged = 0
                    elif event.key == pygame.K_RIGHT:
                        self.sn.snakeLocXchanged = self.sn.bodySize
                        self.sn.snakeLocYchanged = 0
                    elif event.key == pygame.K_UP:
                        self.sn.snakeLocXchanged = 0
                        self.sn.snakeLocYchanged = -self.sn.bodySize
                    elif event.key == pygame.K_DOWN:
                        self.sn.snakeLocXchanged = 0
                        self.sn.snakeLocYchanged = self.sn.bodySize

            self.sn.snakePosition()
            self.sn.snakeRules()

            self.screen.fill((255, 255, 255))
            snakeHead = [self.sn.snakeLocX, self.sn.snakeLocY]
            self.snakeList.append(snakeHead)
            if len(self.snakeList) > self.snakeLength:
                del self.snakeList[0]

            self.sn.createSnake(self.sn.bodySize, self.snakeList)
            # for i in self.snakeList[:-1]:
            #     if i == snakeHead:
            #         self.running = False

            self.food.newFood()
            pygame.display.update()
            if self.sn.snakeLocX == self.food.foodLocationX and self.sn.snakeLocY == self.food.foodLocationY:
                self.food.foodLocation()
                self.snakeLength += 1
            self.clock.tick(self.snakeSpeed)


Game()
