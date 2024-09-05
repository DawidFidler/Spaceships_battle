import pygame
import os

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game!")   #Title of window

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

BORDER = pygame.Rect(WIDTH/2-5, 0, 10, HEIGHT)        #Creating a rectangle which will be a border

FPS = 60
VELOCITY = 5
BULLET_VELOCITY = 8
MAX_BULLETS = 4
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40

YELLOW_HIT = pygame.USEREVENT + 1   #These way we have two seperate use events | gives us unique event id
RED_HIT = pygame.USEREVENT + 2      #

YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join("Assets", "spaceship_yellow.png"))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)     #Scaling and rotating an image

RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join("Assets", "spaceship_red.png"))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), -90)    #Scaling and rotating an image

SPACE = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "space.png")), (WIDTH, HEIGHT))

def draw_window(red, yellow, red_bullets, yellow_bullets):
    WIN.blit(SPACE, (0, 0))     #Background color
    pygame.draw.rect(WIN, BLACK, BORDER)    #Creating border in the middle of screen
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))      #Using blit I draw a surface onto the screen (i.e. images)
    WIN.blit(RED_SPACESHIP, (red.x, red.y))         #Instead of coordinates I will draw wherever red or yellow rectangles are
    
    for bullet in red_bullets:
        pygame.draw.rect(WIN, RED, bullet)
    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet)

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

def hadle_bullets(yellow_bullets, red_bullets, yellow, red):
    for bullet in yellow_bullets:
        bullet.x += BULLET_VELOCITY     #Bullet movement
        if red.colliderect(bullet):      #Checking if bullet hitting spaceship | function works if both objects are rectangles
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        elif bullet.x > WIDTH:        #When bullet if out of screen a new magazine is loaded
            yellow_bullets.remove(bullet)

    for bullet in red_bullets:
        bullet.x -= BULLET_VELOCITY     #Bullet movement
        if yellow.colliderect(bullet):      #Checking if bullet hitting spaceship | function works if both objects are rectangles
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)
        



def main():
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)      #Creating rectangles which represents our spaceships. This will actually allow to move them
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    red_bullets = []
    yellow_bullets = []

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)     #This will controll speed of our while loop
        for event in pygame.event.get():    #standard thing
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:    #key pressing for bullets
                if event.key == pygame.K_LALT and len(yellow_bullets) < MAX_BULLETS:   #Checking if number of bullets on screen is not grater the maximal number
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height/2, 10, 5)      #Creating bullet in the middle height of spaceship ath the right side 
                    yellow_bullets.append(bullet)
    
                if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(red.x, red.y + red.height/2, 10, 5)
                    red_bullets.append(bullet)
                    
    
        keys_pressed = pygame.key.get_pressed()     #Every single time this while loop is running and we reached this line it tells what key is curectly pressed down (Useful if key is being contonousle pressed)
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)
        
        hadle_bullets(yellow_bullets, red_bullets, yellow, red)

        draw_window(red, yellow, red_bullets, yellow_bullets)


    pygame.quit()

#if __name__ == "__main__":  #This way I run the game if I run the file directly
main()
