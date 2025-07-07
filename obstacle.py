import pygame
import random

class Obstacle:
    def __init__(self, score):
        self.width = 50 + min(score // 200, 50)  
        self.height = 50
        self.rect = pygame.Rect(random.randint(800, 1000), 300, self.width, self.height)

    def update(self, speed):
        self.rect.x -= speed
        if self.rect.x < -self.width:
            self.rect.x = random.randint(800, 1200)

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), self.rect)
