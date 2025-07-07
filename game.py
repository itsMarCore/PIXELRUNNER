import pygame
from player import Player
from obstacle import Obstacle
from menu import Menu
from game_over import GameOver

class Game:
    def __init__(self, level=1):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 400))
        pygame.display.set_caption("Pixel Runner")
        self.clock = pygame.time.Clock()
        self.running = True
        self.player = Player()
        self.score = 0
        self.obstacles = []
        self.spawn_timer = 60
        self.font = pygame.font.SysFont(None, 36)
        self.min_distance_between_obstacles = 250
        self.level = level
        self.base_speed = {1: 5, 2: 7, 3: 10}.get(level, 5)

    def run(self):
        menu = Menu(self.screen)
        level = menu.draw_start_menu()
        self.level = level
        self.base_speed = {1: 5, 2: 7, 3: 10}.get(level, 5)

        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)

        GameOver(self.screen, self.score).show()
        self.reset()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

    def update(self):
        self.player.update()
        speed = self.base_speed + self.score // 500

        for obstacle in self.obstacles:
            obstacle.update(speed)
            if self.player.rect.colliderect(obstacle.rect):
                self.running = False

        self.score += 1
        self.min_distance_between_obstacles = max(150, 250 - self.score // 100)

        if self.spawn_timer > 0:
            self.spawn_timer -= 1
        else:
            last = self.obstacles[-1] if self.obstacles else None
            if not last or last.rect.x < 800 - self.min_distance_between_obstacles:
                self.obstacles.append(Obstacle(self.score))

        self.obstacles = [o for o in self.obstacles if o.rect.right > 0]

    def draw(self):
        self.screen.fill((200, 255, 255))
        pygame.draw.rect(self.screen, (100, 200, 100), (0, 350, 800, 50))
        self.player.draw(self.screen)

        for obstacle in self.obstacles:
            obstacle.draw(self.screen)

        score_text = self.font.render(f"Score: {self.score}", True, (0, 0, 0))
        self.screen.blit(score_text, (10, 10))
        pygame.display.flip()

    def reset(self):
        self.__init__(self.level)
        self.run()
