######################################################################
# Assignment: Final Project
#
# Purpose: Create the class for the button objects
#
# Acknowledgements: https://www.youtube.com/watch?v=GMBqjxcKogA&t=55s
######################################################################

class Button:
    def __init__(self, image, pos: tuple, text_input, font, base_color, hover_color):
        self.image = image
        self.posx = pos[0]
        self.posy = pos[1]
        self.font = font
        self.base_color = base_color
        self.hover_color = hover_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        # If there is no image, the text acts as the button
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center=(self.posx, self.posy))
        self.text_rect = self.text.get_rect(center=(self.posx, self.posy))

    def update(self, screen):
        """
        Updates the button on the screen

        :param screen: program window
        :return: None
        """
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def check_for_input(self, position: tuple):
        """
        Checks if button is clicked

        :param position: where the mouse is
        :return: True if button is clicked, False otherwise
        """
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    def change_color(self, position):
        """
        Changes color is mouse is over the button

        :param position: where the mouse is
        :return: None
        """
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hover_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)