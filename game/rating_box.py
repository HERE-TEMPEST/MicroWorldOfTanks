from environment import *


class RatingClass:
    def __init__(self):
        self.base_font = pygame.font.Font(None, 32)
        self.user_text = ''

        self.input_rect = pygame.Rect(450, 400, 140, 32)
        self.color_active = pygame.Color('lightskyblue3')
        self.color_passive = pygame.Color('chartreuse4')
        self.color = self.color_passive
  
        self.active = False

    def input_name(self):
        self.user_text = ""
        play = True
        while play:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.input_rect.collidepoint(event.pos):
                        self.active = True
                    else:
                        self.active = False
    
                if event.type == pygame.KEYDOWN:
                    if event.key == 13:
                        if self.user_text != "":
                            return self.user_text
                    
                    if event.key == pygame.K_BACKSPACE:
                        self.user_text = self.user_text[:-1]
                    else:
                        self.user_text += event.unicode
        
            window.blit(main_menu, (0, 0))
            self.draw_text('You are the Winner!', window, [450, 100], 60, (255, 255, 255), 'arial black')
            self.draw_text('Input your name: ', window, [450, 250], 50, (255, 255, 255), 'arial black')

            if self.active:
                color = self.color_active
            else:
                color = self.color_passive
        
            pygame.draw.rect(window, color, self.input_rect)
            text_surface = self.base_font.render(self.user_text, True, (255, 255, 255))
            window.blit(text_surface, (self.input_rect.x+5, self.input_rect.y+5))
            self.input_rect.w = max(100, text_surface.get_width()+10)
            pygame.display.flip()
            clock.tick(60)
    
    def draw_text(self, words, screen, position, size, colour, font_name, centered = False):
        font = pygame.font.SysFont(font_name, size)
        text = font.render(words, False, colour)
        text_size = text.get_size()
        if centered:
            position[0] = position[0] - text_size[0] // 2
            position[1] = position[1] - text_size[1] // 2
        screen.blit(text, position)
