import pygame
import sys

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont(None, 48)
        self.options = ["Iniciar Juego", "Seleccionar Nivel", "Acerca De", "Salir"]
        self.levels = [1, 2, 3]

    def draw_start_menu(self):
        selected = 0
        while True:
            self.screen.fill((255, 255, 255))
            title = self.font.render("Pixel Runner", True, (0, 0, 0))
            self.screen.blit(title, (250, 50))

            for i, option in enumerate(self.options):
                color = (0, 0, 0) if i != selected else (255, 0, 0)
                text = self.font.render(option, True, color)
                self.screen.blit(text, (200, 150 + i * 60))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        selected = (selected + 1) % len(self.options)
                    elif event.key == pygame.K_UP:
                        selected = (selected - 1) % len(self.options)
                    elif event.key == pygame.K_RETURN:
                        if self.options[selected] == "Iniciar Juego":
                            return 1
                        elif self.options[selected] == "Seleccionar Nivel":
                            return self.select_level()
                        elif self.options[selected] == "Acerca De":
                            self.show_about()
                        elif self.options[selected] == "Salir":
                            pygame.quit()
                            sys.exit()

    def select_level(self):
        selected_level = 0
        while True:
            self.screen.fill((255, 255, 255))
            title = self.font.render("Selecciona Nivel", True, (0, 0, 0))
            self.screen.blit(title, (200, 50))

            for i, level in enumerate(self.levels):
                color = (0, 0, 0) if i != selected_level else (255, 0, 0)
                text = self.font.render(f"Nivel {level}", True, color)
                self.screen.blit(text, (250, 150 + i * 60))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        selected_level = (selected_level + 1) % len(self.levels)
                    elif event.key == pygame.K_UP:
                        selected_level = (selected_level - 1) % len(self.levels)
                    elif event.key == pygame.K_RETURN:
                        return self.levels[selected_level]

    def show_about(self):
        self.screen.fill((255, 255, 255))
        title = self.font.render("Pixel Runner", True, (0, 0, 0))
        self.screen.blit(title, (250, 50))
        author = self.font.render("Desarrollado por: FollaRaperos y Roglo", True, (0, 0, 0))
        self.screen.blit(author, (150, 150))
        press = self.font.render("Presiona cualquier tecla...", True, (100, 100, 100))
        self.screen.blit(press, (150, 300))
        pygame.display.flip()

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    waiting = False
