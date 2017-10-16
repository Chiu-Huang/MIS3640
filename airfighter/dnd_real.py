import pygame as pg
import random
import os
import pygame
import color




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
    font = pg.font.Font(font_name, size)
    text_surface =font.render(text, True, white)
    text_rect = text_surface.get_rect()
    text_rect.center =(x,y)
    surf.blit(text_surface,text_rect)

def button (msg,x,y,w,h,color,icolor,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x  and  y + h > mouse[1] > y:
        pygame.draw.rect (screen, color,(x,y,w,h))
        if click[0] ==1: and action != None:    
    else:
        pygame.draw.rect (screen, icolor,(x,y,w,h))

    draw_text (screen,msg,min(w,h),rect (x) + width/2 , rect(y) + height/2)

    # smallText = pygame.font.Font('freesansbold.ttf',20)
    # textSurf, textRect = text_objects (msg,smallText)
    # textRect.center = (rect (x) + width/2 , rect(y) + height/2)
    # screen.blit (textSurf,textRect)


def newenemy():
    e = Enemy()
    all_sprites.add(e)
    enemies.add(e)    

def draw_shield_bar (surf, x,y,pct):
    if pct < 0:
        pct = 0
    BAR_LENGTH = 100
    BAR_HEIGHT = 10
    fill = (pct/100) * BAR_LENGTH
    outline_rect = pg.Rect(x,y,BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pg.Rect (x,y,fill, BAR_HEIGHT)
    pg.draw.rect(surf,Green,fill_rect)
    pg.draw.rect(surf,white,outline_rect,2)

class Player (pg.sprite.Sprite):
    # sprite of the Player
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        # self.image = pg.Surface ((50,50))
        self.image = pg.image.load (os.path.join (img_folder, "p1_jump.png")).convert()
        self.image.set_colorkey(white)
        # self.image.fill (green)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        # self.y_speed = 5
        self.speedy = 0
        self.speedx = 0
        self.shield = 100


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
        
        self.rect.x += self.speedx
        self.rect.y += self.speedy

    def shoot (self):
        bullet = Bullet (self.rect.centerx,self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)
 # centerx on the player, top of the layer
class Enemy(pg.sprite.Sprite):
    def __init__ (self):
        pg.sprite.Sprite.__init__(self)
        self.image = random.choice (monster_images)
        # self.image = pg.Surface((100,100))
        # self.image.fill(blue)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(30,600)
        # WIDTH - self.rect.width
        self.rect.y = random.randrange(-100,-40)
        self.speedy = random.randrange(1,8)
        self.rot = 0
        self.rot_speed = random.randrange(-8,8)
        self.last_update =pg.time.get_ticks()

    def rotate (self):
        now = pg.time.get_ticks()

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100,-40)
            self.speedy = random.randrange(1,8)

class Bullet(pg.sprite.Sprite):
    def __init__ (self,x,y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((10,20))
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()





all_sprites = pg.sprite.Group()
player = Player()
all_sprites.add(player)
enemies = pg.sprite.Group()
for i in range (0):
    newenemy()

bullets = pg.sprite.Group()




# Load all game graphics
background = pg.image.load (os.path.join(img_folder,"cloud.png")).convert()
background_rect = background.get_rect()

player_img = pg.image.load (os.path.join(img_folder,"cloud.png")).convert()
bullet_img = pg.image.load (os.path.join(img_folder,"cloud.png")).convert()
monster_images = []
monster_list = [".png", ".png"]


for img in monster_list:
    monster_images.append(os.path.join(img_folder,img)).convert())


# Load all game sounds
shoot_sound = pg.mixer.Sound(os.path.join(img_folder,.wav))
shoot_sound.play()
sound_sounds = []
monster_list = [".png", ".png"]
pg.mixer.music.load(os.path.join(img_folder,.wav))
pg.mixer.music.set_volume (0.5)

#Game loop
running = True
while running:
    #keep loop running at the same speed
    clock.tick(FPS)
    # Process input (events)
    for event in pg.event.get():
        # check for closing window
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                player.shoot()        
    
    # Update
    all_sprites.update()

    # check if a bullet hits an enemy
    hits = pygame.sprite.pygame.sprite.groupcollide(enemies, bullets, True,True)
    for hit in hits:
        hits += 1
        newenemy()


    # check to see if an enemy hits the player:
    hits = pygame.sprite.pygame.sprite.spritecollide(player, enemies, False)
    for hit in hits:
        player.shield -= hit.radius * 2
        newenemy()
#pg.sprite.collide_circle
        if player.shield <= 0:
            running = False

    # Draw/Render 
    screen.fill(white)
    screen.blit(background,background_rect)
    all_sprites.draw(screen)
    draw_text(screen,str(score, 18, WIDTH))

    draw_shield_bar(surf,5,5,player.shield)

    # *after* drawing everything, flip the display
    pg.display.flip()



pg.quit()
quit()


