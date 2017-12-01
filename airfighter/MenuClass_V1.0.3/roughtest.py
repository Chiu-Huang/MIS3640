import pygame as pg
import pygame, sys, random, os
from color import *
import startmenu
from menu import *
from image import *


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
pcolor = (255,244,226)
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

def text_box(surf, text):
    global WIDTH, HEIGHT
    fontsize = 30
    font = pg.font.SysFont("arial", fontsize)
    fontHeight = font.size ("Tg")[1]
    rect = pg.Rect([0,4/6*HEIGHT,WIDTH,HEIGHT])    
    rect.left = 10
    rect.top = 4/6*HEIGHT
    pygame.draw.rect(screen, Color.BurlyWood, [0,4/6*HEIGHT,WIDTH,HEIGHT])
    y = rect.top
    lineSpacing = -2

    while text:
        i = 1

        # determine if the row of text will be outside our area
        if y + fontHeight > rect.bottom:
            break

        # determine maximum width of line
        while font.size(text[:i])[0] < WIDTH and i < len(text):
            i += 1
        # if we've wrapped the text, then adjust the wrap to the last word      
        if i < len(text): 
            i = text.rfind(" ", 0, i) + 1

        # render the line and blit it to the >surf
        image = font.render(text[:i], True, white)

        surf.blit(image, (rect.left, y))
        y += fontHeight + lineSpacing

        # remove the text we just blitted
        text = text[i:]

    return text
   

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

def attributescreen (player):
    p = 240
    q = 25
    x = 400
    font = 30
    fcolor = black
    # list = [level, exp, hp, maxhp, gold, 'strength', 'dexterity', 'wisdom']
    # for i in range (0,len(list),1):
        # draw_text(screen, str(list[i])+ str(player.list[i]), 18, p,90,white)
    #     p += 30 
    draw_text(screen,"Level:" + str(player.level), font, x,p,fcolor)
    draw_text(screen,"Exp:" + str(player.exp), font, x,p+q,fcolor)
    draw_text(screen,"hp:" + str(player.hp), font, x,p+q*2,fcolor)
    draw_text(screen,"maxhp:" + str(player.maxhp), font, x,p+q*3,fcolor)
    draw_text(screen,"Strength:" + str(player.attribute['strength']),font, x,p+q*4,fcolor)  
    draw_text(screen,"dexterity:" + str(player.attribute['dexterity']), font, x,p+q*5,fcolor)  
    draw_text(screen,"wisdom:" + str(player.attribute['wisdom']), font, x,p+q*6,fcolor)  



# def gameover():
#     bmid("You died... Please insert coins to play again!",quitf)
#     pg.display.flip()
#     waiting = True
#     while waiting:
#         clock.tick(FPS)
#         for event in pygame.event.get():
#             if event.type == pg.QUIT:
#                 pg.quit()

def fight (a, b):
    a.update_after_monster_dies(b)


def quitf():
    pg.quit()
    quit()


#Define Global Variables
index = [0.8,0.5,0.3]    # usage of attribute
levelup = False
            
from player import *

races = random.choice (["orc", 'human', 'elf'])

all_sprites = pg.sprite.Group()
player = player(race = "orc")

indextime = 0

# create NPCs 

a = Character(race= "human")
a.exp = 250

b = Character(race ="human")
c = Character(race ="orc")
d = Character(race ="elf")



all_sprites.add(player)
all_sprites.add(a)
all_sprites.add(b)
all_sprites.add(c)
all_sprites.add(d)

Team = [a,b,c,d]

monsters = pygame.sprite.Group()
monster1 = monster()
monster1.current_state = 3

monster2 = monster()
monster2.current_state = 5

monster3 = monster()
monster3.current_state = 7

monster4 = monster()
monster4.current_state = 1


# for i in range (0,8,1):
#     monster1 = monster()
#     monsters.add(monster1)
#     print(monster1.x, monster1.y)

# create boss
ms = boss('ms')
ms.current_state = 4
ms.item_list = ['sword' ,"really sharp sword", "knife"]
ms.exp = 300


mirage = boss('mirage')
mirage.current_state = 14
mirage.item_list = ['sword' ,"really sharp sword", "knife"]
mirage.exp = 400

ironspine = boss('ironspine')
ironspine.current_state = 9
ironspine.item_list = ['sword' ,"really sharp sword", "knife"]
ironspine.exp = 500

dragon = boss('dragon')
dragon.current_state = 11
dragon.item_list = ['sword' ,"really sharp sword", "knife"]
dragon.exp = 550

melting = boss('melting')
melting.current_state = 12
melting.item_list = ['sword' ,"really sharp sword", "knife"]
melting.exp = 450




monsters.add(monster1)
monsters.add(monster2)
monsters.add(monster3)
monsters.add(monster4)

monsters.add(ms)
monsters.add(ironspine)
monsters.add(dragon)
monsters.add(melting)
monsters.add(mirage)

import time

def show (string):
    text_box(screen,string)
    pg.display.flip()
    time.sleep(0.5)

