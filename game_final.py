######################################################################
# Assignment: Final Project
#
# Author(s): Magnus McCaslin & Jaron Rhea
#
# Purpose: This file contains the Pong game
######################################################################

import pygame
import random
from time import sleep
from button_class import Button
from classes_final import Ball, Paddle

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100
PADDLE_SPEED = 8.5

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Pong with Random Ball Direction")
        self.clock = pygame.time.Clock()
        self.title_running = True
        self.start_running = False
        pygame.init()
        pygame.font.init()
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()
        self.bg_color = (0, 64, 0)

        # Create game objects
        self.ball = Ball(self.screen)
        self.paddle1 = Paddle(self.screen, 10)  # Left paddle
        self.paddle2 = Paddle(self.screen, SCREEN_WIDTH - 10 - PADDLE_WIDTH)  # Right paddle
        self.paddles = [self.paddle1, self.paddle2]

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
                    self.start_running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.ball.player_score = 0
                        self.ball.opp_score = 0
                        self.title_run()
                    if event.key == pygame.K_r:
                        self.ball.player_score = 0
                        self.ball.opp_score = 0
                        self.ball.x = self.screen.get_width() // 2
                        self.ball.y = self.screen.get_height() // 2
                        # delay the start of next round by one second
                        sleep(1)
                        # starts moving the ball again in a random direction
                        self.ball.angle = random.uniform(0, 360)  # New random angle
                        while self.ball.angle == range(90, 190) or self.ball.angle == range(270, 270):
                            self.ball.angle = random.uniform(0, 360)
                        self.ball.x_vel, self.ball.y_vel = self.ball.calculate_velocity()  # Recalculate velocity

            # Handle paddle movement (example: using arrow keys)
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                self.paddle1.move(-1)  # Move up
            if keys[pygame.K_s]:
                self.paddle1.move(1)  # Move down
            if keys[pygame.K_UP]:
                self.paddle2.move(-1)  # Move up
            if keys[pygame.K_DOWN]:
                self.paddle2.move(1)  # Move down

            # Update game objects
            self.ball.update()
            self.ball.check_paddle_collision(self.paddles)

            # Draw everything
            self.screen.fill(self.bg_color)
            self.ball.draw()
            self.paddle1.draw()
            self.paddle2.draw()

            font = pygame.font.Font(None, 74)
            text = font.render(str(self.ball.player_score), 1, 'white')
            self.screen.blit(text, (250, 10))
            text = font.render(str(self.ball.opp_score), 1, 'white')
            self.screen.blit(text, (450, 10))

            pygame.display.flip()

            self.clock.tick(60)  # Limit frame rate to 60 FPS

        pygame.quit()

def main():
    game = Game()
    game.title_run()

if __name__ == "__main__":
    main()