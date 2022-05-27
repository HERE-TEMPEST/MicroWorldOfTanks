from .block import *

class BrickBlock(Block):
  def __init__(self, x, y, size):
    super().__init__(BRICK_BLOCK, x, y, size)
    self.hp = 1
    self.__status = True
    
  def update(self, objects = []):
    if self.hp <= 0:
      self.__status = False

  def damage(self, value = 0):
    self.hp -= value

  def status(self):
      return self.__status

  def collidepoint(self, x, y):
      return self.sprite.collidepoint(x, y)

  def colliderect(self, object):
      return self.sprite.colliderect(object.sprite)