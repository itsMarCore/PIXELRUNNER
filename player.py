import pygame

class Player:
    def __init__(self):
        self.rect = pygame.Rect(100, 300, 50, 50)
        self.velocity = 0
        self.is_jumping = False

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and not self.is_jumping:
            self.velocity = -10
            self.is_jumping = True

        self.velocity += 0.5
        self.rect.y += self.velocity

        if self.rect.y >= 300:
            self.rect.y = 300
            self.velocity = 0
            self.is_jumping = False

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 255), self.rect)
