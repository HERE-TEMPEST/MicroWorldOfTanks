from .block import *

class ArmorBlock(Block):
  def __init__(self, x, y, size):
    super().__init__(ARMOR_BLOCK, x, y, size)
    self.hp = 100
    self.__status = True

  def update(self, objects=[]):
    if self.hp <= 0:
      self.__status = False 

  def damage(self, value = 0):
    self.hp -= value

  def collidepoint(self, x, y):
      return self.sprite.collidepoint(x, y)

  def colliderect(self, object):
      return self.sprite.colliderect(object.sprite)

  def status(self):
      return self.__status