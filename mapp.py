import random
import random
def roomgenerator():
    list1 = ["This first room is filled with large winch contraptions. Beneath these are trapdoors that are now locked closed. You can tell that this is how the kidnappers got down to the palace", "This room has a small kitchen area off to one side, complete with butchered animals hanging from the ceiling", "This room appears to be a dining area. Tables and chairs are pushed up against the walls, and there are beer kegs (now empty) also lining the walls.", "This room appears to be a barracks of some kind. There are several sets of bunk beds. The sheets of the bed are ruffled, and the beds messy. You find this stunning lack of proper military procedure deplorable", "This room appears to be an armory. Empty weapon racks line the walls, and there are many discarded odds and ends from armour. A target dummy stands against one wall. Upon closer inspection, yuo can see that it is a poorly made rendering of you!", "This room is fairly empty. However, there are a few things of note. First, there is a table with cards on it. It looks like whoever was here was in the middle of a game before you arrived", "This room is a barracks of some kind. There are several sets of bunk beds. These beds have sheets that are folded to military prescision, perfectly straight, and ordered. You can't help but feel a bit of respect for the commanding officer of these orcs.", "Thir room appears to be an armory. Empty weapon racks line the walls. There are also several dismantled suits of armour here. They are too damaged to wear, and look to be in the middle of being repaired", "This room has the look of a tavern. There is a bar on one end, and bottles of wine locked into a cabinet. The bar stools are lined up on the counter, and there is a dart board on one wall (without darts)", "When you first enter this room, you are hit by the foul smell of feces. This room is a lavatory. There are several chamber pots along the walls.", "This room is filled with treasure chests. Although carrying any of these things now will make it hard for you to fight effectively, you may be able to grab them on the way out", "This room stinks. Filled with decaying corpses, and garbage, it is a pigsty. You can see in the corner a pile of refuse that appears to be a bed of some kind."]
    list2 = ["A horrid stench greets you in this room. Worse than anything you hace ever smelled before. It is the stench of death, of rooting corpses. Everywhere you look there are the remnants of corpses, partially decayed. You can tell that this floor is the workshop of one of the Giant King's Necromancers.", "This room is decortaed with engravings of skulls on the lintels and walls. There are a few coffins in niches in the walls. They are nailed shut, but you can har faint banging and scratching comign from within. If the Necromancer nailed these guys away, you don't want to go opening them", "This room is decorated with engravings of skulls on the lintels and walls. There are a few coffins in niches in the walls. These coffins appear to have been broken open, then closed again at some point in time", "This room has the look of a moratorium. Deseaced creatures of all kinds are tied, or strapped down to morgue tables, neatly sliced apart. Many of them have had their insides taken out and spread out beside them", "This room is filled with piles of bones. You have trouble walking even, as the bones are about ankle deep. You shudder to think how many must have died to provide these bones.", "This room is as bad as any of the others. An altar is in here, covered in gore and entrails, devoted to some foul god.", "This necromancer is truly deplorable, almost as bad as the Mad Lich that you faced in the Giant King's old castle. This room seems to be set up as a a greeting for you. Heads of soldiers, soldiers you once knew and fought beside, are mounted pn stakes all around the room. You fight down the urge to empty your stomache", "This room is not as bad as many fo the others. Cleaned with an almost surgical and maniacal intensity, it is filled with shelves and shelves of books. Upon first lookt ehy appear to all be necromantic grimoires, of little use to you", "This room has neatly stacked and ordered limbs, with flesh still on them (although partailly decayed). It seems that you have found the room where the Necromancer creates his zombies.", "This room is disusting, even compared to the others. Cages line the walls, and in these cages lie the screaming remains of what were once people. The cells are splattered with gore, and many of the people have clawed their own eyes out. They look too far gone, too insane, to save. They would probably tear you apart if you opened the cells.", "This room has a great stand. Upon it, you can see a great arcane grimoire. As you reach out to touch it, you hit an invisible wall. it is evidently well warded.", "This room is horrid, decorated with skull motifs, the domain fo the Necromancer. Corpses and skeletons litter the room. It strikes you that not once have you seen a bed for this necromance. He must never sleep."]
    list3 = ["Space seems distorted here, and it is hotter than it was. This is, you assume, the domain of the giants, who are immune to fire", "This room is very odd. The further from the center you go, the starnger things get. Space seems to warp, such that there is room for many bunk beds, sized for ginats against the walls, but in the center of the room, a giant could barely stand up straight. Being this close to the core of the ship must be affecting reality", "This room is freezing cold. You know that staying here for too long without some kind of coat may be the death of you.", "This room appears to be some kind of magical kitchen. Pots and pans swirls, and clatter, and steaming piles of food pile up in one corner where the pans dump them. Howeverm the food smells inedible, fit only for a giant's palatte", "This room has a floor of glass. However, instead of seeing the level of the Necromancer, you instead see a brilliant light. After adjusting to the light, you can see that the rooms floor looks out on a sun!", "This room seems unremarkable. And by seems, we mean is", "This room is unremarkable. It is smallish in size, and entirely plain. You suppose that even monstrous giants need a break from the reality defying laws of their craft.", "This room is filled with the gentle sounds of flowing fountains. Several small fountains are dotted around the room,and this produces a calming effect (but no other effect at all. Don't drink from the fountain, we mean it)", "This room is odd, even for the giants ship. Stepping in one direction takes you in the opposite, and turning left makes the world spin to the right. It is difficult to do anything (except fight)", "The room is empty. At first. Then, as you look more, things start to fade into existence on the walls. After another moment, you can see that they are paintings. Inside the ship, where reality fails, where they kidnapped a princess, the Giants built an art gallery. Maybe you haev misjudged these creatures. Or maybe not. You are probably reading too much into things", "This room is a great forge. You can see a slot for a ring, and a sword. The label on the furnace reads:\n'Place you your magic treasures here,\nAnd we shall return one beyond compare\n\nAn 'Out of order' sign hangs over the slots", "This room is like a writing desk. Meaning that it is decorated with ravens."]
    list4 = ["The throne room. Filled with rubble from the ceiling, it is a shadow of its former glory. There is nothing more to see here but a rope up to the ship. All the doors and windows are blocked by rubble"]
    listlist = [list1, list2, list3]
    #1st is the start room. sixth is the halfway ladder. 11th is the treasure room. 12 is the boss room (except for the last list. 12 is the final ladder for that). the extra list has the very first room, and the final boss room
