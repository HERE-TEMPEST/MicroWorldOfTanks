from main_object import Object, TYPE_BLOCK
from environment import *

BRICK_BLOCK = 0
BUSHES_BLOCK = 1
ARMOR_BLOCK = 2
WATER_BLOCK = 3

class Block(Object):
  def __init__(self, type, x, y, size):
    super().__init__(TYPE_BLOCK)
    self.type_block = type
    self.image = imgBlocks[type]
    self.hp = 1
    self.sprite = pygame.Rect(x, y, size, size)

  def draw(self, window: pygame.Surface):
    window.blit(self.image, self.sprite)

  def damage(self, value = 0):
    pass

  def colliderect(self, object):
    pass
