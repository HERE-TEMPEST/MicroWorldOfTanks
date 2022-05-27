import pygame

imgBlocks = [
  pygame.image.load('images/block_brick.png'),
  pygame.image.load('images/block_bushes.png'),
  pygame.image.load('images/block_armor.png'),
  pygame.image.load('images/block_water.png'),
]

imgTanks = [
  pygame.image.load('images/tank1.png'),
  pygame.image.load('images/tank2.png'),
  pygame.image.load('images/tank3.png'),
  pygame.image.load('images/tank4.png'),
  pygame.image.load('images/tank5.png'),
  pygame.image.load('images/tank6.png'),
  pygame.image.load('images/tank7.png'),
  pygame.image.load('images/tank8.png'),
]

imgBangs = [
  pygame.image.load('images/bang1.png'),
  pygame.image.load('images/bang2.png'),
  pygame.image.load('images/bang3.png'),
]

main_menu = pygame.transform.scale(pygame.image.load("images/main.webp"), [1200, 700])


sprites_buttons = pygame.transform.scale(pygame.image.load("images/buttons.png"), [500, 500])
sprites_germany_button = pygame.transform.scale(pygame.image.load("images/germany.png"), [500, 500])
sprites_russian_button = pygame.transform.scale(pygame.image.load("images/russian.png"), [500, 500])
sprites_song_parameters_button = pygame.transform.scale(pygame.image.load("images/vol song.png"), [500, 500])
sprites_exit_parameters_button = pygame.transform.scale(pygame.image.load("images/Exit.png"), [500, 500])
sprites_rules_parameters_button = pygame.transform.scale(pygame.image.load("images/Rules.png"), [500, 500])


image_button_play = sprites_buttons.subsurface(10 , 150, 250, 50)
image_button_rating = sprites_buttons.subsurface(10 , 90, 250, 50)
image_button_settings = sprites_buttons.subsurface(245 , 160, 250, 50)
image_button_sounds = sprites_buttons.subsurface(11 , 220, 250, 50)


image_button_germany = sprites_germany_button.subsurface(12 , 290, 250, 50)
image_button_russian = sprites_russian_button.subsurface(12 , 290, 250, 50)
image_button_volume = sprites_song_parameters_button.subsurface(12 , 290, 250, 50)
image_button_exit = sprites_exit_parameters_button.subsurface(12 , 290, 250, 50)
image_button_rules = sprites_rules_parameters_button.subsurface(12 , 290, 250, 50)



