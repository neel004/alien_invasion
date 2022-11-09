import pygame


class Ship:
    """A class to manage the ship"""

    def __init__(self, ai_game) -> None:
        """Initialize the ship and its starting position.

        Args:
            ai_game (_type_): _description_
        """
        self.screen = ai_game.screen
        self.screen_react = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.get_rect()
        self.rect = self.image.get_react()
        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_react.midbottom

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)
