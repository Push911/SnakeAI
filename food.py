import pygame
import random


class Food:
    def __init__(self, screen):
        self.screen = screen
        self.radius = 5
        self.foodSize = 10
        self.foodLocationCoordinates = [0, 0]

    def newFood(self):
        pygame.draw.rect(self.screen, (255, 0, 0),
                         pygame.Rect(self.foodLocationCoordinates[0], self.foodLocationCoordinates[1],
                                     self.foodSize, self.foodSize))

    def foodLocation(self):
        self.foodLocationCoordinates = [round(random.randrange(0, self.screen.get_width()) / 10.0) * 10,
                                        round(random.randrange(0, self.screen.get_height()) / 10.0) * 10]
