import pygame

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)


class Game:
    def __init__(self):
        super(Game, self).__init__()
        self.screenWidth = 800
        self.screenHeight = 600
        self.bodySize = 24
        self.screen = pygame.display.set_mode([self.screenWidth, self.screenHeight])
        self.surface = pygame.Surface((self.bodySize, self.bodySize))
        self.rect = self.surface.get_rect()
        self.running = True
        self.direction = 0
        self.velocity = 1
        self.window()

    def window(self):
        self.screen.fill((255, 255, 255))
        self.snake()

    def snake(self):
        self.surface.fill((0, 0, 255))

        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False

            if self.direction == 0:
                self.rect.center = (self.rect.center[0] + self.velocity, self.rect.center[1])
            elif self.direction == 1:
                self.rect.center = (self.rect.center[0] - self.velocity, self.rect.center[1])
            elif self.direction == 2:
                self.rect.center = (self.rect.center[0], self.rect.center[1] - self.velocity)
            elif self.direction == 3:
                self.rect.center = (self.rect.center[0], self.rect.center[1] + self.velocity)

            pressedKey = pygame.key.get_pressed()
            self.update(pressedKey)
            self.screen.blit(self.surface, self.rect)
            pygame.display.flip()
            self.screen.fill((255, 255, 255))

    def update(self, pressedKey):
        if pressedKey[K_RIGHT]:
            self.direction = 0
        elif pressedKey[K_LEFT]:
            self.direction = 1
        elif pressedKey[K_UP]:
            self.direction = 2
        elif pressedKey[K_DOWN]:
            self.direction = 3

        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > self.screenWidth:
            self.rect.right = self.screenWidth
        elif self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= self.screenHeight:
            self.rect.bottom = self.screenHeight


Game()
