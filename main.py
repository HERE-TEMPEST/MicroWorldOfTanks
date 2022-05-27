from menu import *

if __name__ == '__main__':
    menu = MainMenu(GameMenu(), RulesMenu(), RatingMenu(), SoundsMenu())
    menu.start()
