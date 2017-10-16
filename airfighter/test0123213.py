import pygame as pg
from random import *
from os import *
import pygame
import time
from color import *
from pygame import *
Aquamarine = (127,255,212)
Turquoise = (64,224,208)
white =(255,255,255)
black = (0,0,0)
red = (255,0,0)
yellow = (0,255,255)
# define window properties
WIDTH = 800
HEIGHT = 600
FPS = 90

pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption("DND again v2")
clock = pg.time.Clock()

def draw_text(surf,text,size,x,y,color):
    font = pg.font.SysFont("arial", size)
    text_surface =font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center =(x,y)
    surf.blit(text_surface,text_rect)

def button (msg,x,y,w,h,color,icolor,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x  and  y + h > mouse[1] > y:
        pygame.draw.rect (screen, color,(x,y,w,h))
        if click[0] ==1 and action != None:    
            action()
    else:
        pygame.draw.rect (screen, icolor,(x,y,w,h))

    draw_text (screen,msg,20, x + w/2 , y + h/2,white)

def btop(text, action=None):
    button (text,WIDTH/7.5,HEIGHT/5,WIDTH*0.7,HEIGHT*0.15,Aquamarine,Turquoise,action)

def bmid(text, action=None):
    button (text,WIDTH/7.5,HEIGHT*0.4,WIDTH*0.7,HEIGHT*0.15,Aquamarine,Turquoise,action)
def bbot(text, action=None):
    button (text,WIDTH/7.5,HEIGHT*0.6,WIDTH*0.7,HEIGHT*0.15,Aquamarine,Turquoise,action)

def cal():
    print ("Hello World")







running = True
while running:
    #keep loop running at the same speed
    clock.tick(FPS)
    # Process input (events)
    for event in pg.event.get():
        # check for closing window
        if event.type == pg.QUIT:
            running = False

    screen.fill(white)
    pg.display.flip()


pygame.quit()
quit()