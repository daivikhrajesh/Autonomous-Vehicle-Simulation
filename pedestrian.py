""" # pedestrian.py
import pygame
from config import BLACK

class Pedestrian:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

    def update(self):
        # Move pedestrian based on direction
        self.x += self.direction

    def draw(self, screen):
        # Draw the pedestrian on the screen
        pygame.draw.circle(screen, BLACK, (self.x, self.y), 5)
 """