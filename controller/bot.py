from typing import List
from random import randint
import pygame
from map.map import Map

from main_object import Object
from main_object.object import TYPE_BLOCK
from tank.tank import TankBuilder
from .controller import Controller, TYPE_BOT
from tank import Tank
from blocks import WATER_BLOCK

class TankBot(Controller):

  def __init__(self):
    self.amount_bots = 5
    super().__init__(TYPE_BOT)
    self.step = randint(50, 100)
    self.players: List[Tank] = []
    self.tanks: List[Tank] = []

  def update(self, map: Map):
      if self.amount_bots - len(self.tanks) > 0:
        for _ in range(0, self.amount_bots - len(self.tanks)):
          new_bot = TankBuilder.random_generate()
          map.add_object(new_bot)
          self.tanks.append(new_bot)

      if self.step == 0:
        self.step = randint(50, 100)
      self.step -= 1

      for player in self.players:
        if not player.status():
          self.players.remove(player)

      for tank in self.tanks:
        if not tank.status():
          self.tanks.remove(tank)

      for player in self.players:
        x = player.sprite.centerx
        y = player.sprite.centery

        for tank in self.tanks:
          if tank != player and tank.status():
              x_ = tank.sprite.centerx
              y_ = tank.sprite.centery

              l_x = x
              if x_ < x:
                l_x = x_
              l_y = y
              if y_ < y:
                l_y = y_
              layout_x = pygame.Rect(l_x, y_ - 10, abs(x - x_), 20)
              layout_y = pygame.Rect(x_ - 10, l_y, 20, abs(y_ - y))

              #pygame.draw.rect(window, 'red', layout_x)
              #pygame.draw.rect(window, 'red', layout_y)

              flag_x = True
              flag_y = True
              for object in map.objects:
                if object.type is TYPE_BLOCK and object.type_block is not WATER_BLOCK:
                  if layout_x.colliderect(object.sprite):
                    flag_x = False
                  if layout_y.colliderect(object.sprite):
                    flag_y = False

              if x_ - 10 <= x and x_ + 10 >= x and flag_y:
                if y < y_:
                  tank.direct = 0
                else:
                  tank.direct = 2
                tank.shoot()
              elif y_ - 10 <= y and y_ + 10 >= y and flag_x:
                if x < x_:
                  tank.direct = 3
                else:
                  tank.direct = 1
                tank.shoot()
              else:
                if self.step != 0:
                  tank.update_direct(tank.direct)
                else:
                  tank.update_direct(randint(0, 4))
          

  def set(self, tank: Tank):
      self.players.append(tank)
  
  def set_objects(self, tanks: List[Tank]):
      self.tanks = tanks