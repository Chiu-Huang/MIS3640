import random 
import pygame as pg
import pygame

def dice(x):
    return random.randint(1,x)

levelup = False
class Character (pg.sprite.Sprite):
    def dice_attribution(self,x):
        for i in self.attribute:
            k = 1
            for roll_times in range (0,k,1):
                self.attribute[i] += dice(x)

    def buff (self, race):
        if race == "orc":
            self.buff = [1.3,1.1,0.8,0.5] # hp buff, strength buff,dex debuff, widsom debuff 
        if race == "human":
            self.buff = [1,1,11,1.5] # hp buff, strength buff,dex debuff, widsom debuff
        if race == "elf":
            self.buff = [0.9,1.1,1.4,1.2] # hp buff, strength buff,dex debuff, widsom debuff
        if race == "monster":
            self.buff = [0.9,1.1,1.4,1.2] # hp buff, strength buff,dex debuff, widsom debuff
        if race == "boss":
            self.buff = [3,2,1.4,1] # hp buff, strength buff,dex debuff, widsom debuff

        p = ['strength','dexterity','wisdom']
        for i in range (len(p)):
            self.attribute[p[i]] = self.attribute[p[i]] * self.buff[i+1]

    def __init__(self, race = "human"):
        pg.sprite.Sprite.__init__(self)
        self.attribute = {'strength':0, 'dexterity':0, 'wisdom':0}
        self.level = 1

        Character.dice_attribution(self, 18)
        Character.buff(self,race)
        # race formation
        if race == "orc":
            self.buff = [1.3,1.1,0.8,0.5] # hp buff, strength buff,dex debuff, widsom debuff 
        if race == "human":
            self.buff = [1,1,11,1.5] # hp buff, strength buff,dex debuff, widsom debuff
        if race == "elf":
            self.buff = [0.9,1.1,1.4,1.2] # hp buff, strength buff,dex debuff, widsom debuff
        if race == "monster":
            self.buff = [0.9,1.1,1.4,1.2] # hp buff, strength buff,dex debuff, widsom debuff
        
        # hp formula
        k = (50 * self.level + self.attribute['strength']*3) *self.buff[0]
        self.maxhp = round (k,0)
        self.hp = self.maxhp
        self.atk = self.attribute['strength']*8
        self.speed = 8/self.attribute['dexterity']    # second per hit 
        self.defense = 30 * self.level + self.attribute['strength']*2
        self.magic = self.attribute['wisdom'] * 15
        self.exp = 0
        self.gold = random.randint(50,300)
        self.item_list = []
        self.equipped_list = []
        self.time = 0
        # bug, should separate incremental benefit of race buff

        self.x = 0
        self.y = 0
        self.current_state = 0
        self.fight = False
        self.event = False
        self.death = False
        self.levelup = False

    def fight (self, k):
        self.dice = []
        k.dice = []
        self.position = 0
        k.position = 0
        selflist = self.dice[self.position]
        klist = k.dice[k.position]
        diff = selflist - klist
        for i in range (100):
            self.dice.append(dice(18))
            k.dice.append(dice(18))

        if self.attribute[dexterity] > k.attribute[dexterity]:
            start = 0
        else:
            start = 1

        while self.fight:
            if start == 0:
                # fightoption()
                if diff < 0:
                    print ("Missed")
                    self.position +=1 
                    k.position += 1
                    start = 1
                elif diff < 9:
                    k.hp -= self.attribute[strength] * diff
                    self.position +=1 
                    k.position += 1
                    start = 1
                elif diff < 18:
                    k.hp -= self.attribute[strength] * 2 * diff
                    print ("Critical Attack")
                    self.position +=1 
                    k.position += 1
                    start = 1
            if start == 1:
                # fightoption()
                if diff > 0:
                    print ("Missed")
                    self.position +=1 
                    k.position += 1
                    start = 0
                elif diff > -9:
                    self.hp -= k.attribute[strength] * diff
                    self.position +=1 
                    k.position += 1
                    start = 0
                elif diff > -18:
                    self.hp -= k.attribute[strength] * 2 * diff
                    print ("Critical Attack")
                    self.position +=1 
                    k.position += 1
                    start = 0
            if self.hp <= 0:
                self.fight = false
            if k.hp <= 0:
                print ("You win, you receive XX exp + YY gold. format later")
                self.exp += k.exp * 0.5
                self.gold += k.gold
                p = len (k.item_list)
                helper = []
                for i in range (random.randint(0,3)):
                    t = 0
                    helper += random.randint(0,p -t)
                    t += 1
                p1 = len (helper)
                for i in p1:
                    self.item_list.append(k.item_list[i])
                    k.item_list.pop(i)

                self.fight = false


    def work(self):
        mini = 50
        maxi = 300
        p = random.randint(mini,maxi)
        self.gold += p 
        if p > 200:  # don't hard code....
            print ("Your Boss likes your work and decides to pay you extra. You receive ${:02f})".format(p))
        elif p > 125:
            print ("Your hard work paid off. You receive ${:02f})".format(p))
        else:
            print ("You receive ${:02f} ... You can't even buy a beer with that tiny salary. You start to wonder if you should start adventure with the guys in the bar".format(p))
        self.time += 1


    def training(self):
        mini = 5
        maxi = 20
        p = random.randint(mini, maxi)
        self.exp += p 
        if p == maxi:
            print ("You feel tremendous power in your body, add ${:02f} exp & add 1 strength)".format(p))
            self.attribute["strength"]+=1
        elif p > 12:
            print ("After your work out, you gain ${:02f} exp)".format(p))
        else:
            print ("You gain {:02f} exp ... ".format(p))
        self.time += 1

    def discover(self):
        pass
        #reveal uncommon things?

    def buy(self):
        pass

    def sell(self):
        pass     

    def test(self):
        self.hp = 0
    def update(self):
        # # Encounter Monster
        

        # while self.fight:
            
            
        #     pass
        

        # # Encounter Event 
        # while self.event:
        #     pass
        
        # up level
        global levelup
        if self.exp >= 100 * (self.level):
            levelup = True
        if levelup:
            self.exp -= 100*self.level
            self.level += 1
            player.dice_attribution(self,5)
            self.maxhp = round ((50 * self.level + self.attribute['strength']*3) *self.buff[0],0)
            self.hp = self.maxhp    #renew hp
            levelup = False     

        if self.hp < 0:
            self.death = True





class player (Character):
   
    def update(self):
        Character.update(self)        
        if self.death:
            print(self.time)
            self.time -= min(10,self.time)
            print(self.time)


class monster (Character):
    def __init__(self):
        Character.__init__(self)
        self.race = "monster"
        self.level = random.randint(1,3)
        self.x = random.randint(1,5)
        self.y = random.randint(1,5)
        self.name = "Globin"




    def update(self):
        Character.update(self)        
        if self.death:
            #need to ask
            # player.gold += self.gold
            # player.exp +=self.exp
            self.kill()

class boss (Character):
    def __init__(self, name):
        Character.__init__(self)
        self.race = "boss"
        self.level = random.randint(1,3)
        self.x = random.randint(1,5)
        self.y = random.randint(1,5)
        self.name = name 


    def update(self):
        Character.update(self)        
        if self.death:
            #need to ask
            # player.gold += self.gold
            # player.exp +=self.exp
            self.kill()



