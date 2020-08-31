import numpy as np

""" 0: Left
	1: Right
	2: Up
	3: Down"""


class ReinforcementLearning:
	def __init__(self, screen, snake, food):
		self.screen = screen
		self.food = food
		self.snake = snake
		self.distance = 0
		self.gridMatrix = []
		self.foodLocation = []
		self.snakeHeadLocation = []
		self.distance = 0
		self.score = 0
		self.epsilon = 0.7
		self.rows = 40
		self.qTable = np.zeros((self.rows ** 2, 4))
		self.state = 0
		self.action = 0
		self.done = False

	def reward(self):
		self.createMatrix()

		if self.distance < self.calculateDistance():
			self.score -= 1
		elif self.distance > self.calculateDistance():
			self.score += 1

		if self.calculateDistance() is 0:
			self.score += 100
			self.snake.snakeLength += 1
			self.food.foodLocation()

		self.distance = self.calculateDistance()

	def getCurrentLocations(self):
		self.foodLocation = [int(self.food.foodLocationCoordinates[0] / self.snake.bodySize),
		                     int(self.food.foodLocationCoordinates[1] / self.snake.bodySize)]
		self.snakeHeadLocation = [int(self.snake.snakeList[-1][0] / self.snake.bodySize),
		                          int(self.snake.snakeList[-1][1] / self.snake.bodySize)]

	def calculateDistance(self):
		self.getCurrentLocations()
		return (self.snakeHeadLocation[0] - self.foodLocation[0]) ** 2 + \
		       (self.snakeHeadLocation[1] - self.foodLocation[1]) ** 2

	def createMatrix(self):
		self.getCurrentLocations()
		self.gridMatrix = [[0 for _ in range(self.rows)] for _ in range(self.rows)]

		for body in self.snake.snakeList[:-1]:
			if self.screen.get_width() <= self.snake.snakeList[-1][0]:
				print(self.snake.snakeList[-1][0], self.screen.get_width())
				self.snake.gameClose = True
				self.score = -1
				break
			elif self.screen.get_height() <= self.snake.snakeList[-1][1]:
				self.snake.gameClose = True
				self.score = -1
				break

			body = [int(body[0] / self.snake.bodySize), int(body[1] / self.snake.bodySize)]
			self.gridMatrix[body[0]][body[1]] = 2

			self.gridMatrix[self.snakeHeadLocation[0]][self.snakeHeadLocation[1]] = 3

			self.gridMatrix[self.foodLocation[0]][self.foodLocation[1]] = 1

	def step(self):
		self.snake.move(self.action)
		self.reward()

	def epsilonGreedyPolicy(self):
		if np.random.uniform(0, 1) > self.epsilon:
			self.action = np.argmax(self.qTable[self.state])
		else:
			self.action = np.random.randint(4)

	def qLearning(self):
		# self.state = 0
		self.epsilonGreedyPolicy()
