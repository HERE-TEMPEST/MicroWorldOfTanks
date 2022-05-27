from typing import List

from environment import *
from effects import Bang
from map.map import Map
from main_object import *

class Bullet(Object):
    def __init__(self, parent, x, y, direct, damage):
        super().__init__(TYPE_BULLET)
        self.parent = parent
        self.x = x
        self.y = y
        self.direct = direct
        self.damageBullet = damage
        self.__status = True

    def update(self, map: Map):
        self.x += self.direct[0]
        self.y += self.direct[1]

        if self.x < 0 or self.x > WIDTH or self.y < 0 or self.y > HEIGHT:
          self.__status = False
        else:
          for obj in map.objects:
            if obj.id != self.parent and obj.collidepoint(self.x, self.y):
              obj.damage(self.damageBullet)
              if not obj.status():
                for obj in map.objects:
                  if obj.id == self.parent and obj.type is TYPE_TANK:
                    obj.score += 100
              map.add_object(Bang(self.x, self.y))
              self.__status = False
              break

    def draw(self, window):
      pygame.draw.circle(window, 'yellow', (self.x, self.y), 2)

    def status(self):
        return self.__status
