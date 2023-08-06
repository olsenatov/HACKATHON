# import sys module
import pygame
import sys
# pygame.init() will initialize all
# imported module
pygame.init()
clock = pygame.time.Clock()
# it will display on screen
screen = pygame.display.set_mode([600, 500])
# basic font for user typed
base_font = pygame.font.Font(None, 32)
# create rectangle
input_rect = pygame.Rect(200, 200, 140, 32)
# color_active stores color(lightskyblue3) which
# gets active when input box is clicked by user
color_active = pygame.Color('black')
# color_passive store color(chartreuse4) which is
# color of input box.
color_passive = pygame.Color('red')
color = color_passive

    
def name_login():
    user_text = ''
    active = False
    
    # initial_message = "Input your name and press space to start the game"
    # initial_text_surface = base_font.render(initial_message, color_active, True, (0, 0, 0))
    # screen.blit(initial_text_surface, (input_rect.x+5, input_rect.y+5))
    while True:
        for event in pygame.event.get():
        # if user types QUIT then the screen will close
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif  event.type == pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                  return user_text
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False
            if event.type == pygame.KEYDOWN:
                # Check for backspace
                if event.key == pygame.K_BACKSPACE:
                    # get text input from 0 to -1 i.e. end.
                    user_text = user_text[:-1]
                # Unicode standard is used for string
                # formation
                else:
                    user_text += event.unicode
        # it will set background color of screen
        screen.fill((255, 255, 255))
        if active:
            color = color_active
        else:
            color = color_passive
        # draw rectangle and argument passed which should
        # be on screen
        # pygame.draw.rect(screen, color, input_rect)
        pygame.draw.rect(screen, color, input_rect)
        # text = base_font.render("This is the OPTIONS screen.", True, "Black")
        text_surface = base_font.render(user_text, True, (255, 255, 255))
        screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))
        input_rect.w = max(100, text_surface.get_width()+10)
        pygame.display.flip()
        clock.tick(60)