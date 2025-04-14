######################################################################
# Author: Magnus McCaslin
# Username: mccaslinm
#
# Assignment: Final Project
#
# Purpose: Runs a Pong game
######################################################################
import pygame
from button_class import Button

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




    def title_run(self):
        """
        Runs the game forever

        :return: None
        """
        while self.running:
            # Handle game ending first
            self.screen.fill(self.bg_color)
            mouse = pygame.mouse.get_pos()
            quit_button = Button((0, 0), (40, 140), 'Quit')
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if quit_button.posx <= mouse[0] <= quit_button.posx+140 and quit_button.posy <= mouse[1] <= quit_button.posy+40:
                        pygame.quit()

            self.screen.fill(self.bg_color)
            mouse = pygame.mouse.get_pos()
            if width / 2 <= mouse[0] <= width / 2 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
                pygame.draw.rect(screen, color_light, [width / 2, height / 2, 140, 40])
            else:
                pygame.draw.rect(screen, color_dark, [width / 2, height / 2, 140, 40])

            screen.blit(text, (width / 2 + 50, height / 2))
            pygame.display.update()
        pygame.quit()




def main():
    """
    Starts the pong game.

    :return: None
    """
    game = Game()
    game.title_run()

if __name__ == "__main__":
    main()
