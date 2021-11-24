import pygame, sys
from pygame.constants import K_ESCAPE, KEYDOWN, QUIT

def main():

    #Constants
    RED = (255,0,0)
    GREEN = (0,255,0)
    BLUE = (0,0,255)
    MAIN_SCREEN_COLOR = (53,136,208)
    WINDOW_SIZE = (600,400)

    #Declarations
    clock = pygame.time.Clock()
    pygame.display.set_caption('Platformer')
    
    screen = pygame.display.set_mode(WINDOW_SIZE,0,32)
    display = pygame.Surface((300,200))

    player_image = pygame.image.load('2D Platformer/Lumberjack.png')
    #ground = pygame.image.load('2D Platformer/Platform.png')

    while True:
        
        display.fill(MAIN_SCREEN_COLOR)
        display.blit(player_image, (10,190))
        

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        surf = pygame.transform.scale(display, WINDOW_SIZE)
        screen.blit(surf, (0,0))
        pygame.display.update()
        clock.tick(60)

main()