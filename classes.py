import random

class Knight:
    name = ""
    def __init__ (self, newname):
            self.name = newname 
            self.damage = random.randrange(10)+50
            self.health = random.randrange(20)+150
            self.defence = random.randrange(10)+30
            self.regeneration = random.randrange(10)+5
            self.temphealth = self.health
            self.tempdamage = self.damage
            self.tempregeneration = self.regeneration
            self.tempdefence = self.defence
            self.location = 1

class Mage:
    name = ""
    def __init__ (self, newname):
            self.name = newname 
            self.damage = random.randrange(10)+55
            self.health = random.randrange(20)+70
            self.defence = random.randrange(10)+10
            self.regeneration = random.randrange(10)+15
            self.temphealth = self.health
            self.tempdamage = self.damage
            self.tempregeneration = self.regeneration
            self.tempdefence = self.defence
            self.location = 1

class Healer:
    name = ""
    def __init__ (self, newname):
            self.name = newname 
            self.damage = random.randrange(10)+35
            self.health = random.randrange(20)+140
            self.defence = random.randrange(10)+20
            self.regeneration = random.randrange(10)+20
            self.temphealth = self.health
            self.tempdamage = self.damage
            self.tempregeneration = self.regeneration
            self.tempdefence = self.defence
            self.location = 1
            self.lives = 3

class Assassin:
    name = ""
    def __init__ (self, newname):
            self.name = newname 
            self.damage = random.randrange(10)+50
            self.health = random.randrange(20)+70
            self.defence = random.randrange(10)+30
            self.regeneration = random.randrange(10)+10
            self.temphealth = self.health
            self.tempdamage = self.damage
            self.tempregeneration = self.regeneration
            self.tempdefence = self.defence
            self.location = 1

def choose():
    newname = raw_input("What do you want to call your hero?")
    while True:
        whatclass = raw_input("Which class do you want to play? Knight, Mage, Healer, Assassin: ")
        if ("Knight" in whatclass) or ("knight" in whatclass):
            myguy = Knight(newname)
            choice = 0
            break
        elif ("Mage" in whatclass) or ("mage" in whatclass):
            myguy = Mage(newname)
            choice = 1
            break
        elif ("Healer" in whatclass) or ("healer" in whatclass):
            myguy = Healer(newname)
            choice = 2
            break
        elif ("Assassin" in whatclass) or ("assassin" in whatclass):
            myguy = Assassin(newname)
            choice = 3
            break
        else:
            print "Pick a valid input!"
    return choice, myguy

def levelup(myguy):
    myguy.damage = myguy.damage+20
    myguy.health = myguy.health+60
    myguy.defence = myguy.defence+10
    myguy.regeneration = myguy.regeneration+5
    while True:
        best = raw_input("You have attained a new power level!\nWhich one would you like to make even better? defence, health, damage, regeneration, or everything?")
        if "defence" in best:
            myguy.defence = myguy.defence+20
            break
        elif "damage" in best:
            myguy.damage = myguy.damage+60
            break
        elif "health" in best:
            myguy.health = myguy.health+10
            break
        elif "regeneration" in best:
            myguy.regeneration = myguy.regeneration+5
            break
        elif "everything" in best:
            myguy.damage = myguy.damage+5
            myguy.health = myguy.health+15
            myguy.defence = myguy.defence+3
            myguy.regeneration = myguy.regeneration+2
            break
        else:
            print "choose a valid input"
    myguy.tempdamage = myguy.damage
    myguy.temphealth = myguy.health
    myguy.tempdefence = myguy.defence
    myguy.tempregeneration = myguy.regeneration
    return myguy


        
