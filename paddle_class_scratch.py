
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

class Paddle():
    def __init__(self, screen, pos: tuple):
        # Rect Properties
        self.rect_color = (255, 255, 255)
        self.rect_x = pos[0]
        self.rect_y = pos[1]
        self.rect_height = 140
        self.rect_width = 40
        self.rect_pos = (self.rect_x, self.rect_y, self.rect_width, self.rect_height)
        self.surf = pygame.draw.rect(screen, self.rect_color, self.rect_pos, 0)
        self.rect = self.surf.get_rect()

class PlayerPaddle(Paddle):
    def __init__(self, screen, pos: tuple):
        super().__init__(screen, pos,)

    def PaddleMovement(self, keys):
        if keys[pygame.K_UP]:
            self.rect_y.move_up(-3)
        if keys[pygame.K_DOWN]:
            self.rect_y.move_up(3)



class OpponentPaddle(Paddle):
    def __init__(self, screen, pos: tuple):
        super().__init__(screen, pos)



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
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()
        self.clock = pygame.time.Clock()
        self.screen.fill('#9CBEBA')
        self.player = PlayerPaddle(self.screen, (self.width / 2 - 300, self.height / 2))
        self.opponent = OpponentPaddle(self.screen, (self.width / 2 + 300, self.height / 2))

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.player.PaddleMovement(keys)
                    self.opponent.PaddleMovement(keys)

            keys = pygame.key.get_pressed()
            self.player.PaddleMovement(keys)
            self.opponent.PaddleMovement(keys)


            pygame.display.update()
            self.clock.tick(60)

        pygame.quit()


def main():
    game = Game()
    game.run()

if __name__ == "__main__":
    main()