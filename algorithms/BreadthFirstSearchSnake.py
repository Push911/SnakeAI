import queue


class BFS:
	def __init__(self, screen, food, snake):
		self.screen = screen
		self.snake = snake
		self.food = food
		self.gridMatrix = []
		self.path = []
		self.start = []
		self.end = []
		self.directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

	def getStartEndPositions(self):
		for rowIndex, row in enumerate(self.gridMatrix):
			for colIndex, col in enumerate(row):
				if col is 3:
					self.start = [rowIndex, colIndex]
				if col is 1:
					self.end = [rowIndex, colIndex]

	def moveIsValid(self, moves):
		self.getStartEndPositions()
		currentPosition = self.start

		for move in moves:
			if move is "L":
				currentPosition[1] -= 1
			elif move is "R":
				currentPosition[1] += 1
			elif move is "U":
				currentPosition[0] -= 1
			elif move is "D":
				currentPosition[0] += 1

			if not (0 <= currentPosition[1] < len(self.gridMatrix[0]) and 0 <= currentPosition[0] < len(self.gridMatrix)):
				return False
			elif self.gridMatrix[currentPosition[0]][currentPosition[1]] is 2:
				return False

		return True

	def findEnd(self, moves):
		self.getStartEndPositions()
		currentPosition = self.start

		for move in moves:
			if move is "L":
				currentPosition[1] -= 1
			elif move is "R":
				currentPosition[1] += 1
			elif move is "U":
				currentPosition[0] -= 1
			elif move is "D":
				currentPosition[0] += 1

		if currentPosition == self.end:
			print("Found: ", moves)
			self.printMatrix(moves)
			return True

		return False

	def printMatrix(self, moves):
		self.getStartEndPositions()
		currentPosition = self.start

		for move in moves:
			if move is "L":
				currentPosition[1] -= 1
			elif move is "R":
				currentPosition[1] += 1
			elif move is "U":
				currentPosition[0] -= 1
			elif move is "D":
				currentPosition[0] += 1

			if self.gridMatrix[currentPosition[0]][currentPosition[1]] is not 3:
				if self.gridMatrix[currentPosition[0]][currentPosition[1]] is not 1:
					self.gridMatrix[currentPosition[0]][currentPosition[1]] = "+"

		for row in self.gridMatrix:
			print(row)

	def bfs(self):
		path = queue.Queue()
		path.put("")
		add = ""
		while not self.findEnd(add):
			add = path.get()
			for direction in ["L", "R", "U", "D"]:
				tried = add + direction
				print(tried)
				if self.moveIsValid(tried):
					path.put(tried)

	def getCurrentLocation(self):
		self.getStartEndPositions()
		# for row in self.gridMatrix:
		# 	print(row)
		print(self.start, self.end)

	def createMatrix(self):
		rows = 40
		self.getCurrentLocation()
		self.gridMatrix = [[0 for _ in range(rows)] for _ in range(rows)]
		print(self.snake.snakeList)
		print("Food loc", self.food.foodLocationCoordinates)
		self.gridMatrix[int(self.food.foodLocationCoordinates[1] / self.snake.bodySize)][int(self.food.foodLocationCoordinates[0] / self.snake.bodySize)] = 1

		for body in self.snake.snakeList:
			if int(self.snake.snakeList[-1][0] / self.snake.bodySize) < len(self.gridMatrix):
				if int(self.snake.snakeList[-1][1] / self.snake.bodySize) < len(self.gridMatrix):
					self.gridMatrix[int(body[1] / self.snake.bodySize)][int(body[0] / self.snake.bodySize)] = 2
					head = self.snake.snakeList[-1]
					self.gridMatrix[int(head[1] / self.snake.bodySize)][int(head[0] / self.snake.bodySize)] = 3

				if self.snake.snakeList[-1] == self.food.foodLocationCoordinates:
					self.snake.snakeLength += 1
					self.food.foodLocation()
					break
			else:
				self.snake.gameClose = True
				continue

# def move(self):
# 	self.getStartEndPositions()
# 	print(self.path)
#
# 	if len(self.path) > 1:
# 		pos = (self.path[0][0] - self.path[1][0], self.path[0][1] - self.path[1][1])
# 	else:
# 		pos = (0, 0)
#
# 	if pos == (0, -1):
# 		self.snake.left()
# 	elif pos == (0, 1):
# 		self.snake.right()
# 	elif pos == (-1, 0):
# 		self.snake.up()
# 	elif pos == (1, 0):
# 		self.snake.down()
#
# 	self.snake.snakePosition()
# 	print("self", self.snake.snakeList)
