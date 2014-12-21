import monsters
import random
def knightspecial(myguy, monsternum, m1, m2, m3):
    while True:
        if (m3.temphealth >= 0):
            defender = 2
        elif ((m3.temphealth <= 0) or (m3 == 0)) and (m2.temphealth >=0):
            defender = 1
        elif ((m3.temphealth <= 0) or (m3 <= 0)) and ((m2.temphealth <=0) or (m2 <= 0)) and (m1.temphealth >= 0):
            defender = 0
        else:
            print "There are no monsters to attack"
            break
        if defender == 0:
            if (5*myguy.damage - m1.defence) >= 3:
                m1.temphealth -= 5*myguy.damage - m1.defence
            else:
                m1.temphealth -= 3
            break
        elif defender == 1:
            if (5*myguy.damage - m2.defence) >= 3:
                m2.temphealth -= 5*myguy.damage - m2.defence
            else:
                m2.temphealth -= 3
            break
        elif defender == 2:
            if (5*myguy.damage - m3.defence) >= 3:
                m3.temphealth -= 5*myguy.damage - m3.defence
            else:
                m3.temphealth -= 3
            break
    return m1, m2, m3
def magespecial(myguy, monsternum, m1, m2, m3):
    if monsternum == 1:
        if (myguy.damage - m1.defence) >= 3:
            m1.temphealth -= myguy.damage - m1.defence
        else:
            m1.temphealth -= 3
    elif monsternum == 2:
        if (myguy.damage - m1.defence) >= 3:
            m1.temphealth -= myguy.damage - m1.defence
        else:
            m1.temphealth -= 3
        if (myguy.damage - m2.defence) >= 3:
            m2.temphealth -= myguy.damage - m2.defence
        else:
            m2.temphealth -= 3
    elif monsternum == 3:
        if (myguy.damage - m1.defence) >= 3:
            m1.temphealth -= myguy.damage - m1.defence
        else:
            m1.temphealth -= 3
        if (myguy.damage - m2.defence) >= 3:
            m2.temphealth -= myguy.damage - m2.defence
        else:
            m2.temphealth -= 3
        if (myguy.damage - m3.defence) >= 3:
            m3.temphealth -= myguy.damage - m3.defence
        else:
            m3.temphealth -= 3
    return m1, m2, m3
def healerspecial(myguy, health):
    print "RES-URR-ECTION!!!!!!!"
    myguy.lives -= 1
    myguy.temphealth = health
    myguy.tempdamage = myguy.damage
    myguy.tempregeneration = myguy.regeneration
    myguy.tempdefence = myguy.defence
    return myguy
def assassinspecial(m1, m2, m3, monsternum):
    if monsternum == 1:
            m1.temphealth /= 2
            m1.damage /= 2
            m1.defence /= 2
            m1.regeneration /= 2
    elif monsternum == 2:
            m1.temphealth /= 2
            m1.damage /= 2
            m1.defence /= 2
            m1.regeneration /= 2
            m2.temphealth /= 2
            m2.damage /= 2
            m2.defence /= 2
            m2.regeneration /= 2
    elif monsternum == 3:
            m1.temphealth /= 2
            m1.damage /= 2
            m1.defence /= 2
            m1.regeneration /= 2
            m2.temphealth /= 2
            m2.damage /= 2
            m2.defence /= 2
            m2.regeneration /= 2
            m3.temphealth /= 2
            m3.damage /= 2
            m3.defence /= 2
            m3.regeneration /= 2
    return m1, m2, m3
def Attack(Attacker, Defender, recurnum):
    if recurnum == 0:
        return Defender.temphealth
    else:
        if (Attacker.damage - Defender.defence) > 0:
            Defender.temphealth -= (Attacker.damage - Defender.defence)
        else:
            Defender.temphealth -= 5
        return Attack(Attacker, Defender, recurnum - 1)
def Move(location, mmove):
    doors={"1A":4,"1B":6,"1D":5,"1C":2,"2A":1,"2B":6,"2C":3,"2D":5,"3A":2,"3C":4,"3D":5,"3B":6,"4A":3,"4B":6,"4C":1,"4D":5,"5A":2,"5B":3,"5C":4,"5D":1,"6A":2,"6B":1,"6C":4,"6D":3,
           "7A":10,"7B":12,"7D":11,"7C":8,"8A":7,"8B":12,"8C":9,"8D":11,"9A":8,"9C":10,"9D":11,"9B":12,"10A":9,"10B":12,"10C":7,"10D":11,"11A":8,"11B":9,"11C":10,"11D":7,"12A":8,"12B":7,"12C":10,"12D":9,
           "13A":16,"13B":18,"13D":17,"13C":14,"14A":13,"14B":18,"14C":15,"14D":17,"15A":14,"15C":16,"15D":17,"15B":18,"16A":15,"16B":18,"16C":13,"16D":17,"17A":14,"17B":15,"17C":16,"17D":13,"18A":14,"18B":13,"18C":16,"18D":15,
           "19A":22,"19B":24,"19D":23,"19C":20,"20A":19,"20B":24,"20C":21,"20D":23,"21A":20,"21C":22,"21D":23,"21B":24,"22A":21,"22B":24,"22C":19,"22D":23,"23A":20,"23B":21,"23C":22,"23D":19,"24A":20,"24B":19,"24C":22,"24D":21,
           "25A":28,"25B":30,"25D":29,"25C":26,"26A":25,"26B":30,"26C":27,"26D":29,"27A":26,"27C":28,"27D":29,"27B":30,"28A":27,"28B":30,"28C":25,"28D":29,"29A":26,"29B":27,"29C":28,"29D":25,"30A":26,"30B":25,"30C":28,"30D":27,
           "31A":34,"31B":36,"31D":35,"31C":32,"32A":31,"32B":36,"32C":33,"32D":35,"33A":32,"33C":34,"33D":35,"33B":36,"34A":33,"34B":36,"34C":31,"34D":35,"35A":32,"35B":33,"35C":34,"35D":31,"36A":32,"36B":31,"36C":34,"36D":33,}
    while True:
        if mmove == 0:
            whereto = raw_input("Which door would you like to exit from? Type A for north, B for east, C for south, and D for west: ")
            if "A" in whereto or "B" in whereto or "C" in whereto or "D" in whereto:
                plocation = doors[str(location)+whereto]
                break
            else:
                print "Enter a valid answer, good sir!"
        elif mmove == 1:
            choices = ["A", "B", "C", "D"]
            c = random.randrange(4)
            whereto = choices[c]
            plocation = doors[str(location)+whereto]
            break
    return plocation
def Pass(myguy):
    if myguy.temphealth < (myguy.health - myguy.regeneration):
        myguy.temphealth += myguy.regeneration
    else:
        myguy.temphealth = myguy.health
    return myguy
def Special(myguy, choice, monsternum, m1, m2, m3):
    if choice == 0:
        m1, m2, m3 = knightspecial(myguy, monsternum, m1, m2, m3)
    elif choice == 1:
        m1, m2, m3 = magespecial(myguy, monsternum, m1, m2, m3)
    elif choice == 2:
        lives, temphealth, tempdamage, tempregeneration, tempdefence = healerspecial(myguy)
    elif choice == 3:
        m1, m2, m3 = assassinspecial(m1, m2, m3, monsternum)
    if choice != 2:
        return m1, m2, m3
    else:
        return lives, temphealth, tempdamage, tempregeneration, tempdefence
