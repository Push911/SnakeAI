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

	def reward(self):
		self.createMatrix()

		# for row in self.gridMatrix:
		# 	print(row)

		if self.distance < self.calculateDistance():
			self.score -= 1
		elif self.distance > self.calculateDistance():
			self.score += 1

		self.distance = self.calculateDistance()
		print(self.score)

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
		rows = 40
		self.getCurrentLocations()
		self.gridMatrix = [[0 for _ in range(rows)] for _ in range(rows)]

		for body in self.snake.snakeList[:-1]:
			body = [int(body[0] / self.snake.bodySize), int(body[1] / self.snake.bodySize)]
			self.gridMatrix[body[0]][body[1]] = 2

		self.gridMatrix[self.snakeHeadLocation[0]][self.snakeHeadLocation[1]] = 3

		self.gridMatrix[self.foodLocation[0]][self.foodLocation[1]] = 1
