######################################################################
# Author: Magnus McCaslin
# Username: mccaslinm
#
# Assignment: Final Project
#
# Purpose: Runs a Pong game
######################################################################
import pygame, scratch_2
from button_class import Button
from scratch_2 import Paddle, PlayerPaddle, OpponentPaddle, Ball

class Game:
    def __init__(self):
        self.size = 800, 600
        self.title_running = True
        self.start_running = False
        pygame.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Pong Game")
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()
        self.bg_color = (0, 64, 0)
        # Create a clock to control frame rate
        self.clock = pygame.time.Clock()

        # Create the player's paddle (left side)
        self.player = PlayerPaddle(self.screen, (50, self.height // 2 - 70))

        # Create the opponent's paddle (right side)
        self.opponent = OpponentPaddle(self.screen, (self.width - 90, self.height // 2 - 70))

        # Create the ball
        self.ball = Ball(self.screen)

    def title_run(self):
        """
        Runs the main menu screen

        :return: None
        """
        self.title_running = True

        self.screen.fill(self.bg_color)

        while self.title_running:
            # Stores the mouse position as a tuple (x, y)
            mouse = pygame.mouse.get_pos()

            # Creates all buttons needed for this screen
            quit_button = Button(None, (self.width/2, self.height/2), 'QUIT', pygame.font.SysFont('Arial', 50), 'White', 'Grey')
            start_button = Button(None, (self.width/2, self.height/2 - 100), 'START', pygame.font.SysFont('Arial', 50), 'White', 'Grey')

            # Listens for every event in the window and responds accordingly
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.title_running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if quit_button.check_for_input(mouse):
                        self.title_running = False
                    if start_button.check_for_input(mouse):
                        self.start_run()

                for button in [quit_button, start_button]:
                    button.change_color(mouse)
                    button.update(self.screen)



            pygame.display.update()
        pygame.quit()

    def start_run(self):
        self.start_running = True


        while self.start_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.start_running = False  # Exit the game loop if window is closed

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.ball.player_score = 0
                        self.ball.opp_score = 0
                        self.title_run()
                    if event.key == pygame.K_r:
                        self.ball.player_score = 0
                        self.ball.opp_score = 0

            # Get the state of all keyboard keys
            keys = pygame.key.get_pressed()
            # Update the paddles based on key presses
            self.player.handle_movement(keys)
            self.opponent.handle_movement(keys)
            # Update the ball's position
            self.ball.update(keys)
            # Check for collisions between ball and paddles
            self.ball.check_paddle_collision([self.player, self.opponent])
            # Clear the screen by filling it with the background color
            self.screen.fill(self.bg_color)
            # Draw all game objects
            self.player.draw()
            self.opponent.draw()
            self.ball.draw()

            font = pygame.font.Font(None, 74)
            text = font.render(str(self.ball.player_score), 1, 'white')
            self.screen.blit(text, (250, 10))
            text = font.render(str(self.ball.opp_score), 1, 'white')
            self.screen.blit(text, (450, 10))

            # Update the display to show all the drawn elements
            pygame.display.flip()
            # Limit the frame rate to 60 FPS
            self.clock.tick(60)

        # Clean up when game loop exits
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
