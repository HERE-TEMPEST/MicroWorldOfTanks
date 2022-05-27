from typing import List
from random import randint

from blocks import *
from environment import *
from main_object import Object, TYPE_BANG, TYPE_BULLET, TYPE_TANK
from main_object.object import TYPE_BLOCK


class Map:

  def __init__(self):
    self.objects: List[Object] = []
    self.events = []
    pass

  def add_object(self, obje: Object):
    if obje.type is not TYPE_BANG and obje.type is not TYPE_BULLET:
      x = obje.sprite.x
      y = obje.sprite.y
      while True:
        rect = pygame.Rect(x, y, TILE, TILE)
        fined = False
        for obj in self.objects:
          if obj.type is not TYPE_BULLET and obj.type is not TYPE_BANG:
            if rect.colliderect(obj.sprite): fined = True
        if not fined: break
        x = randint(0, WIDTH - TILE)
        y = randint(0, HEIGHT - TILE)
      obje.sprite.x = x
      obje.sprite.y = y
      obje.id = obje.sprite.x * obje.sprite.y
    else:
      obje.id = obje.x * obje.y
    self.events.append(obje)
    self.objects.append(obje)

  def remove_object(self, obj):
    self.objects.remove(obj)
    if obj.type is TYPE_TANK:
      self.events.append(obj)


  def add_anyway(self, obj):
    self.objects.append(obj)
    self.events.append(obj)

  def random_generate_map(self, amount):
    for _ in range(amount):
      x = 0
      y = 0
      while True:
        x = randint(0, WIDTH // TILE - 1) * TILE
        y = randint(1, HEIGHT // TILE - 1) * TILE
        rect = pygame.Rect(x, y, TILE, TILE)
        fined = False
        for obj in self.objects:
            if rect.colliderect(obj.sprite): fined = True
        if not fined: break
      new_block = BrickBlock(x, y, TILE)
      type_block = randint(0, 4)
      if type_block == BUSHES_BLOCK:
        new_block = BushesBlock(x, y, TILE)
      if type_block == ARMOR_BLOCK:
        new_block = ArmorBlock(x, y, TILE)
      if type_block == WATER_BLOCK:
        new_block = WaterBlock(x, y, TILE)
      new_block.id = x * y
      self.objects.append(new_block)

  def load_from_file(self):
    pass


  def update_all(self):
    for object in self.objects:
      object.update(self)

  def flush(self):
    trash = list(filter(lambda obje: not obje.status(), self.objects))
    for _ in trash:
      self.objects.remove(_)
      if _.type is TYPE_TANK:
        self.events.append(_)

  def draw(self, window):
    for object in self.objects:
      if object.type is TYPE_TANK:
        object.draw(window)
    for object in self.objects:
      if object.type is not TYPE_TANK:
          object.draw(window)

  def clear_events(self):
    self.events = []

  def get_events(self):
    return self.events