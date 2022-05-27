from typing import List
import time

from controller import Controller
from controller.controller import TYPE_BOT, TYPE_CLIENT, TYPE_HUMAN, TYPE_SERVER
from main_object import Object
from map import Map

from menu import UIInterface

from environment import *
from tank import Tank

from rating import modelRatings
from .rating_box import RatingClass

class Game(UIInterface):

  def __init__(self, ui: Object, tank: Tank, map: Map, controllers: List[Controller] = []):
    self.controllers = controllers
    self.tank = tank
    self.ui = ui
    self.map = map

  def start(self):
    sounds["background_game"].play()
    play = True
    while play:

      self.map.clear_events()
      
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              play = False

      self.map.update_all()
      self.map.flush()

      keys = pygame.key.get_pressed()
      for controller in self.controllers:
        if controller.type is TYPE_BOT: 
          controller.update(self.map)
        elif controller.type is TYPE_HUMAN:
          controller.events(keys)
          controller.update()
        elif controller.type is TYPE_SERVER:
          controller.update()
          controller.send()
        elif controller.type is TYPE_CLIENT:
          controller.update()
          controller.send()

      if not self.tank.status():
        break

      window.fill('black')
      
      self.ui.update(self.tank, self.map.objects)
      self.map.draw(window)

      self.ui.draw(window)      
      pygame.display.update()
      clock.tick(FPS)
    time.sleep(2)
    sounds["background_game"].stop()

    if modelRatings.get_max() < self.tank.score:
      box = RatingClass()
      user_name = box.input_name()
      modelRatings.append(user_name, self.tank.score)
      modelRatings.save_file("./ratings.xml")

  def exit(self):
    pass