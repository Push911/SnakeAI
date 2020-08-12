import pygame


class Snake:

    def __init__(self, screen):
        self.screen = screen
        self.bodySize = 10
        self.snakeLocX = self.screen.get_width() / 2
        self.snakeLocXchanged = 0
        self.snakeLocY = self.screen.get_height() / 2
        self.snakeLocYchanged = 0
        self.snakeLength = 1
        self.snakeList = []
        self.snakeHead = []
        self.gameClose = False

    def createSnake(self):
        for i in self.snakeList:
            pygame.draw.rect(self.screen, (0, 0, 255), [i[0], i[1], self.bodySize, self.bodySize])

    def snakePosition(self):
        self.snakeLocX += self.snakeLocXchanged
        self.snakeLocY += self.snakeLocYchanged

        self.snakeHead = [self.snakeLocX, self.snakeLocY]
        self.snakeList.append(self.snakeHead)
        if len(self.snakeList) > self.snakeLength:
            del self.snakeList[0]

        self.snakeRules()
        self.screen.fill((255, 255, 255))
        self.createSnake()

    def snakeRules(self):
        for i in self.snakeList[:-1]:
            if i == self.snakeHead:
                self.gameClose = True
        if self.snakeLocX >= self.screen.get_width() or self.snakeLocX <= 0 or self.snakeLocY >= self.screen.get_height() or self.snakeLocY <= 0:
            self.gameClose = True
        # if self.snakeLocX >= self.screen.get_width():
        #     self.snakeLocX = self.screen.get_width() - self.bodySize * len(self.snakeList)
        # elif self.snakeLocX <= 0:
        #     self.snakeLocX = 0 + self.bodySize * len(self.snakeList)
        # elif self.snakeLocY >= self.screen.get_height():
        #     self.snakeLocY = self.screen.get_height() - self.bodySize * len(self.snakeList)
        # elif self.snakeLocY <= 0:
        #     self.snakeLocY = 0 + self.bodySize * len(self.snakeList)

    def left(self):
        self.snakeLocXchanged = -self.bodySize
        self.snakeLocYchanged = 0

    def right(self):
        self.snakeLocXchanged = self.bodySize
        self.snakeLocYchanged = 0

    def up(self):
        self.snakeLocXchanged = 0
        self.snakeLocYchanged = -self.bodySize

    def down(self):
        print("sd")
        self.snakeLocXchanged = 0
        self.snakeLocYchanged = self.bodySize
