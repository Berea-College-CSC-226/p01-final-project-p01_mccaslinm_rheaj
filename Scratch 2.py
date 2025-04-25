import pygame


class Paddle():
    def __init__(self, screen, pos: tuple):
        """
        Initializes the Paddle object.

        Args:
            screen: The Pygame display surface to draw on.
            pos: A tuple representing the initial (x, y) position of the top-left corner of the paddle.
        """
        self.screen = screen  # Store the screen object for drawing later
        self.rect_color = (255, 255, 255)  # White color for the paddle
        self.rect = pygame.Rect(pos[0], pos[1], 40, 140)  # Create a Pygame Rect object directly
        # The Rect object stores position (x, y) and dimensions (width, height)

    def draw(self):
        """
        Draws the paddle on the screen at its current position.
        Must be called every frame to update the paddle's visual position.
        """
        # This draws a filled rectangle on the screen using our stored rect
        pygame.draw.rect(self.screen, self.rect_color, self.rect)


class PlayerPaddle(Paddle):
    def __init__(self, screen, pos: tuple):
        """
        Initializes the PlayerPaddle, inheriting from the Paddle class.
        """
        super().__init__(screen, pos)  # Call the parent class constructor

    def handle_movement(self, keys):
        """
        Handles the movement of the player's paddle based on key presses.

        Args:
            keys: A sequence of boolean values representing the state of each key.
                  Obtained from pygame.key.get_pressed().
        """
        # Check if up arrow key is pressed
        if keys[pygame.K_w]:
            self.rect.y -= 5  # Move the paddle up by decreasing its y-coordinate

        # Check if down arrow key is pressed
        if keys[pygame.K_s]:
            self.rect.y += 5  # Move the paddle down by increasing its y-coordinate

        # Keep the paddle within the screen boundaries
        if self.rect.top < 0:
            self.rect.top = 0  # If the top of the paddle goes above the screen, reset it

        if self.rect.bottom > self.screen.get_height():
            self.rect.bottom = self.screen.get_height()  # If the bottom goes below, reset it


class OpponentPaddle(Paddle):
    def __init__(self, screen, pos: tuple):
        """
        Initializes the OpponentPaddle, inheriting from the Paddle class.
        """
        super().__init__(screen, pos)  # Call the parent class constructor

    def handle_movement(self, keys):
        """
        Handles the movement of the opponent's paddle based on key presses.

        Args:
            keys: A sequence of boolean values representing the state of each key.
                  Obtained from pygame.key.get_pressed().
        """
        # Check if W key is pressed
        if keys[pygame.K_UP]:
            self.rect.y -= 5  # Move the paddle up by decreasing its y-coordinate

        # Check if S key is pressed
        if keys[pygame.K_DOWN]:
            self.rect.y += 5  # Move the paddle down by increasing its y-coordinate

        # Keep the paddle within the screen boundaries
        if self.rect.top < 0:
            self.rect.top = 0  # If the top goes above, reset it

        if self.rect.bottom > self.screen.get_height():
            self.rect.bottom = self.screen.get_height()  # If the bottom goes below, reset it


class Ball:
    def __init__(self, screen):
        """
        Initializes the Ball object.

        Args:
            screen: The Pygame display surface to draw on.
        """
        self.screen = screen
        self.radius = 15
        self.color = (255, 255, 255)  # White color for the ball

        # Position the ball in the center of the screen
        self.x = screen.get_width() // 2
        self.y = screen.get_height() // 2

        # Initial velocity (direction and speed)
        self.x_vel = 5
        self.y_vel = 5

        # Create a rect for collision detection
        self.rect = pygame.Rect(self.x - self.radius, self.y - self.radius,
                                self.radius * 2, self.radius * 2)

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
        if self.x <= 0 or self.x >= self.screen.get_width():
            # Reset ball position
            self.x = self.screen.get_width() // 2
            self.y = self.screen.get_height() // 2
            # Reverse x direction
            self.x_vel *= -1

    def check_paddle_collision(self, paddles):
        """
        Checks if the ball collides with any of the paddles.

        Args:
            paddles: A list of paddle objects to check collisions with.
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
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)


class Game:
    def __init__(self):
        """
        Initializes the Game object, setting up the screen, paddles, ball, and game state.
        """
        self.size = 800, 600  # Width and height of the game window
        self.running = True  # Flag to control the game loop

        pygame.init()  # Initialize all pygame modules

        # Set up the game window
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Pong Game")

        # Get screen dimensions for convenience
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()

        # Create a clock to control frame rate
        self.clock = pygame.time.Clock()

        # Create the player's paddle (left side)
        self.player = PlayerPaddle(self.screen, (50, self.height // 2 - 70))

        # Create the opponent's paddle (right side)
        self.opponent = OpponentPaddle(self.screen, (self.width - 90, self.height // 2 - 70))

        # Create the ball
        self.ball = Ball(self.screen)

        # Set the background color (light blue)
        self.bg_color = '#9CBEBA'

    def run(self):
        """
        The main game loop. Handles events, updates game state, and draws objects.
        """
        while self.running:
            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False  # Exit the game loop if window is closed

            # Get the state of all keyboard keys
            keys = pygame.key.get_pressed()

            # Update the paddles based on key presses
            self.player.handle_movement(keys)
            self.opponent.handle_movement(keys)

            # Update the ball's position
            self.ball.update()

            # Check for collisions between ball and paddles
            self.ball.check_paddle_collision([self.player, self.opponent])

            # Clear the screen by filling it with the background color
            self.screen.fill(self.bg_color)

            # Draw all game objects
            self.player.draw()
            self.opponent.draw()
            self.ball.draw()

            # Draw a center line (aesthetic element)
            pygame.draw.aaline(self.screen, (255, 255, 255),
                               (self.width // 2, 0), (self.width // 2, self.height))

            # Update the display to show all the drawn elements
            pygame.display.flip()

            # Limit the frame rate to 60 FPS
            self.clock.tick(60)

        # Clean up when game loop exits
        pygame.quit()


def main():
    """
    The main function that creates and runs the Game object.
    """
    game = Game()
    game.run()


if __name__ == "__main__":
    main()



