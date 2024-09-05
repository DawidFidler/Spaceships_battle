import pygame
import os


WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game!")   #Title of window

WHITE = (255, 255, 255)
FPS = 60
VELOCITY = 5
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40


YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join("Assets", "spaceship_yellow.png"))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)     #Scaling and rotating an image

RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join("Assets", "spaceship_red.png"))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), -90)    #Scaling and rotating an image

def draw_window(red, yellow):
    WIN.fill(WHITE)     #Background color
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))      #Using blit I draw a surface onto the screen (i.e. images)
    WIN.blit(RED_SPACESHIP, (red.x, red.y))         #Instead of coordinates I will draw wherever red or yellow rectangles are
    pygame.display.update()     #We have to update the screen in order to draw new elements

def yellow_handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a]:
        yellow.x -= VELOCITY
    if keys_pressed[pygame.K_d]:
        yellow.x += VELOCITY
    if keys_pressed[pygame.K_w]:
        yellow.y -= VELOCITY
    if keys_pressed[pygame.K_s]:
        yellow.y += VELOCITY

def red_handle_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT]:
        red.x -= VELOCITY
    if keys_pressed[pygame.K_RIGHT]:
        red.x += VELOCITY
    if keys_pressed[pygame.K_UP]:
        red.y -= VELOCITY
    if keys_pressed[pygame.K_DOWN]:
        red.y += VELOCITY

def main():
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)      #Creating rectangles which represents our spaceships. This will actually allow to move them
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)     #This will controll speed of our while loop
        for event in pygame.event.get():    #standard thing
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()     #Every single time this while loop is running and we reached this line it tells what key is curectly pressed down (Useful if key is being contonousle pressed)
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)
        
        
        draw_window(red, yellow)


    pygame.quit()

#if __name__ == "__main__":  #This way I run the game if I run the file directly
main()