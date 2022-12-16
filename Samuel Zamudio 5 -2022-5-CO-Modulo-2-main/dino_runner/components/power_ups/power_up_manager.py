import pygame
import random

from dino_runner.components.power_ups.shield import Shield
from dino_runner.components.power_ups.hammer import Hammer

class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.when_appears = 0 
        self.duration = random.randint(2, 4)

    def update(self, game):
        self.generate_power_up(game.score.count)
        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)
            if game .player.dino_rect.colliderect(power_up.rect):
              power_up.start_time = pygame.time.get_ticks() / 1000
              game.player.has_power_up = True
              game.player.type = power_up.type
              game.player.power_time_up = power_up.start_time + self.duration

              self.power_ups.pop()

      
    def draw(self, screen):
        for powwer_up in self.power_ups:
          powwer_up.draw(screen)

    def generate_power_up(self, score):
        if len(self.power_ups) == 0 and self.when_appears == score:
          self.power_ups.append(Shield())
          self.when_appears += random.randint(100, 200)
          self.power_ups.append(Hammer())
          self.when_appears += random.randint(100, 200)

    
      
          


