from typing import List
from main_object import Object
from main_object.object import TYPE_TANK, TYPE_UI
from environment import *
import pygame

from tank import Tank


class UIGame(Object):
  def __init__(self):
    super().__init__(TYPE_UI)

  def update(self, tank: Tank, objects: List[Object]):
    koll_tanks = 0

    for obj in objects:
      if obj.type is TYPE_TANK:
        koll_tanks += 1

    hp_tank = tank.hp
    game_score = tank.score
    pygame.font.init()
    f1 = pygame.font.Font(None, 30)

    tanks_text = f1.render(f'Tanks: {koll_tanks}', True,
                  (255, 0, 0))
    HP = f1.render(f'HP: {hp_tank}', True,
                  (255, 0, 0))
    score = f1.render(f'score: {game_score}', True,
                  (255, 0, 0))

    window.blit(tanks_text, (1100, 30))
    window.blit(HP, (1100, 100))
    window.blit(score, (1100,170))


    pressed = pygame.mouse.get_pressed()
    x, y = pygame.mouse.get_pos()

    if pressed[0] and 1110 < x < 1185 and 650 < y < 670:
      return

    if pressed[0] and 1110 < x < 1185 and 600 < y < 620: # stop
      f3 = pygame.font.Font(None, 150)
      pause = f3.render(f'PAUSE', True,
                  (255, 255, 0))
      window.blit(pause, (400,300))




  def draw(self, window):
    pass
