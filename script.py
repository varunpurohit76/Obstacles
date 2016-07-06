import pygame
import time
import random

def car(x, y):
    gameDisplay.blit(carImg, (x, y))

def text_objects(text, font):
    textSurface = font.render(text, True, red)
    return textSurface, textSurface.get_rect()

def obstacle(obstacle_x, obstacle_y, obstacle_w, obstacle_h, obstacle_c):
    pygame.draw.rect(gameDisplay, obstacle_c, [obstacle_x, obstacle_y, obstacle_w, obstacle_h])

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',50)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(4)
    game_loop()

def display_score(score):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Score : "+str(score), True, red)
    gameDisplay.blit(text,(0,0))

def crash():
    pygame.mixer.Sound.play(crash_sound)
    pygame.mixer.music.stop()
    message_display('You crashed bruh!')

def game_loop():
    pygame.mixer.music.load('resources/music.wav')
    pygame.mixer.music.play(-1)
    x = display_width * 0.5
    y = display_height * 0.5
    dx = 0
    dy = 0
    
    obstacle_x = random.randrange(0, display_width)
    obstacle_y = -600
    obstacle_speed = 5
    obstacle_w = 100
    obstacle_h = 100
    obstacle_horizontal_x = -600
    obstacle_horizontal_y = random.randrange(0, display_height)
    obstacle_horizontal_speed = 5
    obstacle_horizontal_w = 100
    obstacle_horizontal_h = 100
    score_start_time = time.time()   

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
            
        obstacle(obstacle_x, obstacle_y, obstacle_w, obstacle_h, black)
        obstacle_y += obstacle_speed

        obstacle(obstacle_horizontal_x, obstacle_horizontal_y, obstacle_horizontal_w, obstacle_horizontal_h, black)
        obstacle_horizontal_x += obstacle_horizontal_speed

        if obstacle_y >= display_height:
            obstacle_y = 0 - obstacle_h
            obstacle_x = random.randrange(0, display_width)
            obstacle_speed += 0.75
            obstacle_w *= 1.1
        
        if obstacle_horizontal_x >= display_width:
            obstacle_horizontal_y = random.randrange(0, display_height)
            obstacle_horizontal_x = 0 - obstacle_horizontal_w
            obstacle_horizontal_h *= 1.1

        car(x, y)
        display_score("%0.1f" % (time.time() - score_start_time))
        
        if y < (obstacle_y + obstacle_h) and (y + obj_height) > obstacle_y:
            if x > obstacle_x and x < obstacle_x + obstacle_w or x + obj_width > obstacle_x and x + obj_width < obstacle_x + obstacle_w:
                crash()

        if obstacle_horizontal_x + obstacle_horizontal_w > x and obstacle_horizontal_x < x + obj_width:
            if y < obstacle_horizontal_y and y + obj_height > obstacle_horizontal_y or y > obstacle_horizontal_y and y < obstacle_horizontal_y + obstacle_horizontal_h:
                crash()

        pygame.display.update()
        clock.tick(60)

pygame.init()
crash_sound = pygame.mixer.Sound('resources/crash.wav')
display_width = 800
display_height = 600
obj_height = 50
obj_width = 50
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Game')
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
clock = pygame.time.Clock()
carImg = pygame.image.load('resources/obj.png')
game_loop()
pygame.quit()
quit()
