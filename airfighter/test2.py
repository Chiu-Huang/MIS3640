import pygame as pg
import random
import os
import pygame
from color import *


# define window properties
WIDTH = 800
HEIGHT = 600
FPS = 90
# define colors
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0, 255,0)
blue = (0,0,255)
Aquamarine = (127,255,212)
Turquoise = (64,224,208)
# set up assets folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")

# initializing pygame and create window 
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






def dice(x):
    return random.randint(1,x)


def menu():
    pg.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            if event.type == pg.KEYUP:
                waiting = False
def gameover():
    bmid("You died... Please insert coins to play again!",quitf)
    pg.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pg.QUIT:
                pg.quit()





def quitf():
    pg.quit()
    quit()


#Define Global Variables
index = [0.8,0.5,0.3]    # usage of attribute
levelup = False
class Player (pg.sprite.Sprite):
    # sprite of the Player
    global index
    global levelup


    def dice_attribution(self,x):
        for i in self.attribute:
            k = 1
            for roll_times in range (0,k,1):
                self.attribute[i] += dice(x)


    def __init__(self,race):
        pg.sprite.Sprite.__init__(self)
        self.attribute = {'strength':0, 'dexterity':0, 'wisdom':0}
        self.level = 1
        # def dice_attribution(x):
        #     for i in self.attribute:
        #         k = int(input("How many dices do you want to allocate to {}?".format(i)))
        #         for roll_times in range (0,k,1):
        #             self.attribute[i] += dice(x)

        Player.dice_attribution(self, 18)
        # race formation
        if race == "orc":
            self.buff = [1.3,1.1,0.8,0.5] # hp buff, strength buff,dex debuff, widsom debuff 
        if race == "human":
            self.buff = [1,1,11,1.5] # hp buff, strength buff,dex debuff, widsom debuff
        if race == "elf":
            self.buff = [0.9,1.1,1.4,1.2] # hp buff, strength buff,dex debuff, widsom debuff
        
        # hp formula
        k = (50 * self.level + self.attribute['strength']*index[0]) *self.buff[0]
        self.maxhp = round (k,0)
        self.hp = self.maxhp
        self.exp = 0
        self.gold = 1000
        self.item_list = []
        self.equipped_list = []
        
    def expgain(self):
        self.exp += 100
    # def minushp(self):
    #     self.hp = 0
    def update(self):
        global levelup
        if self.exp >= 100 * (self.level):
            levelup = True
        if levelup:
            self.exp -= 100*self.level
            self.level += 1
            Player.dice_attribution(self,5)
            self.maxhp = round ((50 * self.level + self.attribute['strength']*index[0]) *self.buff[0],0)
            self.hp = self.maxhp    #renew hp
            levelup = False     



class Monster (pg.sprite.Sprite):
    # sprite of the Player
    global index
    global levelup

    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.attribute = {'strength':0, 'dexterity':0, 'wisdom':0}
        self.level = random.randint(1,5)
        # def dice_attribution(x):
        #     for i in self.attribute:
        #         k = int(input("How many dices do you want to allocate to {}?".format(i)))
        #         for roll_times in range (0,k,1):
        #             self.attribute[i] += dice(x)

        Player.dice_attribution(self, 18)        
        # hp formula
        k = (30 * self.level + self.attribute['strength']*index[0])
        self.maxhp = round (k,0)
        self.hp = self.maxhp
        self.exp = 20 + self.level * random.randint(30,50)
        self.gold = 50 + self.level * random.randint(0,200)
        self.item_list = []
        
    def minushp(self):
        self.hp = 0

    def update(self):
        if self.hp <= 0:
            player.gold += self.gold
            player.exp +=self.exp
            self.kill()
            


        
    # def update(self):
# Load all game graphics
# menu = pg.image.load('menu.png')
# menu_rect = menu.get_rect()




all_sprites = pg.sprite.Group()
player = Player("orc")
all_sprites.add(player)
monsters = pygame.sprite.Group()
for i in range (0,8,1):
    monster1 = Monster()
    monsters.add(monster1)










# Game Loop
running = True
while running:
    #keep loop running at the same speed
    clock.tick(FPS)
    Menu = True
    
    # Process input (events)
    if player.hp <= 0:
        gameover()
    for event in pg.event.get():
        # check for closing window
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYUP:
            if event.key == pg.K_SPACE:
                monster1.minushp()        
            # if event.key == pg.K_SPACE:
            #     menu()
    
    
    
    
    
    # Update
    all_sprites.update()





    # draw and render
    screen.fill(Color.Salmon)
    # screen.blit(menu,menu_rect)
    draw_text(screen,"hp:" + str(player.maxhp), 18, 30,30,white)
    draw_text(screen,"Exp:" + str(player.exp), 18, 30,60,white)
    draw_text(screen,"Strength:" + str(player.attribute['strength']), 18, 30,90,white)
    draw_text(screen,"Level:" + str(player.level), 18, 30,120,white)

    # all_sprites.draw(screen)

    # draw_text(screen,"Hello world",50,400,300)             both functions work perfectly fine
    # button("hello world",400,300,100,100,Color.Salmon,Color.Orange,quitf)
    pg.display.flip()



quitf()
