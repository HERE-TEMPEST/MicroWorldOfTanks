from .block import *

class BushesBlock(Block):
  def __init__(self, x, y, size):
    super().__init__(BUSHES_BLOCK, x, y, size)
    
  def damage(self, value = 0):
    return True