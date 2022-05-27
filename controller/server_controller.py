import pickle
from random import randint
import time
from main_object import TYPE_BANG, TYPE_BLOCK, TYPE_BULLET, TYPE_TANK

from protocols import Request, Response
from tank import Tank
from tank.bullet.bullet import Bullet
from .controller import Controller, TYPE_SERVER
from map import Map
from interworking import DuplexQueue

CONNECTED = 0
DISCONNECTED = 100
BLOCK = 1
TANK = 2
BULLET = 4
END_CHUNK = 3
S_TANK = 5
S_BULLET = 6
S_BLOCK = 7


class ServerController(Controller):
  def __init__(self, map: Map, queue: DuplexQueue):
    super().__init__(TYPE_SERVER)
    self.queue = queue
    self.tank = None
    self.map = map
  
  def update(self):
    count = 20
    while count != 0:
      count -= 1
      message: Request = self.queue.shift_in()
      if message is not None:
        body = pickle.loads(message.body)

        if body["command"] is S_TANK:
          for object in self.map.objects:
            if object.id == body["id"] and object.type is TYPE_TANK:
              object.sprite.x = body["x"]
              object.sprite.y = body["y"]
              object.direct = body["d"]
              break
          continue

        if body["command"] is DISCONNECTED:
          for object in self.map.objects:
            if object.id == body["id"] and object.type is TYPE_TANK:
              object.set_status(False)
              break
          continue


        if body["command"] is S_BULLET:
          new_bullet = Bullet(body["id"], body["x"], body["y"], body["d"], body["u"]) 
          self.map.add_anyway(new_bullet)
          continue

        if body["command"] is CONNECTED:
          tank = Tank(0, 0)
          tank.level = randint(0, 7)
          self.map.add_object(tank)
          response = Response(message.id, pickle.dumps({"command": CONNECTED, "u": tank.bulletDamage ,"id": tank.id, "x": tank.sprite.x, "y": tank.sprite.y, "l": tank.level, "secret": body["secret"]}))
          self.queue.push_out_wait(response)
          for object in self.map.objects:
            if object.type is TYPE_BLOCK or object.type is TYPE_TANK or object.type is TYPE_BULLET:
              body = None
              if object.type is TYPE_BLOCK:
                body = {
                  "command": BLOCK,
                  "x": object.sprite.x,
                  "y": object.sprite.y,
                  "id": object.id,
                  "type": object.type_block,
                }
              elif object.type is TYPE_TANK and object.id != tank.id:
                body = {
                  "command": TANK,
                  "x": object.sprite.x,
                  "y": object.sprite.y,
                  "id": object.id,
                  "l": object.level,
                  "u": object.bulletDamage
                }
              elif object.type is TYPE_BULLET:
                body = {
                  "command": BULLET,
                  "x": object.x,
                  "y": object.y,
                  "d": object.direct,
                  "u": object.damageBullet,
                  "id": object.parent
                }
              if body is not None:
                res = Response(message.id, pickle.dumps(body))
                self.queue.push_out_wait(res)
                time.sleep(0.005)
          last_res = Response(message.id, pickle.dumps({ "command": END_CHUNK }))
          self.queue.push_out_wait(last_res)


  def send(self):
    for object in self.map.events:
      time.sleep(0.001)
      if object.type is TYPE_TANK:
        response = {
          "command": S_TANK,
          "id": object.id,
          "x": object.sprite.x,
          "y": object.sprite.y,
          "d": object.direct,
          "s": object.status()
        }
        self.queue.push_out_wait(Response(999, pickle.dumps(response)))
        continue
      if object.type is TYPE_BULLET:
        response = {
          "command": S_BULLET,
          "x": object.x,
          "y": object.y,
          "d": object.direct,
          "u": object.damageBullet,
          "id": object.parent
        }
        self.queue.push_out_wait(Response(999, pickle.dumps(response)))
        continue

  def set(self, tank):
    self.tank = tank

  def set_objects(self, objects=[]):
    pass