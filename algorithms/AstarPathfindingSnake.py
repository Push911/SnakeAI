from snake import Snake
from food import Food


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
		self.food = Food(self.screen)
		self.snake = Snake(self.screen)
		self.gridMatrix = []
		self.path = []
		self.start = ()
		self.end = ()
		self.directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

	def getStartEndPositions(self):
		# for row in self.gridMatrix:
		# 	print(row)
		for rowIndex, row in enumerate(self.gridMatrix):
			for colIndex, col in enumerate(row):
				if col is 3:
					self.start = (rowIndex, colIndex)
					print(self.start)
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

	def move(self):
		print(self.start, self.end)
		# self.getStartEndPositions()
		# print(self.path)
		if len(self.path) > 1:
			pos = (self.path[-1][0] - self.path[-2][0], self.path[-1][1] - self.path[-2][1])
		else:
			pos = (0, 0)

		if pos == (-1, 0):
			self.snake.left()
		elif pos == (1, 0):
			self.snake.right()
		elif pos == (0, -1):
			self.snake.up()
		elif pos == (0, 1):
			self.snake.down()

		self.snake.snakePosition()
		# self.path.pop(-1)
		print(pos)
