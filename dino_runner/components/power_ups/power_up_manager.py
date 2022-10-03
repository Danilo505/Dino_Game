from pickle import TRUE
import random
import pygame

from dino_runner.components.power_ups.shield import Hammer, Shield, Heart

class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.when_appear = 0

    def update(self, game, points):
        if len(self.power_ups) == 0 and self.when_appear == points:
            self.poder = random.randint(0, 2)
            self.when_appear += random.randint(200, 300)

            if self.poder ==1:
                self.power_ups.append(Shield())

            elif self.poder == 0:
                self.power_ups.append(Hammer())
            else:
                self.power_ups.append(Heart())

        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)
            if game.player.dino_rect.colliderect(power_up):
                power_up.start_time = pygame.time.get_ticks() 
                
                if self.poder == 0:
                   game.player.shield = False
                   game.player.hammer = True
                   game.player.heart = False
                   self.player_config(game.player, power_up)
                elif self.poder == 1:
                    game.player.shield = True
                    game.player.hammer = False
                    game.player.heart = False
                    self.player_config(game.player, power_up)
                else:
                    game.player.shield = False
                    game.player.hammer = False
                    game.player.heart = True
                    self.player_config(game.player, power_up)
               
                self.power_ups.remove(power_up)
                
    
    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset_power_ups(self):
        self.power_ups = []
        self.when_appear = random.randint(200, 200)

    def player_config(self, player, power_up):
        player.has_power_up = True
        player.type = power_up.type
        player.shield_time_up = power_up.start_time + (power_up.duration * 1000)