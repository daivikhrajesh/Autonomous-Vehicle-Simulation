#vehicle.py

import pygame
import numpy as np
from config import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, BLACK, RED

class Vehicle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocity = 0
        self.acceleration = 0

    def update(self):
        # Update vehicle position based on velocity and acceleration
        self.x += self.velocity
        self.y += self.acceleration

    def draw(self, screen):
        # Draw the vehicle on the screen
        pygame.draw.circle(screen, BLACK, (self.x, self.y), 10)
