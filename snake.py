import pygame


class Snake:
    def __init__(self, screen):
        self.screen = screen
        self.bodySize = 20
        self.snakeLoc = [self.screen.get_width() / 2, self.screen.get_height() / 2]
        self.snakeLocXchanged = 0
        self.snakeLocYchanged = 0
        self.currentDirectionVector = 0
        self.leftDirectionVector = 0
        self.rightDirectionVector = 0
        self.snakeLength = 1
        self.snakeList = []
        self.snakeHead = []
        self.steps = 100
        self.gameClose = False

    def createSnake(self):
        for i in self.snakeList:
            pygame.draw.rect(self.screen, (0, 0, 255), [i[0], i[1], self.bodySize, self.bodySize])

    def snakePosition(self):
        self.snakeLoc[0] += self.snakeLocXchanged
        self.snakeLoc[1] += self.snakeLocYchanged
        self.snakeHead = [self.snakeLoc[0], self.snakeLoc[1]]
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

        if self.snakeLoc[0] >= self.screen.get_width() or self.snakeLoc[0] <= 0 or self.snakeLoc[1] >= self.screen.get_height() or self.snakeLoc[1] <= 0:
            self.gameClose = True

    def left(self):
        print("LEFT")
        self.snakeLocXchanged = -self.bodySize
        self.snakeLocYchanged = 0

    def right(self):
        print("RIGHT")
        self.snakeLocXchanged = self.bodySize
        self.snakeLocYchanged = 0

    def up(self):
        print("UP")
        self.snakeLocXchanged = 0
        self.snakeLocYchanged = -self.bodySize

    def down(self):
        print("DOWN")
        self.snakeLocXchanged = 0
        self.snakeLocYchanged = self.bodySize
