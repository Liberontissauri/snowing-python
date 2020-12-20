import random
from Snowball  import Snowball
from time import sleep

class Screen:
    def __init__(self,size_x,size_y, snowball_speed):
        self.size_x = size_x
        self.size_y = size_y

        self.snowball_speed = snowball_speed

        # Generating a grid of the elements to display on the screen
        self.content = {}
        for y in range(0,size_y):
            self.content[y] = {}
            for x in range(0,size_x):
                self.content[y][x] = None

    def clear_content(self):
        self.content = {}
        for y in range(0,self.size_y):
            for x in range(0,self.size_x):
                self.content[y][x] = None

    def printScreen(self):
        print("\033c", end="") # Clearing the screen

        for y in range(0, self.size_y):
            print("\n", end="")
            for x in range(0, self.size_x):
                if self.content[y][x] == None:
                    print(" ", end="")
                else:
                    print("*", end="")

    def update(self):
        for x in range(0, self.size_x):
            for y in range(0, self.size_y):
                y = self.size_y - y
                if self.content[y-1][x] != None:
                    if y != self.size_y:
                        self.content[y][x] = Snowball(positionX=x, positionY=y)
                    self.content[y-1][x] = None

            if random.randint(0,800) == 1:
                self.content[0][x] = Snowball(positionX=x, positionY=0)
        self.printScreen()
        sleep(self.snowball_speed)
        self.update()

    def start(self):
        self.update()
