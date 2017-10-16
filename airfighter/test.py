import pygame
import time
import random
pygame.init()

crash_sound = pygame.mixer.Sound("crash.wav")
pygame.mixer.music.load("jazz.wav")


display_width = 800
display_height = 800

gamedisplay = pygame.display.set_mode((display_width,display_height))
# frame size
pygame.display.set_caption ('DND First Trial')
# title
clock = pygame.time.Clock ()
# time

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0, 255,0)
blue = (0,0,255)

pause = False
gamedisplay.fill(white)

carimg = pygame.image.load ('racecar.png')
pygame.display.set_icon(carimg) # 32*32 pixels
def car (x,y):
    gamedisplay.blit (carimg,(x,y))

def text_objects (text, font):
    textSurface = font.render(text,True,black)
    return textSurface, textSurface.get_rect()

def message_display (text):
    largetext = pygame.font.Font ('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects (text,largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gamedisplay.blit (TextSurf, TextRect)

    pygame.display.update ()
    time.sleep (3)
    game_loop ()

def crash ():
    message_display ('You crashed')

def things (x,y,w,h,color):
    pygame.draw.rect(gamedisplay, color,[x,y,w,h])


#print (mouse)
def button (msg,x,y,w,h,color,icolor,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x  and  y + h > mouse[1] > y:
        pygame.draw.rect (gamedisplay, color,(x,y,w,h))
        if click[0] ==1: and action != None:
            

            # if action == "play":
            #     game_loop()
            # elif action == "quit":
            #     pygame.quit()
            #     quit()
            
    else:
        pygame.draw.rect (gamedisplay, icolor,(x,y,w,h))

    smallText = pygame.font.Font('freesansbold.ttf',20)
    textSurf, textRect = text_objects (msg,smallText)
    textRect.center = (rect (x) + width/2 , rect(y) + height/2)
    gamedisplay.blit (textSurf,textRect)


def unpaused():
    global pause
    pygame.mixer.music.unpause()
    pause = False


def crashed ():
    pygmae.mixer.music.stop()
    pygame.mixer.music.play(crash_sound)

    # gamedisplay.fill(white)
    largetext = pygame.font.Font ('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects ("You Crashed",largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gamedisplay.blit (TextSurf, TextRect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        button ("Play again",150,450,100,50,green,bright_green,game_loop)
        button ("Quit",550,450,100,50,red,bright_red,quitgame)
        pygame.display.update()
        clock.tick(15)


def paused ():
    
    pygame.mixer.music.pause()
    # gamedisplay.fill(white)
    largetext = pygame.font.Font ('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects ("pause",largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gamedisplay.blit (TextSurf, TextRect)

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        button ("Continue",150,450,100,50,green,bright_green,unpause)
        button ("Quit",550,450,100,50,red,bright_red,quitgame)
        pygame.display.update()
        clock.tick(15)



def game_intro ():
    intro = True
    largetext = pygame.font.Font ('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects (text,largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gamedisplay.blit (TextSurf, TextRect)
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        # gamedisplay.fill(white)
        
        pygame.display.update()
        clock.tick(15)




def game_loop():
    global pause
    pygame.mixer.music.play(-1)
    x = display_width * 0.45
    y = display_height * 0.8
    x_change = 0

    thing_x = random.range(0,display_width)
    thing_y = -600
    thing_speed = 7
    thing_w = 100
    thing_h = 100
    
    gameExit = False
    while not gameExit:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_left:
                    x_change = -5
                if event.key == pygame.K_right:
                    x_change = 5 
                if event.key == py.game.K_p:
                    pause = True
                    paused () 
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_left or event.key == pygame.K_right:
                    x_change = 0



            print (event)
        pygame.display.update()
        clock.tick(60)
    x += x_change
    gamedisplay.fill(white)
    
    things (thing_x, thing_y,thing_w,thing_h, black)
    thing_y += thing_speed

    if x > display_width -car_width or x < 0 :
        crash()

    if thing_y > display_height:
        thing_y = 0 - thing_h
        thing_x = random.randrange(0,display_width)
    car (x,y)

    

game_intro()
game_loop()
pygame.quit()
quit()
