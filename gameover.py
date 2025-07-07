import pygame
import time

class GameOver:
    def __init__(self, screen, score):
        self.screen = screen
        self.score = score
        self.font = pygame.font.SysFont(None, 48)

    def show(self):
        self.screen.fill((255, 255, 255))
        text = self.font.render("Game Over", True, (255, 0, 0))
        score_text = self.font.render(f"Puntaje: {self.score}", True, (0, 0, 0))
        self.screen.blit(text, (300, 150))
        self.screen.blit(score_text, (300, 220))
        pygame.display.flip()
        time.sleep(2)
