import pygame
from food import Food
from snake import Snake
from algorithms.BreadthFirstSearchSnake import BFS


class Game:
    def __init__(self):
        super(Game, self).__init__()
        pygame.init()
        self.screenWidth = 800
        self.screenHeight = 800
        self.screen = pygame.display.set_mode([self.screenWidth, self.screenHeight])
        pygame.display.set_caption("Snake AI")
        self.snakeSpeed = 100
        self.clock = pygame.time.Clock()
        self.food = Food(self.screen)
        self.snake = Snake(self.screen)
        # self.aStar = AStar(self.screen)
        self.bfs = BFS(self.screen, self.food, self.snake)
        self.gameOver = False
        self.snake.gameClose = False
        self.food.foodLocation()
        self.gameLoop()

    def board(self):
        rows = 40
        sizeBtw = self.screenWidth // rows

        # self.aStar.createMatrix(self.food)
        self.bfs.createMatrix()

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
            # self.aStar.getCurrentLocation()
            # self.aStar.aStar()
            # self.aStar.move()
            self.bfs.getCurrentLocation()
            self.bfs.bfs()
            self.board()
            self.food.newFood()

            pygame.display.update()

            self.clock.tick(self.snakeSpeed)


Game()
