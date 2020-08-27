import pygame
from food import Food
from snake import Snake
from algorithms.AstarPathfindingSnake import AStar


class Game:
    def __init__(self):
        super(Game, self).__init__()
        pygame.init()
        self.screenWidth = 800
        self.screenHeight = 800
        self.screen = pygame.display.set_mode([self.screenWidth, self.screenHeight])
        pygame.display.set_caption("Snake AI")
        self.snakeSpeed = 10
        self.clock = pygame.time.Clock()
        self.food = Food(self.screen)
        self.snake = Snake(self.screen)
        self.aStar = AStar(self.screen)
        self.gameOver = False
        self.snake.gameClose = False
        self.food.foodLocation()
        self.gameLoop()

    def board(self):
        rows = 40
        sizeBtw = self.screenWidth // rows

        self.aStar.gridMatrix = [[0 for _ in range(rows)] for _ in range(rows)]
        self.aStar.gridMatrix[int(self.food.foodLocationCoordinates[1] / self.snake.bodySize)][int(self.food.foodLocationCoordinates[0] / self.snake.bodySize)] = 1

        for body in self.snake.snakeList:
            if int(self.snake.snakeList[-1][0] / self.snake.bodySize) < len(self.aStar.gridMatrix):
                if int(self.snake.snakeList[-1][1] / self.snake.bodySize) < len(self.aStar.gridMatrix):
                    self.aStar.gridMatrix[int(body[1] / self.snake.bodySize)][int(body[0] / self.snake.bodySize)] = 2
                    head = self.snake.snakeList[-1]
                    # print(self.snake.snakeList)
                    self.aStar.gridMatrix[int(head[1] / self.snake.bodySize)][int(head[0] / self.snake.bodySize)] = 3
            else:
                self.snake.gameClose = True
                continue

        x, y = 0, 0
        for row in range(rows):
            x += sizeBtw
            y += sizeBtw
            pygame.draw.line(self.screen, (0, 0, 0), (x, 0), (x, self.screenWidth))
            pygame.draw.line(self.screen, (0, 0, 0), (0, y), (self.screenHeight, y))

    def gameLoop(self):
        while not self.gameOver:
            while self.snake.gameClose:
                self.screen.fill((255, 255, 255))
                pygame.display.update()
                self.__init__()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.gameOver = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.snake.left()
                    elif event.key == pygame.K_RIGHT:
                        self.snake.right()
                    elif event.key == pygame.K_UP:
                        self.snake.up()
                    elif event.key == pygame.K_DOWN:
                        self.snake.down()

            self.snake.snakePosition()
            print(self.snake.snakeList)
            self.aStar.getCurrentLocation()
            self.aStar.aStar()
            # self.aStar.move()
            self.food.newFood()
            print(self.aStar.path)
            self.board()
            pygame.display.update()

            if self.snake.snakeLoc[0] == self.food.foodLocationCoordinates[0] \
                    and self.snake.snakeLoc[1] == self.food.foodLocationCoordinates[1]:
                self.food.foodLocation()
                self.snake.snakeLength += 1
                self.aStar.aStar()

            self.clock.tick(self.snakeSpeed)


Game()
