import numpy as np
import random
from algorithms.simpleAI import SimpleAI


class GeneticAlgorithm:
    def __init__(self, screen, food, snake, logic):
        self.fitness = []
        self.screen = screen
        self.food = food
        self.snake = snake
        self.logic = logic
        self.simpleAI = SimpleAI(self.screen, self.snake, self.food, self.logic)

    def calculatePopulationFitnessValue(self, population):
        fitnessTemp = []
        for i in range(population.shape[0]):
            fit = self.simpleAI.runAI(population[i])
            print(f"Chromosome {str(i)} fitness value: {fit}")
            fitnessTemp.append(fit)
        self.fitness = np.array(fitnessTemp)

    def selectBestGeneration(self, population, amountOfParents):
        parents = np.empty((amountOfParents, population.shape[1]))
        for parent in range(amountOfParents):
            maxFitnessIndex = np.where(self.fitness == np.max(self.fitness))
            maxFitnessIndex = maxFitnessIndex[0][0]
            parents[parent, :] = population[maxFitnessIndex, :]
            self.fitness[maxFitnessIndex] = -99999999
        return parents

    def crossover(self, parents, offspringSize):
        offspring = np.empty(offspringSize)
        for i in range(offspringSize[0]):
            while True:
                firstParentIndex = random.randint(0, parents.shape[0] - 1)
                secondParentIndex = random.randint(0, parents.shape[0] - 1)
                if firstParentIndex != secondParentIndex:
                    for j in range(offspringSize[1]):
                        if random.uniform(0, 1) < 0.5:
                            offspring[i, j] = parents[firstParentIndex, j]
                        else:
                            offspring[i, j] = parents[secondParentIndex, j]
                    break
        return offspring

    def mutation(self, offspringCrossover):
        global j
        for i in range(offspringCrossover.shape[0]):
            for _ in range(25):
                j = random.randint(0, offspringCrossover.shape[1] - 1)
            randomValue = np.random.choice(np.arange(-1, 1, step=0.001), size=1, replace=False)
            offspringCrossover[i, j] = offspringCrossover[i, j] + randomValue
        return offspringCrossover
