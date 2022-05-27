from typing import List, Sequence
import pygame

from tank import Tank
from .controller import Controller, TYPE_HUMAN
from main_object import Object

class PlayerController(Controller):
  def __init__(self) -> None:
    super().__init__(TYPE_HUMAN)
    self.tank: Tank = None
    self.objects = None
    self.left: int = 0
    self.right: int = 0
    self.up: int = 0
    self.down: int = 0
    self.shoot: int = 0
    self.__events = List[Sequence]

  def set_left(self, event):
    self.left = event

  def set_right(self, event):
    self.right = event

  def set_up(self, event):
    self.up = event

  def set_down(self, event):
    self.down = event

  def set_shoot(self, event):
    self.shoot = event

  def events(self, events):
    self.__events = events

  def set(self, tank):
    self.tank = tank

  def set_objects(self, objects: List[Object] = []):
    self.objects = objects

  def update(self, objects = []):
    if self.__events[self.left]:
      self.tank.update_direct(3)
    if self.__events[self.right]:
      self.tank.update_direct(1)
    if self.__events[self.up]:
      self.tank.update_direct(0)
    if self.__events[self.down]:
      self.tank.update_direct(2)
    if self.__events[self.shoot]:
      self.tank.shoot()
