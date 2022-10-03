
import pygame
import random

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import BIRD

class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            obstacle_draw = random.randint(0, 1)
            if obstacle_draw == 0:
                cactus_type = "SMALL" if random.randint(0,1) == 0 else "LARGE"
                self.obstacles.append(Cactus(cactus_type))
            else:
                bird_y = random.randint (0, 1)
                self.obstacles.append (Bird(BIRD,bird_y))


        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if game.player.shield:
                    self.obstacles.remove(obstacle)
                elif game.player.hammer:
                    self.obstacles.remove(obstacle)
                elif game.player.heart:
                    self.obstacles.remove(obstacle)
                else:
                    pygame.time.delay(500)    
                    game.death_count += 1
                    game.playing = False
                    break
    
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []