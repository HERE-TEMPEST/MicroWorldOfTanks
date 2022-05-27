from main_object import *
from images import *
from environment import *

class Bang(Object):
  def __init__(self, x, y):
    super().__init__(TYPE_BANG)
    self.__status = True
    self.x = x
    self.y = y
    self.frame = 0

  def update(self, objects = []):
    self.frame += 0.2
    if self.frame >= 3:
      self.__status = False

  def draw(self, window: pygame.Surface):
    image = imgBangs[int(self.frame)]
    rect = image.get_rect(center = (self.x, self.y))
    window.blit(image, rect)    

  def status(self):
    return self.__status
