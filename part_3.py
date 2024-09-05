import pygame
import os


WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game!")   #Title of window

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

BORDER = pygame.Rect(WIDTH/2-5, 0, 10, HEIGHT)        #Creating a rectangle which will be a border

FPS = 60
VELOCITY = 5
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40


YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join("Assets", "spaceship_yellow.png"))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)     #Scaling and rotating an image

RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join("Assets", "spaceship_red.png"))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), -90)    #Scaling and rotating an image

def draw_window(red, yellow):
    WIN.fill(WHITE)     #Background color
    pygame.draw.rect(WIN, BLACK, BORDER)    #Creating border in the middle of screen
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))      #Using blit I draw a surface onto the screen (i.e. images)
    WIN.blit(RED_SPACESHIP, (red.x, red.y))         #Instead of coordinates I will draw wherever red or yellow rectangles are
    pygame.display.update()     #We have to update the screen in order to draw new elements

def yellow_handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x > 0:
        yellow.x -= VELOCITY
    if keys_pressed[pygame.K_d] and (yellow.x + yellow.width) < BORDER.x:
        yellow.x += VELOCITY
    if keys_pressed[pygame.K_w] and yellow.y > 0:
        yellow.y -= VELOCITY
    if keys_pressed[pygame.K_s] and (yellow.y + yellow.height) < HEIGHT - 10:
        yellow.y += VELOCITY

def red_handle_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x > (BORDER.x + BORDER.width):
        red.x -= VELOCITY
    if keys_pressed[pygame.K_RIGHT] and red.x + red.width < WIDTH:
        red.x += VELOCITY
    if keys_pressed[pygame.K_UP] and red.y > 0 :
        red.y -= VELOCITY
    if keys_pressed[pygame.K_DOWN] and red.y + red.height < HEIGHT - 10:
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