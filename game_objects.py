import pygame
from settings import *

class Paddle:
    def __init__(self, x, y, width, height, color, speed):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.speed = speed  # Make sure to initialize the speed attribute here

    def move(self, direction, screen_width):
        if direction == "left" and self.rect.left > 0:
            self.rect.x -= self.speed
        elif direction == "right" and self.rect.right < screen_width:
            self.rect.x += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)


class Ball:
    def __init__(self, x, y, speed_x, speed_y, radius, color):
        self.x = x  # Floating-point x position
        self.y = y  # Floating-point y position
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.radius = radius
        self.color = color
        self.rect = pygame.Rect(int(x), int(y), radius*2, radius*2)
    
    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y
        # Update the rect position based on the new x and y
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)

        # Collision with walls
        if self.rect.right >= SCREEN_WIDTH or self.rect.left <= 0:
            self.speed_x *= -1
        if self.rect.top <= 0:
            self.speed_y *= -1

    def draw(self, screen):
        pygame.draw.ellipse(screen, self.color, self.rect)

class Brick:
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
