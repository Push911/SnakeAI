import pygame


class Snake:
    def __init__(self, screen):
        self.screen = screen
        self.bodySize = 10
        self.snakeLocX = self.screen.get_width() / 2
        self.snakeLocXchanged = 0
        self.snakeLocY = self.screen.get_height() / 2
        self.snakeLocYchanged = 0
        self.snakeSpeed = 15
        self.snakeLength = 1
        self.snakeList = []

    def createSnake(self, size, snakeList):
        for i in snakeList:
            pygame.draw.rect(self.screen, (0, 0, 255), [i[0], i[1], size, size])

    def snakePosition(self):
        self.snakeLocX += self.snakeLocXchanged
        self.snakeLocY += self.snakeLocYchanged

    def snakeRules(self):
        if self.snakeLocX >= self.screen.get_width():
            self.snakeLocX = self.screen.get_width() - self.bodySize
        elif self.snakeLocX < 0:
            self.snakeLocX = 0
        elif self.snakeLocY >= self.screen.get_height():
            self.snakeLocY = self.screen.get_height() - self.bodySize
        elif self.snakeLocY <= 0:
            self.snakeLocY = 0
#     def snake(self):
#         while self.running:
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     self.running = False
#
#                 if event.type == pygame.KEYDOWN:
#                     if event.key == pygame.K_LEFT:
#                         self.snakeLocXchanged = -self.bodySize
#                         self.snakeLocYchanged = 0
#                     elif event.key == pygame.K_RIGHT:
#                         self.snakeLocXchanged = self.bodySize
#                         self.snakeLocYchanged = 0
#                     elif event.key == pygame.K_UP:
#                         self.snakeLocXchanged = 0
#                         self.snakeLocYchanged = -self.bodySize
#                     elif event.key == pygame.K_DOWN:
#                         self.snakeLocXchanged = 0
#                         self.snakeLocYchanged = self.bodySize
#
#             self.snakeLocX += self.snakeLocXchanged
#             self.snakeLocY += self.snakeLocYchanged
#
#             if self.snakeLocX >= self.screenWidth:
#                 self.snakeLocX = self.screenWidth - self.bodySize
#             elif self.snakeLocX < 0:
#                 self.snakeLocX = 0
#             elif self.snakeLocY >= self.screenHeight:
#                 self.snakeLocY = self.screenHeight - self.bodySize
#             elif self.snakeLocY <= 0:
#                 self.snakeLocY = 0
#
#             self.screen.fill((255, 255, 255))
#             pygame.draw.rect(self.screen, (0, 0, 255), [self.snakeLocX, self.snakeLocY, self.bodySize, self.bodySize])
#             self.food.newFood()
#             pygame.display.update()
#             if self.snakeLocX == self.food.foodLocationX and self.snakeLocY == self.food.foodLocationY:
#                 self.food.foodLocation()
#                 self.snakeLength += 1
#             self.clock.tick(self.snakeSpeed)
#
#
# Game()
