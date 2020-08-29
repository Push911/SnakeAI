from snake import Snake


class Node:
	def __init__(self, parent=None, position=None):
		self.parent = parent
		self.position = position
		self.g = 0
		self.h = 0
		self.f = 0

	def __eq__(self, other):
		return self.position == other.position


class AStar:
	def __init__(self, screen):
		self.screen = screen
		self.snake = Snake(self.screen)
		self.gridMatrix = []
		self.path = []
		self.start = ()
		self.end = ()
		self.directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

	def getStartEndPositions(self):
		for rowIndex, row in enumerate(self.gridMatrix):
			for colIndex, col in enumerate(row):
				if col is 3:
					self.start = (rowIndex, colIndex)
				if col is 1:
					self.end = (rowIndex, colIndex)

	def aStar(self):
		self.getStartEndPositions()
		startNode = Node(None, self.start)
		startNode.g = startNode.h = startNode.f = 0
		endNode = Node(None, self.end)
		endNode.g = endNode.h = endNode.f = 0
		openList = []
		closedList = []
		openList.append(startNode)

		while len(openList) > 0:
			currentNode = openList[0]
			currentNodeIndex = 0
			for index, node in enumerate(openList):
				if node.f < currentNode.f:
					currentNode = node
					currentNodeIndex = index

			openList.pop(currentNodeIndex)
			closedList.append(currentNode)

			if currentNode == endNode:
				self.path = []
				current = currentNode
				while current is not None:
					self.path.append(current.position)
					current = current.parent
				return self.path[::-1]

			children = []
			for newPosition in self.directions:
				nodePosition = (currentNode.position[0] + newPosition[0], currentNode.position[1] + newPosition[1])

				if len(self.gridMatrix) <= nodePosition[0] or len(self.gridMatrix[0]) <= nodePosition[1]:
					continue

				if len(self.gridMatrix) < nodePosition[0] < 0 or len(self.gridMatrix[0]) < nodePosition[1] < 0:
					continue

				if self.gridMatrix[nodePosition[0]][nodePosition[1]] is 2:
					continue

				newNode = Node(currentNode, nodePosition)
				children.append(newNode)

			for child in children:
				for closedChild in closedList:
					if child is closedChild:
						continue

				child.g = currentNode.g + 1
				child.h = self.distance(child, endNode)
				child.f = child.g + child.h

				for openNode in openList:
					if child is openNode and child.g > openNode.g:
						continue

				openList.append(child)

	def getCurrentLocation(self):
		self.getStartEndPositions()
		# for row in self.gridMatrix:
		# 	print(row)
		print(self.start, self.end)

	@staticmethod
	def distance(currentNode, endNode):
		return (currentNode.position[0] - endNode.position[0]) ** 2 + (currentNode.position[1] - endNode.position[1]) ** 2

	def createMatrix(self, food):
		rows = 40

		self.gridMatrix = [[0 for _ in range(rows)] for _ in range(rows)]
		print("Food loc", food.foodLocationCoordinates)
		self.gridMatrix[int(food.foodLocationCoordinates[1] / self.snake.bodySize)][int(food.foodLocationCoordinates[0] / self.snake.bodySize)] = 1
		for body in self.snake.snakeList:
			if int(self.snake.snakeList[-1][0] / self.snake.bodySize) < len(self.gridMatrix):
				if int(self.snake.snakeList[-1][1] / self.snake.bodySize) < len(self.gridMatrix):
					self.gridMatrix[int(body[1] / self.snake.bodySize)][int(body[0] / self.snake.bodySize)] = 2
					head = self.snake.snakeList[-1]
					self.gridMatrix[int(head[1] / self.snake.bodySize)][int(head[0] / self.snake.bodySize)] = 3

				if self.snake.snakeList[-1] == food.foodLocationCoordinates:
					self.snake.snakeLength += 1
					food.foodLocation()
					break
			else:
				self.snake.gameClose = True
				continue

	def move(self):
		self.getStartEndPositions()
		print(self.path)

		if len(self.path) > 1:
			pos = (self.path[0][0] - self.path[1][0], self.path[0][1] - self.path[1][1])
		else:
			pos = (0, 0)

		if pos == (0, -1):
			self.snake.left()
		elif pos == (0, 1):
			self.snake.right()
		elif pos == (-1, 0):
			self.snake.up()
		elif pos == (1, 0):
			self.snake.down()

		self.snake.snakePosition()
		print("self", self.snake.snakeList)