stringg = ""
def fight (a,b):
    global stringg
    show ("You enounter " + str((b.race)) + " "+ str(b.name))
    
    while a.hp > 0 and b.hp > 0:
        print ("Monster's HP is {}.".format(b.hp))
        time.sleep(0.5)
        if a.attribute['strength'] > b.attribute['strength']:
            b.hp -= 1000
        else:
            b.hp -=100

        print ("Your remaining HP is {}.".format(a.hp))
        print ("Monster's HP is {}.".format(b.hp))
        if b.hp <= 0:
            
            # Gain
            if b.exp == 0:
                b.exp = 50
            a.exp += b.exp * 0.5
            a.gold += b.gold
            p = len (b.item_list)
            helper = []
            for i in range (random.randint(0,3)):
                t = 0
                de = random.randint(0,p -t)
                print (de)
                helper += [de]
                t += 1
            p1 = len (helper)
            if len(b.item_list) == 0:
                show ("The monster has nothing for you to loot")
            else:
                for i in range(p1):
                    a.item_list.append(b.item_list[i])
                    # b.item_list.pop(i)
                    show ("You loot an item " + str(b.item_list[i]))
                    time.sleep(0.5)

            b.kill()


    # a.exp += 10000
    # a.gold += 100

    stringg = "You Win! You gain " + str(b.exp*0.5) +"exp & " + str(b.gold) + "gold"
    pg.display.flip()
status = []
timer = []
# Game Loop
running = True
startmenu.main()
while running:
    #keep loop running at the same speed
    clock.tick(FPS)
    # Process input (events)
    # if player.hp <= 0:
    #     screen.fill(Aquamarine)
    #     gameover()
    for event in pg.event.get():
        # check for closing window
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYUP:
            if event.key == pg.K_SPACE:
                monster1.minushp()
            # if event.key == pg.K_TAB:
            #     gamemenu()
            #     pygame.display.update(rect_list)

            if event.key == pg.K_w:
                player.current_state += 1
                player.time +=1
            if event.key == pg.K_s:
                player.current_state -= 1
                player.time +=1
            if event.key == pg.K_a:
                player.x -= 1
            if event.key == pg.K_d:
                player.x += 1
            if event.key == pg.K_p:
                player.work()
            if event.key == pg.K_o:
                player.training()
            if event.key == pg.K_i:
                player.test()      
            # event 1
            if event.key == pg.K_u:
                screen.fill(black)
                pg.display.flip()
                time.sleep (1.0)
                player.time = 0
                stringg = "You saw a black shadow & the second after that, you realize that you are back to the Village"

                # add flip 
            # if event.key == pg.K_SPACE:
            #     menu()
    for i in monsters:
        if i.current_state == player.current_state:
            fight (player,i)

    if indextime not in timer and indextime != player.time:
        timer += [indextime]
        status += [[player.attribute, player.maxhp, player.hp, player.atk, player.speed, player.defense, player.magic,player.exp,player.gold,player.item_list, player.equipped_list, player.time,player.current_state,player.level]]
        print (status)
        indextime = player.time

    if player.hp <= 0:
        # player.time -= min(5,player.time)
        player.time = 0
        indextime = player.time
        for i in status:
            if i[11] == player.time:
                player.attribute = i[0]
                player.maxhp = i[1]
                player.hp = i[2]
                player.atk = i[3]
                player.speed = i[4]
                player.defense = i[5]
                player.magic = i[6]
                player.exp = i[7]
                player.gold =i[8]
                player.item_list = i[9]
                player.equipped_list = i[10]
                player.time = i[11]
                player.current_state =i[12]
                player.level = i[13] 


        screen.fill(black)
        pg.display.flip()
        time.sleep (0.4)
        screen.fill(white)
        pg.display.flip()
        time.sleep (0.2)
        screen.fill(black)
        pg.display.flip()
        time.sleep (0.1)
        if player.hp < 0:
            player.hp = player.maxhp
        stringg = "You felt tremendous pain and blacked out. When you restore consciousness, you realize that you are at stage " + str(player.current_state)


        

    # Update
    all_sprites.update()





    # draw and render

    screen.fill(Color.Salmon)
    # screen.blit(menu,menu_rect)
    draw_text(screen,"hp:" + str(player.maxhp), 18, 30,30,white)
    draw_text(screen,"Exp:" + str(player.exp), 18, 30,60,white)
    draw_text(screen,"Strength:" + str(player.attribute['strength']), 18, 30,90,white)
    draw_text(screen,"Level:" + str(player.level), 18, 30,120,white)
    draw_text(screen,"Current States: " + str(player.current_state), 18, 30,150,white)
    if stringg != "":
        text_box(screen,stringg)
    # all_sprites.draw(screen)
    # pygame.draw.rect(screen, black, (200,150,100,50))
    # text_box(screen,"dijdwq dijwqdqijwdid djiwqdjiqj  dwqjdiwqdjiwd dwqijdwq jdiwqjdiwqjd jidwqjdiwqjd djiwqdjwqidjqwid jdqiwjdqijdwqd djwqid")
    # draw_text(screen,"Hello world",50,400,300)             both functions work perfectly fine
    # button("hello world",400,300,100,100,Color.Salmon,Color.Orange,quitf)
    pg.display.flip()



quitf()


