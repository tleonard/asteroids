import pygame
from constants import *

def main():
    print (f"""
           Starting asteroids!
           Screen width: {SCREEN_WIDTH}
           Screen height: {SCREEN_HEIGHT}
           """)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        screen.fill(color="black")
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
if __name__ == "__main__":
    main()