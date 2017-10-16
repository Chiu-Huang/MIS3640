import pygame as pg
import random
import os
import pygame

WIDTH = 800
HEIGHT = 600
FPS = 30


# define colors
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0, 255,0)
blue = (0,0,255)


# set up assets folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")

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
        self.y_speed = 5
    def update(self):
        self.rect.x += 5
        if self.rect.left > WIDTH:
            self.rect.right = 0
        self.rect.y += self.y_speed
        if self.rect.bottom > HEIGHT -200:
            self.y_speed = -5
        if self.rect.top < 200:
            self.y_speed = 5
# initializing pygame and create window 
pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption("DND again v2")
clock = pg.time.Clock()

all_sprites = pg.sprite.Group()
player = Player()
all_sprites.add(player)




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
        
    
    # Update
    all_sprites.update()

    # Draw/Render 
    screen.fill(white)
    all_sprites.draw(screen)


    # *after* drawing everything, flip the display
    pg.display.flip()



pg.quit()
quit()






