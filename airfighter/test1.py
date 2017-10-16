import pygame as pg
import random
import os
import pygame
from color import *




WIDTH = 800
HEIGHT = 600
FPS = 90
# define colors
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0, 255,0)
blue = (0,0,255)



# set up assets folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")



# initializing pygame and create window 
pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption("DND again v2")
clock = pg.time.Clock()

def draw_text(surf,text,size,x,y):
    font = pg.font.SysFont("arial", size)
    text_surface =font.render(text, True, black)
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

    draw_text (screen,msg,20, x + w/2 , y + h/2)

def quitf():
    pg.quit()
    quit()




class Player (pg.sprite.Sprite):
    # sprite of the Player
    def __init__(self,race):
        pg.sprite.Sprite.__init__(self)
        # self.image = pg.Surface ((50,50))
        # self.image = pg.image.load (os.path.join (img_folder, "p1_jump.png")).convert()
        # self.image.set_colorkey(white)
        # # self.image.fill (green)
        # self.rect = self.image.get_rect()
        # self.rect.center = (WIDTH/2, HEIGHT/2)
        self.attribute = {'strength':0, 'dexterity':0, 'widsom':0}
        index = [0.8,0.5,0.3]    # usage of attribute
        if race == "orc":
            self.buff = [1.3,1.1,0.8,0.5] # hp buff, strength buff,dex debuff, widsom debuff 
            self.maxhp = (100 + attribute['strength']*index[0]) *self.buff[0]


        if race == "human":
            self.hp = 100
        if race == "elf":
            self.hp = 100
        
        
        
        
        self.exp = 0
        
        self.item_list = []
        self.equipped_list = []
                
        # # self.y_speed = 5
        # self.speedy = 0
        # self.speedx = 0
        # self.shield = 100
    def levelup():
        if self.exp > 100*self.level:
            levelup = True

    def update(self):
        self.speedx =0
        self.speedy = 0
        keystate = pg.key.get_pressed()
        if keystate[pg.K_LEFT]:
            self.speedx = -5
        if keystate[pg.K_RIGHT]:
            self.speedx = 5
        if keystate[pg.K_UP]:
            self.speedy = -5
        if keystate[pg.K_DOWN]:
            self.speedy = 5
        
        if levelup:
            self.exp -= 100*self.level
            self.level += 1
            self.hp += 50 * self.buff[0]        
        
        self.rect.x += self.speedx
        self.rect.y += self.speedy

all_sprites = pg.sprite.Group()
player = Player()
all_sprites.add(player)

running = True
while running:
    #keep loop running at the same speed
    clock.tick(FPS)
    # Process input (events)
    for event in pg.event.get():
        # check for closing window
        if event.type == pg.QUIT:
            running = False


    # Update
    all_sprites.update()


    # draw and render
    screen.fill(white)
    # draw_text(screen,"Hello world",50,400,300)             both functions work perfectly fine
    # button("hello world",400,300,100,100,Color.Salmon,Color.Orange,quitf)
    pg.display.flip()



quitf()
