import pygame
import os


WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game!")   #Title of window

WHITE = (255, 255, 255)
FPS = 60
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40


YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join("Assets", "spaceship_yellow.png"))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)     #Scaling and rotating an image

RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join("Assets", "spaceship_red.png"))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), -90)    #Scaling and rotating an image

def draw_winow():
        WIN.fill(WHITE)     #Background color
        WIN.blit(YELLOW_SPACESHIP, (300, 100))      #Using blit I draw a surface onto the screen (i.e. images)
        WIN.blit(RED_SPACESHIP, (700, 100))
        pygame.display.update()     #We have to update the screen in order to draw new elements


def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)     #This will controll speed of our while loop
        for event in pygame.event.get():    #standard thing
            if event.type == pygame.QUIT:
                run = False
    
        draw_winow()



    pygame.quit()

if __name__ == "__main__":  #This way I run the game if I run the file directly
    main()