#    Rooms=[ [0,"",""],[0,"",""],[0,"",""],
 #           [0,"",""],[0,"",""],[0,"",""],
  #          [0,"",""],[0,"",""],[0,"",""],
   #         [0,"",""],[0,"",""],[0,"",""],
    #        [0,"",""],[0,"",""],[0,"",""],
     #       [0,"",""],[0,"",""],[0,"",""],
      #      [0,"",""],[0,"",""],[0,"",""],
       #     [0,"",""],[0,"",""],[0,"",""],
        #    [0,"",""],[0,"",""],[0,"",""],
         #   [0,"",""],[0,"",""],[0,"",""],
          #  [0,"",""],[0,"",""],[0,"",""],
           # [0,"",""],[0,"",""],[0,"",""]]
    Rooms=["","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""]
    y=0
    for z in range (3):
        for i in range (12):
            #location=z+(i*.01)
            description=listlist[z]
            x=random.randrange(12)
            while description[x] in "xyz":
                x=random.randrange(12)
            Rooms[y]=description[x]
            description[x]="xyz"
            y+=1
    ntrap=random.randrange(12)+1
    ntreasure=random.randrange(12)+1
    nstairs=random.randrange(6)+1
    return Rooms, ntreasure, ntrap, nstairs
def perform(location, ntrap, ntreasure, nstairs, myguy):
    if location == ntreasure or location == ntreasure+12 or location == ntreasure+24:
            print "you have found a treasure"
            myguy.damage+=30
            myguy.tempdamage+=30
    elif location == ntrap or location== ntrap+12 or location== ntrap+24:
        if location == ntrap:
            x=input("There seems to be a set of stairs to the next floor, but they seem to be shaky. you can not tell whats beyond the stairs. would you go up or stay on the same level? 1 for stay, 0 to go up the stairs")
            if x == 1:
                print "you see the stairs fade out as you decide to stay at your floor"
            else:
                print "HAHAHAHAHAHAHA, you fell for it, tell me how you feel, wait i don't care. you took damage for the fall by the way" 
                myguy.temphealth= myguy.temphealth-((.5)*(myguy.temphealth))
        elif location == ntrap+12:
            x=raw_input("There seems to be a dark energy coming from the corners of this room. a riddle appears in front of you: Clad and mail never clinking, never thristy always drinking, alive without breath as cold as death")
            while "fish" not in x:
                print ("Nice try, but you failed, be ashamed, as a punishment you take"+(0.02*myguy.temphealth)+"damage")
                x= raw_input("Now i would ask how you feel but you know i don't care, so just go ahead and guess again")
            print "eh i'll get you later don't worry"
        elif location== ntrap+24:
            print "If a fat boy fell at a height of 13 meters and his weight was 249 kg what would his speed be before hitting the ground?"
            x=input(":) physics ftw, now becareful cause if you fail you will fall just like the fat boy")
            y=(((249*9.8*13)*2)/249)^0.5
            if (y-1) < x < (y+1) :
                print " ah, well i guess your not sleeping during physics class"
            else:
                myguy.location-=12
                print "now now don't cry we all thought physics was useless. but think again"
    elif location == nstairs or location == nstairs+6 or location == nstairs+12 or location == nstairs+18 or location == nstairs+24 or location == nstairs+30:
        x= input("would you like to go to the next level? 1 for yes 83 for no")
        if x==1:
            myguy.location+=6
            print "You moved to the next level"
    #return myguy


