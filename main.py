import classes
import monsters
import text
import System
import mapp
from time import time

#main
ntrap=0
ntreasure=0
nstairs=0
Rooms, ntreasure, ntrap, nstairs = mapp.roomgenerator()
xp = 0
m1 = 0
m2 = 0
m3 = 0
classlist = ("knight", "mage", "healer", "assassin")
mlist = ("orc", "zombie", "giant", "troll", "necromancer", "giant king", "gelatinous cube")
choice, myguy = classes.choose()
print "You are the valiant", classlist[choice], "who is named", (myguy.name), "health is", (myguy.health), "\ndamage is", (myguy.damage), "\nDefence is", (myguy.defence), "\nregeneration is", (myguy.regeneration)
newname = "Hrothgar the Bane"
gk1 = monsters.GiantKing(newname)
print "He is the despicable", mlist[gk1.type-1], "who is named", (gk1.name), "He is strong, and does is", (gk1.damage), "points of damage. He is tough, and has", (gk1.health), "points of health. He is armoured, and has", (gk1.defence), "defence. He heals fast, and has", (gk1.regeneration), "points of regeneration"
print "This is how to level up:"
myguy = classes.levelup(myguy)
print "\nAnd now, on to the main event"
GC1, Troll, Necro = monsters.bossgen()
text.intro()
tempdefence = 0
newlocation = 1
cmonster = 0
mmove = 0
m1, m2, m3, cmonster, mtype = monsters.mgen(myguy.location)
m4 = m1
cmonster = 0
healthholder = myguy.temphealth
done = 0
done1 = 0
done2 = 0
done3 = 0
while (myguy.temphealth >= 0) or (gk1.temphealth >= 0):
    #cmlist = [m1, m2, m3]
    if (cmonster != 0):
        if cmonster == 0:
            print "All monsters dead!"
            xp += 1
            cmonster = 0
    if myguy.location <= 12:
        print "\nYou are on the first floor."
    elif myguy.location > 12 and myguy.location <= 24:
        print "\nYou are on the second floor."
    elif myguy.location > 24 and myguy.location <= 36:
        print "\nYou are on the third floor."
    print "Your health is", (myguy.temphealth), "\ndamage is", (myguy.tempdamage), "\nDefence is", (myguy.tempdefence), "\nregeneration is", (myguy.tempregeneration)
    if tempdefence == 1:
        myguy.tempdefence -= 20
        tempdefence = 0
    if newlocation == 1:
        m1, m2, m3, cmonster, mtype = monsters.mgen(myguy.location)
        cmlist = [m1, m2, m3]
        newlocation = 2
        specialuse = 0
    for i in range (cmonster):
        z = cmlist[i]
        if z.temphealth <= 0:
            cmonster -= 1
            del cmlist[i]
            xp = xp + 1
    if cmonster != 0:
        print "\nThere are", cmonster, mlist[m1.type-1], "in this room. They raise their weapons and charge!"
    for i in range (cmonster):
        z = cmlist[i]
        print"\nMonster health is", (z.temphealth), "\ndamage is", (z.damage), "\nDefence is", (z.defence), "\nregeneration is", (z.regeneration)
    t1 = time()
    if (newlocation == 2) and (cmonster == 0):
        for i in range(36):
            if i+1 == myguy.location:
                print Rooms[i]
                mapp.perform(myguy.location,ntrap,ntreasure,nstairs, myguy)
                newlocation = 0
                break
    if choice == 2:
        if cmonster != 0:
            answer = raw_input("Attack, defend, stay, or move\n--> ")
        else:
            answer = raw_input("Stay or move\n--> ")
    else:
        if cmonster != 0:
            answer = raw_input("Attack, defend, stay, special, or move\n--> ")
        else:
            answer = raw_input("Stay or move\n--> ")
    for i in range (cmonster):
        z = cmlist[i]
        if z.temphealth <= 0:
            cmonster -= 1
            del cmlist[i]
            xp = xp + 1
    if ("attack" in answer) and (cmonster>0):
        if (m3.temphealth >= 0) and (m3.type != 8) and (cmonster == 3):
            defender = 2
        elif (m3.temphealth <= 0) and (m2.temphealth >=0) and (m2.type != 8) and (cmonster == 2):
            defender = 1
        elif (m3.temphealth <= 0) and (m2.temphealth <=0)and (m1.temphealth >= 0) and (cmonster == 1):
            defender = 0
        hit = monsters.misschance(cmlist[defender])
        if hit == 1:
            temphealth = System.Attack(myguy, cmlist[defender], 1)
            cmlist[defender].temphealth = temphealth
        else:
            print "He dodged it!"
    elif "move" in answer:
        myguy.location = System.Move(myguy.location, mmove)
        newlocation = 1
    elif "defend" in answer:
        myguy.tempdefence += 20
        tempdefence = 1
    elif "stay" in answer:
        myguy = System.Pass(myguy)
    elif ("special" in answer) and choice != 2 and (specialuse != 1):
        m1, m2, m3 = System.Special(myguy, choice, cmonster, m1, m2, m3)
        specialuse = 1
    elif (specialuse == 1) and ("special" in answer):
        print "You alreadys used your special in this room"
    else:
        if choice == 2:
            if cmonster <= 0:
                print "You can only defend, stay, or move. "
            else:
                print "You can only attack, defend, stay, or move. "
        else:
            if cmonster <= 0:
                print "You can only defend, stay, special, or move. "
            else:
                print "You can only attack, defend, stay, special, or move. "
    t2 = time()
    GC1.location = monsters.timer(t1, t2, GC1.location)
    if (GC1.location == myguy.location) and (done3 != 1):
        m3 = m2
        m2 = m1
        m1 = GC1
        if cmonster < 3:
            cmonster = 1
        text.boss(myguy.location)
        done4 = 1
    if myguy.location == 12 and (done != 1):
        m1 = Troll
        m2 = m4
        m3 = m4
        text.boss(myguy.location)
        cmonster = 1
        done = 1
    if myguy.location == 24 and (done1 != 1):
        cmonster = 3
        m1, m2, m3, cmonster, mtype = monster.mgen
        m3 = m1
        m2 = m1
        m1 = Necro
        if cmonster < 3:
            cmonster = 3
        text.boss(myguy.location)
        done1 = 1
    if myguy.location == 36 and (done2 != 1):
        cmonster = 1
        m1 = GK1
        GK1 = m1
        text.boss(myguy.location)
        cmonster = 1
        done2 = 1
    for i in range(cmonster):
        if cmlist[i].count != 1:
            cmonster += m1.count
    temphealth = myguy.temphealth
    for i in range(cmonster):
        if cmlist[i] != 0:
            maction = monsters.mdecide(cmlist[i])
            if maction == 0:
                if cmlist[i].type == 6:
                    dmg = monsters.balefulsword(myguy, gk1, gk1.count)
                    myguy.temphealth -= dmg
                    myguy.health -= dmg
                else:
                    temphealth = System.Attack(cmlist[i], myguy, cmonster)
            elif maction == 1:
                which = monsters.mspecial(cmlist[i])
                if which == 1:
                    monsters.alliedhealing(cmonster, cmlist)
                elif which == 2:
                    monsters.steallife(myguy, cmlist[i])
    myguy.temphealth = temphealth
    if (m1.type == 4) or (m1.type == 7):
        monsters.rapidregen(m1)
    if xp >= 15:
        print "LEVEL UP!!!!!!!!!!!!!!!!!!!!!!!!!"
        myguy = classes.levelup(myguy)
        xp -= 15
    if myguy.temphealth <= 0:
        if (choice != 2):
            break
        if choice == 2:
            if myguy.lives != 0:
                myguy = System.healerspecial(myguy, healthholder)
    if myguy.temphealth > myguy.health:
        myguy.temphealth = myguy.health
if myguy.temphealth <= 0:
    text.dead()
elif gk1.temphealth <= 0:
    text.conclusion()
    












