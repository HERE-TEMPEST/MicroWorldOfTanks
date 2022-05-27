import pickle
from re import S
from main_object.object import TYPE_BULLET, TYPE_TANK

from tank import Bullet
from tank.tank import Tank
from .controller import Controller, TYPE_CLIENT
from map import Map
from interworking import DuplexQueue

CONNECTED = 0
BLOCK = 1
TANK = 2
BULLET = 4
END_CHUNK = 3
S_TANK = 5
S_BULLET = 6
S_BLOCK = 7



class ClientController(Controller):
  def __init__(self, map: Map, queue: DuplexQueue):
    super().__init__(TYPE_CLIENT)
    self.map = map
    self.queue = queue
    self.tank = None

  def update(self):
    count = 20
    while count != 0:
      count -= 1
      message = self.queue.shift_in()
      if message is not None:
        body = pickle.loads(message)

        if body["command"] == CONNECTED:
          new_tank = Tank(body["x"], body["y"])
          new_tank.id = body["id"]
          new_tank.level = body["l"]
          new_tank.bulletDamage = body["u"]
          continue

        if body["command"] == S_TANK:
          for object in self.map.objects:
            if object.id == body["id"] and object.type is TYPE_TANK:
              if body["s"] is False:
                self.map.objects.remove(object)
              elif self.tank.id != body["id"]:
                object.sprite.x = body["x"]
                object.sprite.y = body["y"]
                object.direct = body["d"]
                #object.update_direct(body["d"])
              break
          continue

        if body["command"] == S_BULLET:
          if self.tank.id != body["id"]:
            new_bullet = Bullet(body["id"],body["x"], body["y"], body["d"], body["u"])
            self.map.add_anyway(new_bullet)
          continue

  def send(self):
    for event in self.map.get_events():
      if event.type is TYPE_TANK and event.id == self.tank.id:
        response = {
          "command": S_TANK,
          "id": event.id,
          "x": event.sprite.x,
          "y": event.sprite.y,
          "d": event.direct,
        }
        self.queue.push_out_wait(pickle.dumps(response))
        continue
      if event.type is TYPE_BULLET and event.parent == self.tank.id and event.status():
        response = {
          "command": S_BULLET,
          "d": event.direct,
          "x": event.x,
          "y": event.y,
          "id": event.parent,
          "u": event.damageBullet
        }
        self.queue.push_out_wait(pickle.dumps(response))
        continue

  def set(self, tank):
    self.tank = tank

  def set_objects(self, objects=[]):
    pass