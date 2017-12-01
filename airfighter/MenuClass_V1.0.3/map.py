import pygame as pg

class Map (pg.sprite.Sprite):
    def __init__ (self,name, description = None, treasure = 1, monster = 1):
        """ 1 is the least, 3 is the most."""
        self.name = name
        self.description = description
        self.treasure = treasure
        self.monster = monster


mapname = "forest, dungeon1, dungeon2, dungeon3"
mapdescription = "dqwpjdwfogjdpjdwqd, dijwqodwocq, dqwijdosjvd, icoqjedqwoijd"

mapname = mapname.split(", ")
mapdescription = mapdescription.split(", ")

percentl = [0.01, 0.3,0.3, 0.39]


def percentagelist (xl, percentl):
    k = []
    for i in range (len (xl)):
        k += (xl[i] * 100 * percentl[i]) //1
    return k

mapgenerator = 
forest = Map(forest)


def mapsize (x=5, y=5):
    k = []
    for i in range (0, x+1):
        for j in range (0,y+1):
            k.append ((i, j))
    k.pop(0)
    return k

def mapinit (x, y):
    k = mapsize (x,y)
    
    








maplocation = [(0,"F", 1),(1,"L",2), (2,"F",3), (3, "F", 4), (1,"R",5),(5,"F",6),(6,"F",7),(7, "L", 8), (8, "F", 14), (14, "F",10), (10,"L", 11), (10, "R", 12), (4, "B", 5), (10,"R",12),(7,"R",9),(9,"F",8),(8,"R",9),(12,"R",11)]

current_state = 0


possible_route = []
for i in maplocation:
    if i[0] == current_state:
        possible_route.append(i[1])
    


























