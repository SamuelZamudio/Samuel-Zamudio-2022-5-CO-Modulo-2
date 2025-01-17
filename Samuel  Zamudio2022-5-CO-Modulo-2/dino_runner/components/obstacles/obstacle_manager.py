import pygame
import random

from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.cactus2 import Cactus2
from dino_runner.components.obstacles.bird import Bird



class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if random.randint(0, 2) == 0:
            self.obstacles.append(Cactus(SMALL_CACTUS))
        elif random.randint(0, 2) == 1:
            self.obstacles.append(Cactus2(LARGE_CACTUS))
        elif random.randint(0, 2) == 2:
            self.obstacles.append(Bird(BIRD))

        
        for obstacle in self.obstacles:
          obstacle.update(game.game_speed, self.obstacles)
          if game.player.dino_rect.colliderect(obstacle.rect):
            print("colision")
            game.playing = True
            break


    def draw(self,screen):
        for obstacle in self.obstacles:
          obstacle.draw(screen)    




    