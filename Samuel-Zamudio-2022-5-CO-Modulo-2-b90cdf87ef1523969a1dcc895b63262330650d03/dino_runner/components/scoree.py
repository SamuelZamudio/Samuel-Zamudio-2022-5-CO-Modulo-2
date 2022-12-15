import pygame

from dino_runner.utils.constants import FONT_STYLE, SCREEN_HEIGHT, SCREEN_WIDTH

class Scoree:
    half_screen_height = SCREEN_HEIGHT // 2 + 50
    half_screen_width = SCREEN_WIDTH // 2
    def __init__(self, message_score, screen):
       screen.fill((255, 255, 255)) 
       self.font = pygame.font.Font(FONT_STYLE, 30)
       self.text = self.font.render(message_score, True,(0, 0, 0))
       self.text_rect = self.text.get_rect()
       self.text_rect.center = (self.half_screen_width, self.half_screen_height)

    def update_scoree(self, game):
      pygame.display.update()
      self.handle_events_on_score(game)

    def draw(self, screen):
        screen.blit(self.text, self.text_rect)

    def handle_events_on_score(self, game):
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          game.running = False
          game.playing = False
        elif event.type == pygame.KEYDOWN:
          game.run()

    def reset_screen_color(self,screen):
        screen.fill((255, 255, 255)) 

    def update_message_score(self, message_score):
       self.text = self.font.render(message_score, True,(0, 0, 0))
       self.text_rect = self.text.get_rect()
       self.text_rect.center = (self.half_screen_width, self.half_screen_height)