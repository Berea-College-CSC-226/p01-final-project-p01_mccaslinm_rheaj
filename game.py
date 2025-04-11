######################################################################
# Author: Magnus McCaslin
# Username: mccaslinm
#
# Assignment: Final Project
#
# Purpose: Runs a Pong game
######################################################################
import pygame
import sys

class Game:

    def __init__(self):
        """
        Game class for handling the game logic.
        """
        self.size = 800, 600
        self.running = True
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Pong Game")
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()
        self.bg_color = (0, 64, 0)

    def title_screen(self):



    def run(self):
        """
        Runs the game forever

        :return: None
        """
        while self.running:
            # Handle game ending first
            self.screen.fill(self.bg_color)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            pygame.display.flip()
        pygame.quit()


def main():
    """
    Starts the cat game.

    :return: None
    """
    game = Game()
    game.run()

if __name__ == "__main__":
    main()
