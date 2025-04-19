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
        Runs the main menu screen

        :return: None
        """

        self.screen.fill(self.bg_color)

        while self.running:
            # Stores the mouse position as a tuple (x, y)
            mouse = pygame.mouse.get_pos()

            # Creates all buttons needed for this screen
            quit_button = Button(None, (self.width/2, self.height/2 + 100), 'QUIT', pygame.font.SysFont('Arial', 50), 'White', 'Grey')
            single_player_button = Button(None, (self.width/2, self.height/2 - 100), 'SINGLE PLAYER', pygame.font.SysFont('Arial', 50), 'White', 'Grey')
            multiplayer_button = Button(None, (self.width/2, self.height/2), 'MULTIPLAYER', pygame.font.SysFont('Arial', 50), 'White', 'Grey')

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if quit_button.checkForInput(mouse):
                        self.running = False
                    if single_player_button.checkForInput(mouse):
                        self.single_player_run()
                    if multiplayer_button.checkForInput(mouse):
                        self.multiplayer_run()


                for button in [quit_button, single_player_button, multiplayer_button]:
                    button.changeColor(mouse)
                    button.update(self.screen)

            pygame.display.update()
        pygame.quit()

    def single_player_run(self):
        print('SINGLE PLAYER RUNNING')

    def multiplayer_run(self):
        print('MULTIPLAYER RUNNING')




def main():
    """
    Starts the pong game.

    :return: None
    """
    game = Game()
    game.title_run()

if __name__ == "__main__":
    main()
