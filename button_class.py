######################################################################
# Author: Magnus McCaslin
# Username: mccaslinm
#
# Assignment: Final Project
#
# Purpose: Create the class for the button objects
######################################################################

class Button():


    def __init__(self, pos: tuple, size, message, event):
        self.posx = pos[0]
        self.posy = pos[1]
        self.size = size
        self.color = (255, 255, 255)
        self.color_light = (170, 170, 170)
        self.color_dark = (100, 100, 100)
        self.message = message
        self.event = event

    def start_game(self):




