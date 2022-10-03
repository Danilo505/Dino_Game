
from asyncio import shield
from ctypes import pointer
import pygame
import random

from dino_runner.components.power_ups.shield import Shield

class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.when_appear = 0

    def update(self, game, points):
        if len(self.power_ups) == 0:
            if self.when_appear == points:
                self.when_appear = random.randint(self.when_appear +200, self.when_appear +300)
                self.power_ups.append(Shield())

        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)
            if game.player.dino_rect.colliderect(power_up):
                power_up.start_time = pygame.time.get_ticks()
                game.player.shield = True
                game.player.type = power_up.type
                game.player.shield_time_up = power_up.start_time + (random.randint(5, 8)*1000 )
                self.power_ups.remove(power_up)
                break
    
    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset_power_ups(self):
        self.power_ups = []
        self.when_appear = random.randint(200, 200)