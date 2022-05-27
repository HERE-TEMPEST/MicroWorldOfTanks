from blocks.block import WATER_BLOCK
from .block import *

class WaterBlock(Block):
  def __init__(self, x, y, size):
    super().__init__(WATER_BLOCK, x, y, size)
    self.hp = 2
    
  def colliderect(self, object):
      return self.sprite.colliderect(object.sprite)
