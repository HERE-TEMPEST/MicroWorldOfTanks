import pygame
from .interface import UIInterface
from environment import *


class RulesMenu(UIInterface):

  def __init__(self):
    super().__init__()

  def start(self):
    rules = 'В управлении нет ничего сложного, для передвижения танчика,\nв различные стороны, помогут стрелки на клавиатуре,\nа стрелять по вражеским танкам, сможете с помощью кнопки F.\nДля того чтобы игра стала более интересной и захватывающей, можно играть\nс другом и уже ликвидировать врага на пару.\nВся гениальность игры заключается в отсутствии сюжета,\nно при этом в безумной увлекательности всего игрового процесса.'
    play = True
    while play:

      for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

      window.fill('black')
      window.blit(main_menu, pygame.Rect(0, 0, 1200, 700))
      window.blit(image_button_exit, pygame.Rect(480, 600, 250, 50))

      f3 = pygame.font.Font(None, 30)
      my_own_rules = f3.render(rules, True,
                (0, 0, 0))
      window.blit(my_own_rules, (300,300))

      pressed = pygame.mouse.get_pressed()
      x, y = pygame.mouse.get_pos()

      if pressed[0] and 480 < x < 730 and 600 < y < 650:
          return
      pygame.display.update()

  def exit(self):
    pass
