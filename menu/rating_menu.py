import sys
import pygame
from .interface import UIInterface
from environment import *

from rating import modelRatings

class RatingMenu(UIInterface):

    def __init__(self):
        super().__init__()
        pass

    def start(self):

        # top 3
        story_count = modelRatings.get_ratings()[:3]

        play = True
        while play:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    play = False

            window.fill('black')
            window.blit(main_menu, pygame.Rect(0, 0, 1200, 700))
            window.blit(image_button_exit, pygame.Rect(480, 600, 250, 50))
            weigth = 0
            f1 = pygame.font.Font(None, 30)
            for element in story_count:
                key = f1.render(element.name, True,
                                (255, 255, 255))
                value = f1.render(f'{element.score}', True,
                                  (255, 255, 255))
                window.blit(key, (480, 250 + weigth))
                window.blit(value, (680, 250 + weigth))
                weigth += 50
            pygame.display.update()

            pressed = pygame.mouse.get_pressed()
            x, y = pygame.mouse.get_pos()

            if pressed[0] and 480 < x < 730 and 600 < y < 650:
                return

    def exit(self):
        pass
