import sys
import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:
    """Class to manage game assets and behaviour."""

    def __init__(self) -> None:
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        # Set the background color.
        self.bg_color = self.settings.bg_color

        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for Keybord and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # Redraw the screen during each pass through the loop.
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            # Make the most recently drawn screen visible.
            pygame.display.flip()


if __name__ == "__main__":
    # Init game instance and run the game.
    ai = AlienInvasion()
    ai.run_game()