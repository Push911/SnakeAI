import math

import numpy as np


class Logic:
    def __init__(self, screen, snake):
        self.screen = screen
        self.snake = snake
        # self.currentDirectionVector = []
        # self.leftDirectionVector = []
        # self.rightDirectionVector = []

    @staticmethod
    def snakeCollision(snakeLoc, snakeList):
        if snakeLoc in snakeList[1:]:
            return 1
        else:
            return 0

    @staticmethod
    def foodDistanceFromSnake(food, snakeLocation):
        return np.linalg.norm(np.array(food) - np.array(snakeLocation[0]))

    def boundsCollision(self, snakeHead):
        if snakeHead[0] >= self.screen.get_width() or snakeHead[0] < 0 or snakeHead[1] >= self.screen.get_height() \
                or snakeHead[1] < 0:
            return 1
        else:
            return 0

    def isDirectionBlocked(self, snakeList, currentDirectionVector):
        nextStep = snakeList[0] + currentDirectionVector
        if self.boundsCollision(nextStep) == 1 or self.snakeCollision(nextStep.tolist(), snakeList) == 1:
            return 1
        else:
            return 0

    def blockedDirections(self, snakeList):
        currentDirectionVector = np.array(snakeList[0]) - np.array(snakeList[1])
        leftDirectionVector = np.array([currentDirectionVector[1], -currentDirectionVector[0]])
        rightDirectionVector = np.array([-currentDirectionVector[1], currentDirectionVector[0]])

        isFrontBlocked = self.isDirectionBlocked(snakeList, currentDirectionVector)
        isLeftBlocked = self.isDirectionBlocked(snakeList, leftDirectionVector)
        isRightBlocked = self.isDirectionBlocked(snakeList, rightDirectionVector)

        return currentDirectionVector, isFrontBlocked, isLeftBlocked, isRightBlocked

    def directionVector(self, snakeLocation, direction):
        currentDirectionVector = np.array(snakeLocation[0]) - np.array(snakeLocation[1])
        leftDirectionVector = np.array([currentDirectionVector[1], - currentDirectionVector[0]])
        rightDirectionVector = np.array([-currentDirectionVector[1], currentDirectionVector[0]])

        newDirection = currentDirectionVector

        if direction == -1:
            newDirection = leftDirectionVector
        if direction == 1:
            newDirection = rightDirectionVector

        direct = self.directionToMove(newDirection)

        return direction, direct

    def directionToMove(self, newDirection):
        if newDirection.tolist() == [self.snake.bodySize, 0]:
            direction = 0
        elif newDirection.tolist() == [-self.snake.bodySize, 0]:
            direction = 1
        elif newDirection.tolist() == [0, self.snake.bodySize]:
            direction = 2
        else:
            direction = 3
        return direction

    def angleToFood(self, snakeLocation, foodLocation):
        foodDirectionVector = np.array(foodLocation) - np.array(snakeLocation[0])
        snakeDirectionVector = np.array(snakeLocation[0]) - np.array(snakeLocation[1])

        normFoodDirectionVector = np.linalg.norm(foodDirectionVector)
        normSnakeDirectionVector = np.linalg.norm(snakeDirectionVector)

        if normFoodDirectionVector == 0:
            normFoodDirectionVector = self.snake.bodySize
        if normSnakeDirectionVector == 0:
            normSnakeDirectionVector = self.snake.bodySize

        normalizedFoodDirectionVector = foodDirectionVector / normFoodDirectionVector
        normalizedSnakeDirectionVector = snakeDirectionVector / normSnakeDirectionVector

        angle = math.atan2(normalizedFoodDirectionVector[1] * normalizedSnakeDirectionVector[0] -
                           normalizedFoodDirectionVector[0] * normalizedSnakeDirectionVector[1],
                           normalizedFoodDirectionVector[1] * normalizedSnakeDirectionVector[1] +
                           normalizedFoodDirectionVector[0] * normalizedSnakeDirectionVector[0]) / math.pi

        return angle, snakeDirectionVector, normalizedFoodDirectionVector, normalizedSnakeDirectionVector
