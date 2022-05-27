import pygame.key

from .interface import UIInterface
#import pygame
from environment import *

class SoundsMenu(UIInterface):

  def __init__(self):
    super().__init__()
    self.on_off = True
    pass

  def start(self):
    self.on_off = True
    play = True
    while play:

      for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False


      window.fill('black')
      window.blit(main_menu, pygame.Rect(0, 0 , 1200, 700))

      window.blit(image_button_volume, pygame.Rect(480, 250 , 250, 50))
      window.blit(image_button_russian, pygame.Rect(480, 310 , 250, 50))
      window.blit(image_button_germany, pygame.Rect(480, 370 , 250, 50))
      window.blit(image_button_exit, pygame.Rect(480, 430 , 250, 50))


      pressed = pygame.mouse.get_pressed()
      x, y = pygame.mouse.get_pos()
 
      if pressed[0] and 502 < x and x < 700 and 251 < y and y < 292 and self.on_off:
        on_off()
        self.on_off = False
      if pressed[0] and 502 < x and x < 700 and 310 < y and y < 352:
        change_language_russian()
      if pressed[0] and 502 < x and x < 700 and 374 < y and y < 414:
        change_language_germany()
      if pressed[0] and 502 < x and x < 700 and 444 < y and y < 478:
        return



      pygame.display.update()

  def exit(self):
    pass
