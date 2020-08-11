import pygame
import random


class Food:
    def __init__(self, screen):
        self.screen = screen
        self.radius = 5
        self.foodLocationX = 0
        self.foodLocationY = 0

    def newFood(self):
        pygame.draw.circle(self.screen, (255, 0, 0), (self.foodLocationX, self.foodLocationY), self.radius)

    def foodLocation(self):
        self.foodLocationX = round(random.randrange(0, self.screen.get_width() - 2 * self.radius) / 10.0) * 10
        self.foodLocationY = round(random.randrange(0, self.screen.get_height() - 2 * self.radius) / 10.0) * 10
