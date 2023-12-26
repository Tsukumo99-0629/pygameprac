import sys

import pygame

from settings import Settings
from ship import Ship
from yusya import Yusya

class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("エイリアン侵略")
        self.ship = Ship(self)
        self.yusya = Yusya(self)



    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()


    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
    
    def _update_screen(self):
            self.screen.fill(self.settings.bg_color)    
            self.ship.blitme()
            self.yusya.blitme()    
            pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
    