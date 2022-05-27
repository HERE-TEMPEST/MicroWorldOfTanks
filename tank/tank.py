from random import randint
from typing import List

from map.map import Map


from .bullet import Bullet
from environment import *
from main_object import *

class Tank(Object):
    def __init__(self, x, y):
        super().__init__(TYPE_TANK)
        self.sprite = pygame.Rect(x, y, TILE, TILE)
        self.direct = 0
        self.moveSpeed = 1
        self.hp = HP_TANK
        self.__status = True
        self.radius_view = 200

        self.__event_shoot = False
        self.__move = False
        self.shotTimer = 0
        self.shotDelay = 100
        self.bulletSpeed = 5
        self.bulletDamage = 1

        self.score = 0

        self.level = 0
        self.image = pygame.transform.rotate(imgTanks[self.level], - self.direct * 90)
        self.sprite = self.image.get_rect(center = self.sprite.center)

    def update_direct(self, direct):
      self.__move = True
      self.direct = direct

    def shoot(self):
      self.__event_shoot = True

    def update(self, map: Map):
        self.image = pygame.transform.rotate(imgTanks[self.level], -self.direct * 90)
        self.image = pygame.transform.scale(self.image, (self.image.get_width() - 5, self.image.get_height() - 5))
        self.sprite = self.image.get_rect(center = self.sprite.center)

        if self.__move is True:
          oldX, oldY = self.sprite.topleft
          self.sprite.x += DIRECTS[self.direct][0] * self.moveSpeed
          self.sprite.y += DIRECTS[self.direct][1] * self.moveSpeed

          if self.sprite.x < 0 or self.sprite.x + 32 > WIDTH or self.sprite.y < 0 or self.sprite.y + 32 > HEIGHT:
            self.sprite.topleft = oldX, oldY
          else:
            for obj in map.objects:
                if obj != self and obj.colliderect(self):
                    self.sprite.topleft = oldX, oldY
            self.__move = False
          
          map.events.append(self)

        if self.__event_shoot is True and self.shotTimer == 0:
            sounds["babah"].play()
            speed_bullet = [DIRECTS[self.direct][0] * self.bulletSpeed, DIRECTS[self.direct][1] * self.bulletSpeed]
            bullet = Bullet(self.id, self.sprite.centerx, self.sprite.centery, speed_bullet, self.bulletDamage)
            map.add_anyway(bullet)
            self.shotTimer = self.shotDelay
        self.__event_shoot = False

        if self.shotTimer > 0: self.shotTimer -= 1

    def draw(self, window):
        window.blit(self.image, self.sprite)

    def status(self):
        return self.__status


    def set_status(self, status):
        self.__status = status

    def damage(self, value = 0):
      self.hp -= value
      sounds["shot"].play()
      if self.hp <= 0:
        sounds["dead"].play()
        self.__status = False

    def collidepoint(self, x, y):
        return self.sprite.collidepoint(x, y)

    def colliderect(self, object):
        return self.sprite.colliderect(object.sprite)



class TankBuilder:

  tank = Tank(0, 0)

  def set_level(amount):
    TankBuilder.tank.level = amount

  def set_damage(amount):
    TankBuilder.tank.bulletDamage = amount

  def set_speed(amount):
    TankBuilder.tank.moveSpeed = amount

  def set_health(amount):
    TankBuilder.tank.hp = amount

  def set_shot_delay(amount):
    TankBuilder.tank.shotDelay = amount

  def get_result():
    tank = TankBuilder.tank
    TankBuilder.tank = Tank(0, 0)
    return tank
    
    
  def custom_level_1():
    return TankBuilder.get_result()

  def custom_level_2():
    TankBuilder.tank.bulletDamage = 3
    TankBuilder.tank.moveSpeed = 1
    TankBuilder.tank.level = 2
    return TankBuilder.get_result()

  def custom_level_3():
    TankBuilder.tank.bulletDamage = 3
    TankBuilder.tank.moveSpeed = 1
    TankBuilder.tank.level = 2
    return TankBuilder.get_result()

  def custom_level_4():
    TankBuilder.tank.bulletDamage = 0.5
    TankBuilder.tank.moveSpeed = 1
    TankBuilder.tank.level = 4
    TankBuilder.tank.hp = 15
    return TankBuilder.get_result()

  def custom_level_5():
    TankBuilder.tank.moveSpeed = 3
    TankBuilder.tank.level = 5
    return TankBuilder.get_result()

  def custom_level_6():
    TankBuilder.tank.level = 6
    TankBuilder.tank.moveSpeed = 1
    TankBuilder.tank.bulletDamage = 2
    TankBuilder.tank.shotDelay = 70
    return TankBuilder.get_result()
    
  def custom_level_7():
    TankBuilder.tank.bulletDamage = 1
    TankBuilder.tank.moveSpeed = 1
    TankBuilder.tank.level = 7
    TankBuilder.tank.hp = 8
    return TankBuilder.get_result()

  def random_generate(level = 0):
    level = randint(1, 7)
    if level is 1:
      return TankBuilder.custom_level_1()
    if level is 2:
      return TankBuilder.custom_level_2()
    if level is 3:
      return TankBuilder.custom_level_3()
    if level is 4:
      return TankBuilder.custom_level_4()
    if level is 5:
      return TankBuilder.custom_level_5()
    if level is 6:
      return TankBuilder.custom_level_6()
    if level is 7:
      return TankBuilder.custom_level_7()
    return TankBuilder.get_result()
