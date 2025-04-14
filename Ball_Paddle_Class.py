#######################################################################################
#Author: Jaron Rhea
#
#
#
#######################################################################################

from turtle import *

import pygame
from pygame import *
from tkinter import *

    class Ball():



        def __init__(self):

            self.color = "Blue"
            self.size = 5
            self.turtle = None
            self.loc = sety(0) and setx(0)
            self.speed = 3




    class Paddle():

        def __init__(self):
            self.color = "White"
            self.size = 25
            self.turtle = None




        def PaddleMovement():

            inputkeys = pygame.key.get_pressed()

            if inputkeys[pygame.KEYUP]:
                y += speed(5)

            if inputkeys[pygame.KEYDOWN]:
                y -= speed(5)




