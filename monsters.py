import random
import System

class Orc:
    name = ""
    def __init__ (self, newname):
            self.name = newname 
            self.damage = random.randrange(10)+20
            self.health = random.randrange(20)+50
            self.defence = random.randrange(10)+5
            self.regeneration = random.randrange(10)
            self.temphealth = self.health
            self.type = 1
            self.misschance = 1
            self.count = 1

class Zombie:
    name = ""
    def __init__ (self, newname):
            self.name = newname 
            self.damage = random.randrange(10)+20
            self.health = random.randrange(20)+100
            self.defence = random.randrange(10)+5
            self.regeneration = random.randrange(10)
            self.temphealth = self.health
            self.type = 2
            self.misschance = 1
            self.count = 1

class Giant:
    name = ""
    def __init__ (self, newname):
            self.name = newname 
            self.damage = random.randrange(10)+40
            self.health = random.randrange(20)+70
            self.defence = random.randrange(10)+20
            self.regeneration = random.randrange(10)+5
            self.temphealth = self.health
            self.type = 3
            self.misschance = 1
            self.count = 1

class Troll:
    name = ""
    def __init__ (self, newname):
            self.name = newname 
            self.damage = random.randrange(10)+90
            self.health = random.randrange(20)+400
            self.defence = random.randrange(10)+30
            self.regeneration = random.randrange(10)+20
            self.temphealth = self.health
            self.type = 4
            self.misschance = 1
            self.count = 2

class Necromancer:
    name = ""
    def __init__ (self, newname):
            self.name = newname 
            self.damage = random.randrange(10)+150
            self.health = random.randrange(20)+300
            self.defence = random.randrange(10)+80
            self.regeneration = random.randrange(10)+50
            self.temphealth = self.health
            self.type = 5
            self.misschance = 1
            self.count = 1

class GiantKing:
    name = ""
    def __init__ (self, newname):
            self.name = newname 
            self.damage = random.randrange(10)+300
            self.health = random.randrange(20)+5000
            self.defence = random.randrange(10)+200
            self.regeneration = random.randrange(10)+75
            self.temphealth = self.health
            self.type = 6
            self.misschance = 1
            self.count = 3


class Ooze:
    name = ""
    def __init__ (self, newname):
            self.damage = random.randrange(10)+150
            self.health = random.randrange(20)+3000
            self.defence = random.randrange(10)+30
            self.regeneration = random.randrange(10)+60
            self.temphealth = self.health
            self.type = 7
            self.misschance = 5
            self.count = 1
            self.location = 36

class dummy:
    name = ""
    def __init__ (self, newname):
            self.damage = 0
            self.health = 0
            self.defence = 0
            self.regeneration = 0
            self.temphealth = 0
            self.type = 8
            self.misschance = 0
            self.count = 0

def bossgen():
    gc1 = Ooze("Blob")
    troll = Troll("Bloodsoaked")
    necro = Necromancer("Necroman")
    return gc1, troll, necro

def rapidregen(monster):
    monster.temphealth += monster.regeneration

def alliedhealing(cmonster, list1):
    for i in range(cmonster):
        rapidregen(list1(i))

def balefulsword(myguy, monster, x):
    if x != 0:
        z = monster.damage - myguy.defence
        return z
    else:
        return 0

def steallife(myguy, monster):
    x = monster.damage-myguy.health
    myguy.temphealth -= x
    monster.temphealth += x

def timer(t1, t2, GC1):
    tt = t2-t1
    mmove = 1
    for i in range(int(tt)):
        GC1 = System.Move(GC1, mmove)
    mmove = 0
    return GC1

def mdecide(monster):
    chance = monster.type
    if (chance == 5) or (chance == 6):
        r = random.randrange(10)
        if r == 0:
            special = 1
        else:
            special = 0
    else:
        special = 0
    return special

def mspecial(m1):
    if m1.type == 5:
        return 1
    elif m1.type == 6:
        return 2

def mgen(herolocation):
    if herolocation >= 1 and herolocation < 2:
        m1=Orc("Red Shirt")
        m2=Orc("Blue Shirt")
        m3=Orc("Yellow Shirt")
        mtype = 1
    elif herolocation >= 2 and herolocation < 3:
        m1=Zombie("Grey Skin")
        m2=Zombie("Green Skin")
        m3=Zombie("Purple Skin")
        mtype = 2
    elif herolocation >= 3 and herolocation < 4:
        m1=Giant("Red Helm")
        m2=Giant("Blue Helm")
        m3=Giant("Orange Helm")
        mtype = 3
    else:
        m1 = Orc("Red Shirt")
        m2 = Orc("Blue Shirt")
        m3 = Orc("Yellow Shirt")
        mtype = 1
    monsternum = random.randrange(4)
    if monsternum == 1:
        m2 = dummy("duh")
        m3 = dummy("duh")
        return m1, m2, m3, monsternum, mtype
    elif monsternum == 2:
        m3 = dummy("duh")
        return m1, m2, m3, monsternum, mtype
    elif monsternum == 3:
        return m1, m2, m3, monsternum, mtype
    else:
        m1 = dummy("duh")
        m2 = dummy("duh")
        m3 = dummy("duh")
        return m1, m2, m3, monsternum, mtype

def misschance(m1):
    r = random.randrange(5)+2
    if r >= m1.misschance:
        return 1
    else:
        return 0

def choose():
    again = "y"
    while "y" in again:
        newname = raw_input("What do you want to call your monster?")
        while True:
            whatclass = input("Which do you want the monster to be? 1 = Orc, 2 = Zombie, 3 = Giant, 7 = Ooze, 6 = Giant King, 5 = Necromancer, 4 = Troll")
            if whatclass == 1:
                myguy = Orc(newname)
                choice = "Orc"
                break
            elif whatclass == 2:
                myguy = Zombie(newname)
                choice = "Zombie"
                break
            elif whatclass == 3:
                myguy = Giant(newname)
                choice = "Giant"
                break
            elif whatclass == 7:
                myguy = Ooze(newname)
                choice = "Ooze"
                break
            elif whatclass == 6:
                myguy = GiantKing(newname)
                choice = "GiantKing"
                break
            elif whatclass == 5:
                myguy = Necromancer(newname)
                choice = "Necromancer"
                break
            elif whatclass == 4:
                myguy = Troll(newname)
                choice = "Troll"
                break
            else:
                print "Pick a valid input!"


#main
