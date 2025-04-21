#######################################################################################
#Author: Jaron Rhea
#
#
#
#######################################################################################

import pygame

    #
    #
    # class Ball():
    #
    #
    #
    #     def __init__(self):
    #
    #         self.color = "Blue"
    #         self.size = 5
    #         self.turtle = None
    #         self.loc = (0) and (0)
    #         self.speed = 3



import pygame

class Paddle(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen_size = screen
        self.surf = pygame.image.load('image/Vertical_Rectangle_Black_Bordered-400x533.jpg').convert_alpha()
        self.surf.set_colorkey((255, 255, 255), pygame.RLEACCEL)
        self.rect = self.surf.get_rect()
        self.rect.center = (
            self.screen_size.get_width() // 2,
            self.screen_size.get_height() // 2
        )

    def PaddleMovement(self, keys):
        pass


class PlayerPaddle(Paddle):
    def __init__(self, screen):
        super().__init__(screen)

    def PaddleMovement(self, keys):
        if keys[pygame.K_UP]:
            self.rect.move_ip(0, -3)
        if keys[pygame.K_DOWN]:
            self.rect.move_ip(0, 3)



class OpponentPaddle(Paddle):
    def __init__(self, screen):
        super().__init__(screen)
        # Position the opponent on the left side of the screen
        self.rect.midleft = (10, screen.get_height() // 2)

    def PaddleMovement(self, keys):
        if keys[pygame.K_w]:
            self.rect.move_ip(0, -3)  # Move up
        if keys[pygame.K_s]:
            self.rect.move_ip(0, 3)  # Move down



class Game:
    def __init__(self):
        self.size = 800, 600
        self.running = True
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        self.clock = pygame.time.Clock()
        self.player = PlayerPaddle(self.screen)
        self.opponent = OpponentPaddle(self.screen)

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            keys = pygame.key.get_pressed()
            self.player.PaddleMovement(keys)
            self.opponent.PaddleMovement(keys)

            self.screen.fill('#9CBEBA')
            self.screen.blit(self.player.surf, self.player.rect)
            self.screen.blit(self.opponent.surf, self.opponent.rect)
            pygame.display.update()
            self.clock.tick(60)

        pygame.quit()


def main():
    game = Game()
    game.run()

if __name__ == "__main__":
    main()



def main():
    game = Game()
    game.run()

if __name__ == "__main__":
    main()