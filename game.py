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
        pass



    def run(self):
        """
        Runs the game forever

        :return: None
        """
        while self.running:
            # Handle game ending first
            self.screen.fill(self.bg_color)
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.width/2 <= mouse[0] <= self.width/2+140 and self.height/2 <= mouse[1] <= height/2+40:
                        pygame.draw.rect(self.screen, self.color)


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
