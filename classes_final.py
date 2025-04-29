######################################################################
# Assignment: Final Project
#
# Author(s): Magnus McCaslin & Jaron Rhea
#
# Purpose: Contains the classes for the paddle and ball objects
######################################################################

import pygame
import random
import math
from time import sleep

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100
PADDLE_SPEED = 8.5

class Ball:
    def __init__(self, screen):
        """
        Initializes the Ball object.
        """
        self.screen = screen
        self.radius = 15
        self.color = WHITE

        # Position the ball in the center of the screen
        self.x = screen.get_width() // 2
        self.y = screen.get_height() // 2

        # Randomize the initial angle and speed
        self.speed = 9.5  # Set a constant speed
        self.angle = random.uniform(0, 360 )  # Random angle in degrees (0-360)
        while self.angle == range(80, 120) or self.angle == range(260, 280) or self.angle == range(0, 30) or self.angle == range(330, 360) or self.angle == range(150, 210):
            self.angle = random.uniform(0, 360)

        self.x_vel, self.y_vel = self.calculate_velocity() # Calculate initial velocity

        # Create a rect for collision detection
        self.rect = pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2)

        self.player_score = 0
        self.opp_score = 0

    def calculate_velocity(self):
        """
        Calculates the x and y velocities based on the angle and speed.
        """
        radians = math.radians(self.angle)
        x_vel = self.speed * math.cos(radians)
        y_vel = -self.speed * math.sin(radians) # Invert y-axis for Pygame
        return x_vel, y_vel

    def update(self):
        """
        Updates the ball's position and handles basic wall collisions.
        """
        # Update ball position based on velocity
        self.x += self.x_vel
        self.y += self.y_vel

        # Update the collision rect to match the ball's position
        self.rect.center = (self.x, self.y)

        # Check for top/bottom wall collisions
        if self.y <= self.radius or self.y >= self.screen.get_height() - self.radius:
            self.y_vel *= -1  # Reverse y velocity (bounce)

        # Check if ball went past left or right edge (point scored)
        if self.x <= 0:
            self.opp_score += 1
        elif self.x >= self.screen.get_width():
            self.player_score += 1
        if self.x <= 0 or self.x >= self.screen.get_width():
            # Reset ball position
            self.x = self.screen.get_width() // 2
            self.y = self.screen.get_height() // 2
            #delay the start of next round by one second
            sleep(1)
            #starts moving the ball again in a random direction
            self.angle = random.uniform(0, 360) # New random angle
            while self.angle == range(90, 190) or self.angle == range(270, 270):
                self.angle = random.uniform(0, 360)
            self.x_vel, self.y_vel = self.calculate_velocity() # Recalculate velocity

    def check_paddle_collision(self, paddles):
        """
        Checks if the ball collides with any of the paddles.
        """
        for paddle in paddles:
            if self.rect.colliderect(paddle.rect):
                self.x_vel *= -1  # Reverse the x velocity (bounce)
                # Add a small offset to prevent the ball from getting stuck in paddle
                if self.x_vel > 0:
                    self.rect.left = paddle.rect.right
                else:
                    self.rect.right = paddle.rect.left
                break

    def draw(self):
        """
        Draws the ball on the screen.
        """
        pygame.draw.circle(self.screen, self.color, (int(self.x), int(self.y)), self.radius)

class Paddle:
    def __init__(self, screen, x):
        self.screen = screen
        self.width = PADDLE_WIDTH
        self.height = PADDLE_HEIGHT
        self.color = WHITE
        self.x = x
        self.y = screen.get_height() // 2 - self.height // 2
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def move(self, direction):
        self.y += direction * PADDLE_SPEED
        self.y = max(0, min(self.y, self.screen.get_height() - self.height))  # Keep paddle on screen
        self.rect.y = self.y

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)