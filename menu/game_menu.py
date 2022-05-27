import multiprocessing
from random import randint
import socket
import pickle

from interworking import DuplexQueue, ICMessageBroker, ISMessageBroker
from tank.bullet.bullet import Bullet
from tank.tank import TankBuilder
from .interface import UIInterface

from environment import *

import time

from game import Game
from blocks import *
from controller import TankBot, PlayerController, ClientController, ServerController
from map import Map
from tank import Tank
from game import UIGame


def start_client(queue, env):
  hostname = socket.gethostbyname(socket.gethostname())
  broker = ICMessageBroker(hostname, 5050, queue)
  try:
    broker.start()
    env.put("work")
    env.get(block=True)
    broker.close()
    queue.close()
    return
  except BaseException:
    env.put("error")
    return

def start_server(queue, env):
  hostname = socket.gethostbyname(socket.gethostname())
  broker = ISMessageBroker(hostname, 5050, queue)
  try:
    broker.start()
    env.put("work")
    env.get(block=True)
    broker.close()
    queue.close()
    return
  except BaseException:
    env.put("error")
    return



class GameMenu(UIInterface):

  def __init__(self):
    pass

  def start(self):
    play = True
    while play:

      for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False


      window.fill('black')
      window.blit(main_menu, pygame.Rect(0, 0 , 1200, 700))

      window.blit(image_button_volume, pygame.Rect(480, 250 , 250, 50))
      window.blit(image_button_russian, pygame.Rect(480, 310 , 250, 50))
      window.blit(image_button_germany, pygame.Rect(480, 370 , 250, 50))
      window.blit(image_button_exit, pygame.Rect(480, 430 , 250, 50))


      pressed = pygame.mouse.get_pressed()
      x, y = pygame.mouse.get_pos()
 
      # event Local Game
      if pressed[0] and 502 < x and x < 700 and 251 < y and y < 292:

        map = Map()
        map.random_generate_map(200)

        player_tank = TankBuilder.random_generate()

        controller_for_bots = TankBot()
        player_controller = PlayerController()

        player_controller.set_left(LEFT)
        player_controller.set_right(RIGHT)
        player_controller.set_up(UP)
        player_controller.set_down(DOWN)
        player_controller.set_shoot(SHOOT)

        player_controller.set(player_tank)
        controller_for_bots.set(player_tank)
        map.add_object(player_tank)

        ui = UIGame()
        game = Game(ui, player_tank, map, [controller_for_bots, player_controller])
        game.start()
        return

      try:
        # event Create Server
        if pressed[0] and 502 < x and x < 700 and 310 < y and y < 352:
          env = multiprocessing.Queue()
          queue = DuplexQueue()
          process = multiprocessing.Process(target=start_server, args=(queue, env))
          process.start()

          if env.get() == "error":
            process.join()
            continue

          map = Map()
          map.add_object(tank)
          map.random_generate_map(200)

          player_controller = PlayerController()
          server_controller = ServerController(map, queue)

          player_controller.set_left(LEFT)
          player_controller.set_right(RIGHT)
          player_controller.set_up(UP)
          player_controller.set_down(DOWN)
          player_controller.set_shoot(SHOOT)


          ui = UIGame()
          game = Game(ui, tank, map, [player_controller, server_controller])
          game.start()

          env.put("message")
          process.join()
          return
      except BaseException:
        env.put("message")
        process.join()
        return
        
      try:
        # event Connect to Server
        if pressed[0] and 502 < x and x < 700 and 374 < y and y < 414:
          env = multiprocessing.Queue()
          queue = DuplexQueue()
          process = multiprocessing.Process(target=start_client, args=(queue, env))
          process.start()

          if env.get() == "error":
            process.join()
            print("error in connection")
            continue
          
          secret = randint(0, 1000)
          messgae = {
            "command": 0,
            "secret": secret,
          }
          queue.push_out_wait(pickle.dumps(messgae))

          tank = Tank(0, 0)
          while True:
            message = queue.shift_in_wait()
            body = pickle.loads(message)
            if body["command"] == 0 and body["secret"] == secret:
              tank.sprite.x = body["x"]
              tank.sprite.y = body["y"]
              tank.id = body["id"]
              tank.level = body["l"]
              tank.bulletDamage = body["u"]
              break

          map = Map()
          map.add_object(tank)

          # get all objects from server (pre-load)
          while True:
            message = queue.shift_in_wait()
            body = pickle.loads(message)
            if body["command"] == 3:
              break
            elif body["command"] == 1:
              block = BrickBlock(body["x"], body["y"], TILE)
              if body["type"] == BUSHES_BLOCK:
                block = BushesBlock(body["x"], body["y"], TILE)
              elif body["type"] == ARMOR_BLOCK:
                block = ArmorBlock(body["x"], body["y"], TILE)
              elif body["type"] == WATER_BLOCK:
                block = WaterBlock(body["x"], body["y"], TILE)
              block.id = body["id"]
              map.add_anyway(block)
            elif body["command"] == 2:
              new_tank = Tank(body["x"], body["y"])
              new_tank.level = body["l"]
              new_tank.id = body["id"]
              new_tank.bulletDamage = body["u"]
              map.add_anyway(new_tank)
            elif body["command"] == 4:
              bullet = Bullet(body["id"], body["x"], body["y"], body["d"], body["u"])
              map.add_anyway(bullet)
              pass
            
          player_controller = PlayerController()
          player_controller.set_left(LEFT)
          player_controller.set_right(RIGHT)
          player_controller.set_up(UP)
          player_controller.set_down(DOWN)
          player_controller.set_shoot(SHOOT)
          player_controller.set(tank)

          client_controller = ClientController(map, queue)
          client_controller.set(tank)

          ui = UIGame()
          game = Game(ui, tank, map, [client_controller, player_controller])
          game.start()

          # event DISCONNECT
          queue.push_out_wait({ "command": 100, "id": tank.id })

          time.sleep(1)
          env.put("message")
          process.join()
          return
      except BaseException:
        env.put("message")
        process.join()
        return

      if pressed[0] and 502 < x and x < 700 and 444 < y and y < 478:
        return
      pygame.display.update()


  def exit(self):
    pass
