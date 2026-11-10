import pygame
import random

pygame.init()

# Dimensions of the screen
WIDTH, HEIGHT = 600, 500
 
# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (135, 206, 235)
RED = (255, 0, 0)
NAVY_BLUE = (0, 0, 128)
font = pygame.font.Font('freesansbold.ttf', 15)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Block Breaker")

# to control the frame rate
clock = pygame.time.Clock()
FPS = 30
# Striker class
class Striker:
    def _init_(self, posx, posy, width, height, speed, color):
        self.posx, self.posy = posx, posy
        self.width, self.height = width, height
        self.speed = speed
        self.color = color

        # The rect variable is used to handle the placement
        # and the collisions of the object
        self.strikerRect = pygame.Rect(
            self.posx, self.posy, self.width, self.height)
        self.striker = pygame.draw.rect(screen, 
                               self.color, self.strikerRect)

    # Used to render the object on the screen
    def display(self):
        self.striker = pygame.draw.rect(screen, 
                            self.color, self.strikerRect)

    # Used to update the state of the object
    def update(self, xFac):
        self.posx += self.speed*xFac

        # Restricting the striker to be in between the 
        # left and right edges of the screen
        if self.posx <= 0:
            self.posx = 0
        elif self.posx+self.width >= WIDTH:
            self.posx = WIDTH-self.width

        self.strikerRect = pygame.Rect(
            self.posx, self.posy, self.width, self.height)

    # Returns the rect of the object
    def getRect(self):
        return self.strikerRect