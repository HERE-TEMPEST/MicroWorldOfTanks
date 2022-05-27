from .interface import UIInterface
from environment import *

class MainMenu(UIInterface):

  def __init__(self, mplay: UIInterface, msettings: UIInterface, mratings: UIInterface, msounds: UIInterface):
    self.mplay = mplay
    self.msettings = msettings
    self.mratings = mratings
    self.msounds = msounds

  def start(self):
    play = True
    
    sounds["background_menu"].play()
    while play:

      window.fill('black')
      window.blit(main_menu, pygame.Rect(0, 0 , 1200, 700))      
      window.blit(image_button_play, pygame.Rect(950, 402 , 250, 50))      
      window.blit(image_button_rating, pygame.Rect(950, 460 , 250, 50))      
      window.blit(image_button_rules, pygame.Rect(950, 520 , 250, 50))      
      window.blit(image_button_sounds, pygame.Rect(950, 575 , 250, 50))
      window.blit(image_button_exit, pygame.Rect(950, 630 , 250, 50))
      pygame.display.update()

      for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

      keys = pygame.key.get_pressed()

      pressed = pygame.mouse.get_pressed()
      x, y = pygame.mouse.get_pos()

      if pressed[0] and 976 < x and x < 1176 and 402 < y and y < 452:
        sounds["background_menu"].stop()
        self.mplay.start()
        sounds["background_menu"].play()
        continue

      if pressed[0] and 976 < x and x < 1176 and 464 < y and y < 510:
        sounds["background_menu"].stop()
        self.mratings.start()
        sounds["background_menu"].play()
        continue

      if pressed[0] and 976 < x and x < 1176 and 522 < y and y < 564:
        sounds["background_menu"].stop()
        self.msettings.start()
        sounds["background_menu"].play()
        continue

      if pressed[0] and 976 < x and x < 1176 and 577 < y and y < 622:
        sounds["background_menu"].stop()
        self.msounds.start()
        sounds["background_menu"].play()
        continue
        
      if pressed[0] and 976 < x and x < 1176 and 630 < y and y < 677:
        play = False
        continue

        
      if keys[pygame.K_ESCAPE]:
        return

    sounds["background_menu"].stop()

  def exit(self):
    pass
