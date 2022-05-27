import pygame

sounds = {
    "background_game": pygame.mixer.Sound('sounds/igra-prestolov-zastavka.mp3'),
    "background_menu": pygame.mixer.Sound('sounds/main_menu.mp3'),
    "babah": pygame.mixer.Sound('sounds/babahz.mp3'),
    "shot": pygame.mixer.Sound('sounds/probitie-2.mp3'),
    "dead": pygame.mixer.Sound('sounds/tank-unichtozhen.mp3')
}
sounds["background_game"].set_volume(0.5)

class MySound:
  def play():
    pass
  def stop():
    pass
  def set_volume(value):
    pass

ON_OFF = True

def change_language_russian():
    global sounds
    if not isinstance(sounds["dead"], MySound):
      sounds["shot"] = pygame.mixer.Sound('sounds/probitie-2.mp3')
      sounds["dead"] = pygame.mixer.Sound('sounds/tank-unichtozhen.mp3')

def change_language_germany():
    global sounds
    if not isinstance(sounds["dead"], MySound):
      sounds["dead"] = pygame.mixer.Sound('sounds/dead.mp3')
      sounds["dead"].set_volume(0.5)
      sounds["shot"] = pygame.mixer.Sound('sounds/shoot.mp3')
      sounds["shot"].set_volume(0.5)

def on_off():
    global sounds
    global ON_OFF
    if ON_OFF:
      sounds["dead"] = MySound
      sounds["shot"] = MySound
      sounds["background_game"] = MySound
      sounds["background_menu"] = MySound
      sounds["babah"] = MySound
      ON_OFF = False
    else:
      sounds["background_game"] = pygame.mixer.Sound('sounds/igra-prestolov-zastavka.mp3')
      sounds["background_game"].set_volume(0.5)
      sounds["background_menu"] = pygame.mixer.Sound('sounds/main_menu.mp3')
      sounds["babah"] = pygame.mixer.Sound('sounds/babahz.mp3')
      sounds["shot"] = pygame.mixer.Sound('sounds/probitie-2.mp3')
      sounds["dead"] = pygame.mixer.Sound('sounds/tank-unichtozhen.mp3')
      ON_OFF = True


