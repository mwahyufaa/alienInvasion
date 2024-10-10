import sys
import pygame

from settings import Settings
class AlienInvasion:
    """Overall class to manage game assets and behaviour."""

    def __init__(self):
        """Initialize the game, create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((1280,720))
        pygame.diplay.set_caption("Alien Invasion")

        #set background color
        self.bg_color = (0,0,255)

    def run_game(self):
        """Start the main loop for game"""
        while True:
            #Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            #Redraw the screen during each pass through the loop.
            self.screen.fill(self.bg_color)

            #Make the most recently drawn screen visible.
            pygame.diplay.flip()

if __name__ == '__main__':
    #Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()

class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's static settings."""
        #Screen settings
        self.screen_width = 1280
        self.screen_height = 720
        self.bg_color=(0,0,255)




