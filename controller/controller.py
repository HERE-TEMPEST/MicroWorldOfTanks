TYPE_HUMAN = 0
TYPE_BOT = 1
TYPE_SERVER = 2
TYPE_CLIENT = 3

class Controller:
  def __init__(self, type):
    self.type = type
    self.object = None
    pass

  def update(self):
    pass

  def set(self, tank):
    pass
  
  def set_objects(self, objects = []):
    pass