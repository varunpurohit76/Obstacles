import pygame
import time

def car(x, y):
    gameDisplay.blit(carImg, (x, y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',50)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    game_loop()

def crash():
    message_display('You touched the walls')

def game_loop():
    x = display_width * 0.5
    y = display_height * 0.5
    dx = 0
    dy = 0
    exit_game = False

    while not exit_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx = -5
                elif event.key == pygame.K_RIGHT:
                    dx = 5
                elif event.key == pygame.K_UP:
                    dy = -5
                elif event.key == pygame.K_DOWN:
                    dy = 5
        
            if event.type == pygame.KEYUP:
                if (event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN):
                    dx = 0
                    dy = 0

        x += dx
        y += dy

        if (x < 0):
            x = 0 
        if (x + obj_width  > 800):
            x = 800 - obj_width
        if (y < 0):
            y = 0
        if (y + obj_height > 600):
            y = 600 - obj_height

        gameDisplay.fill(white)
        car(x, y)
        
        if x == 0 or x == (800 - obj_width):
            crash()

        pygame.display.update()
        clock.tick(60)

pygame.init()
display_width = 800
display_height = 600
obj_height = 49
obj_width = 50
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Game')
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
clock = pygame.time.Clock()
carImg = pygame.image.load('ball.png')
game_loop()
pygame.quit()
quit()
