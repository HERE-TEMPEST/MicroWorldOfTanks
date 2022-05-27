

TYPE_TANK = 0
TYPE_BLOCK = 1
TYPE_BANG = 2
TYPE_BULLET = 3
TYPE_UI = 4


class Object:
  def __init__(self, type):
    self.id = 0
    self.type = type
    self.__status = True
    pass

  def update(self, objects = []):
    pass

  def draw(self, window):
    pass

  def damage(self, value = 0):
    pass

  def colliderect(self, object):
    pass

  def collidepoint(self, x, y):
    pass

  def status(self):
    return self.__status