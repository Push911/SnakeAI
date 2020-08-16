import numpy as np


class SimpleAI:
    def __init__(self, screen, snake, food, logic):
        self.direction = [0, 1, 2, 3]
        self.screen = screen
        self.snake = snake
        self.food = food
        self.logic = logic
        self.score = 0
        self.score2 = 0
        self.scoreMax = 0
        self.inputLayerNeurons = 7
        self.firstHiddenLayerNeurons = 9
        self.secondHiddenLayerNeurons = 15
        self.outputLayerNeurons = 3
        self.weights1Shape = (self.firstHiddenLayerNeurons, self.inputLayerNeurons)
        self.weights2Shape = (self.secondHiddenLayerNeurons, self.firstHiddenLayerNeurons)
        self.weights3Shape = (self.outputLayerNeurons, self.secondHiddenLayerNeurons)

    @staticmethod
    def softmax(n):
        return np.exp(n.T) / np.sum(np.exp(n.T), axis=1).reshape(-1, 1)

    @staticmethod
    def sigmoid(n):
        return 1 / (1 - np.exp(-n))

    def initializeWeights(self, weights):
        weights1 = weights[0:self.weights1Shape[0] * self.weights1Shape[1]]
        weights2 = weights[self.weights1Shape[0] * self.weights1Shape[1]:self.weights2Shape[0] * self.weights2Shape[1] +
                           self.weights1Shape[0] * self.weights1Shape[1]]
        weights3 = weights[
                   self.weights2Shape[0] * self.weights2Shape[1] + self.weights1Shape[0] * self.weights1Shape[1]:]
        return (weights1.reshape(self.weights1Shape[0], self.weights1Shape[1]),
                weights2.reshape(self.weights2Shape[0], self.weights2Shape[1]),
                weights3.reshape(self.weights3Shape[0], self.weights3Shape[1]))

    def forwardPropagation(self, matrix, weights):
        weights1, weights2, weights3 = self.initializeWeights(weights)

        weightsOfInputLayer = np.matmul(weights1, matrix.T)
        nodesOfInputLayer = np.tanh(weightsOfInputLayer)
        weightsOfHiddenLayer = np.matmul(weights2, nodesOfInputLayer)
        nodesOfHiddenLayer = np.tanh(weightsOfHiddenLayer)
        weightsOfOutputLayer = np.matmul(weights3, nodesOfHiddenLayer)
        nodesOfOutputLayer = np.tanh(weightsOfOutputLayer)
        return nodesOfOutputLayer

    def runAI(self, weights):
        for _ in range(1):
            countSameDirection = 0
            previousDirection = 0
            for _ in range(200):  # redo with self.snake.steps
                currentDirectionVector, isFrontBlocked, isLeftBlocked, isRightBlocked = self.logic.blockedDirections()
                angle, snakeDirectionVector, normalizedFoodDirectionVector, normalizedSnakeDirectionVector = \
                    self.logic.angleToFood(self.snake.snakeList, self.food.foodLocationCoordinates)
                predictedDirection = np.argmax(
                    np.array(self.forwardPropagation(np.array([isLeftBlocked, isFrontBlocked, isRightBlocked,
                                                               normalizedFoodDirectionVector[0],
                                                               normalizedSnakeDirectionVector[0],
                                                               normalizedFoodDirectionVector[1],
                                                               normalizedSnakeDirectionVector[1]]).reshape(-1, 7),
                                                     weights))) - 1

                if predictedDirection == previousDirection:
                    countSameDirection += 1
                else:
                    countSameDirection = 0
                    previousDirection = predictedDirection

                newDirection = np.array(self.snake.snakeList[0]) - np.array(self.snake.snakeList[1])
                if predictedDirection == -1:
                    newDirection = np.array([newDirection[1], -newDirection[0]])
                if predictedDirection == 1:
                    newDirection = np.array([-newDirection[1], newDirection[0]])

                directionToMove = self.logic.directionToMove(newDirection)
                nextStep = self.snake.snakeList[0] + currentDirectionVector

                if self.logic.boundsCollision(self.snake.snakeList[0]) == 1 \
                        or self.logic.snakeCollision(nextStep.tolist()) == 1:
                    self.score += 150
                    break
                else:
                    self.score = 0

                # self.snake.snakeList, self.food.foodLocationCoordinates, score = game()
                if self.score > self.scoreMax:
                    self.scoreMax = self.score

                if countSameDirection > 8 and predictedDirection != 0:
                    self.score2 -= 1
                else:
                    self.score2 += 2

        return self.score + self.score2 * 5000
