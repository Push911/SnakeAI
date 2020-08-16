import pygame
import numpy as np
from food import Food
from snake import Snake
from gameLogic import Logic
from geneticAlgorithm import GeneticAlgorithm
# from algorithms.simpleAlgorithm import SimpleAlg
from algorithms.simpleAI import SimpleAI


class Game:
    def __init__(self):
        super(Game, self).__init__()
        self.screenWidth = 800
        self.screenHeight = 600
        self.screen = pygame.display.set_mode([self.screenWidth, self.screenHeight])
        pygame.display.set_caption("Snake AI")
        self.bodySize = 10
        self.snakeSpeed = 200
        self.gameOver = False
        self.clock = pygame.time.Clock()
        self.food = Food(self.screen)
        self.snake = Snake(self.screen)
        self.logic = Logic(self.screen, self.snake)
        self.geneticAlg = GeneticAlgorithm(self.screen, self.food, self.snake, self.logic)
        # self.algorithm = SimpleAlg(self.screen, self.snake)
        self.simpleAi = SimpleAI(self.screen, self.snake, self.food, self.logic)
        self.snake.gameClose = False
        self.food.foodLocation()
        self.gameLoop()

    def gameLoop(self):
        populationChromosomes = 50
        weightsAmount = self.simpleAi.inputLayerNeurons * self.simpleAi.firstHiddenLayerNeurons + \
                             self.simpleAi.firstHiddenLayerNeurons * self.simpleAi.secondHiddenLayerNeurons + \
                             self.simpleAi.secondHiddenLayerNeurons * self.simpleAi.outputLayerNeurons
        populationSize = (populationChromosomes, weightsAmount)
        newPopulation = np.random.choice(np.arange(-1, 1, step=0.01), size=populationSize, replace=True)
        generations = 100
        matingParentsAmount = 12
        for generation in range(generations):
            # print(newPopulation[0])
            self.geneticAlg.fitness = self.geneticAlg.calculatePopulationFitnessValue(newPopulation)
            parents = self.geneticAlg.selectBestGeneration(newPopulation, matingParentsAmount)
            offspringCrossover = self.geneticAlg.crossover(parents,
                                                           offspringSize=(populationSize[0] -
                                                                          parents.shape[0], weightsAmount))
            offspringMutation = self.geneticAlg.mutation(offspringCrossover)
            newPopulation[0:parents.shape[0], :] = parents
            newPopulation[parents.shape[0]:, :] = offspringMutation
        # while not self.gameOver:
        #     while self.snake.gameClose:
        #         self.screen.fill((255, 255, 255))
        #         pygame.display.update()
        #         self.__init__()
        #         # self.gameLoop()
        #         # for event in pygame.event.get():
        #         #     if event.type == pygame.KEYDOWN:
        #         #         if event.key == pygame.K_q:
        #         #             self.snake.gameClose = False
        #         #             self.gameOver = True
        #         #         if event.key == pygame.K_c:
        #         #             self.gameLoop()
        #
        #     for event in pygame.event.get():
        #         if event.type == pygame.QUIT:
        #             self.gameOver = True
        #
        #         if event.type == pygame.KEYDOWN:
        #             if event.key == pygame.K_LEFT:
        #                 self.snake.left()
        #             elif event.key == pygame.K_RIGHT:
        #                 self.snake.right()
        #             elif event.key == pygame.K_UP:
        #                 self.snake.up()
        #             elif event.key == pygame.K_DOWN:
        #                 self.snake.down()
        #
        #     # self.algorithm.findPath(self.food.foodLocationCoordinates)
        #     self.food.newFood()
        #     # print(self.logic.blockedDirections())
        #     pygame.display.update()
        #
        #     if self.snake.snakeLoc[0] == self.food.foodLocationCoordinates[0] \
        #             and self.snake.snakeLoc[1] == self.food.foodLocationCoordinates[1]:
        #         self.food.foodLocation()
        #         # self.snake.steps = 0
        #         self.snake.snakeLength += 1
        #
        #     self.clock.tick(self.snakeSpeed)


Game()
