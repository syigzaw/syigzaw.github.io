def intro():
    print\
"""
You know who you are. But, for the sake of story purposes, I will tell you anyways. But, like any good story, this must start in the same old way...

    A long time ago, in a faraway land, lived a princess in her castle golden. Her father had recently died, leaving her with no family remaining in the world, and only a few loyal retainers and servants remaining. You were always the most loyal of her servants, and so she trusts you implicitly.
    Alone, with no help, you had to try and regain control over a land rebelling. You left her for a time, to try and restore order. That task accomplished, you returned to the castle. After a time helping the princess, you started to feel that maybe there was...something more between the two of you.
    However, before it could become anything more, disaster struck.
    An army was marching towards the kingdom, led by the evil Giant King, in his floating fortress. You marched out to lead the army against this new threat.
    Many months, and many battles followed. Slowly but surely, under your leadership, the soldiers beat back the enemy, right to the gates of the Giant King's castle. You yourself led the march into the castle, doing battle with orcs, trolls, giants, and zombies. Finally, you reached his steward, the Dread Necromancer, the Lich King. You managed to defeat him, but barely. With his last moments, the Lich cursed you, draining your powers away.
    Weakened, you left the castle, and left the fighting to lesser generals. As you marched back, you heard more and more news of the Giant King's forces being pushed further back. But, of the king himself, there was no sign.
    In a panic, you fled back to the princess, sure that the Giant King would kidnap her. However, when you arrived at the castle, all was well.
    Greeted by a fanfare of trumpets, you march boldy to the throne room, where, the princess is seated happily. She greets you with a smile.
    "And how is my favourite, brave, noble General today?"

"""
    raw_input("-->")

    print\
"""
    Before she has a chance to respond, there is a terrible grating crashing noise, and the throne room ceiling collapses. A large piece of rubble falls, and pins you, so that you cannot move.
    Through the hole you can see a giant cube of black metal floating above the castle. It is the Giant King's floating fortress. Holes open in the bottom, and orcs slide down on ropes, along with giants.
    The giants grab the princess, and climb back up the ropes. One of the orcs stays behind, and the rest climb up too.
    As they climb, the princess screams, and shouts for you to help her please!, and that she loves you, please, save her!
    The giants cackle evilly, and the floating fortress appears to be getting ready to leave. The trapdoors they came through all close, but one. A rope hangs down from that for the one orc remaining, who seems to be intent on desecrating the throne room.

    You despair for a moment of ever finding her and saving her, but then you realize that love cannot be stopped! You push the rubble off of you, and climb to your feet. A scream of rage seems ready to burst from your lips.
    You leap up, kill the guard, and climb the rope into the firt room.
"""

def conclusion():
    print\
"""
    The Giant King lies dead before you, and there, tied up is the princess.
    You rush forwards, and untie her, and she falls into your arms. You hold her up, and she looks into your eyes. You can tell that she wants to say something, as she opens her mouth. Suddenly, the ship jolts, and you can tell that the ship is falling out of the sky, the magic that held it aloft dead like the king.
    You have to time for a happy reunion. You grab the princess by the hand, and run for the ladder. As you run to the surface, you pass many fleeing monsters, but they have no interest in you anymore, and you none in them. You get to the top of the castole, and stand there. There are no life boats, nothing to get you to safety.
    The ground rushes up towards you, and you fear that this is the end.
    Suddenly, you see one last life boat. You jump aboard, and cast off.
    You float down sedately to the ground, as the floating fortress comes down a ways off. In a spectacular explosion, it lands, and is destroyed. You and the princess stand there, and watch it.
    Suddenly, you realize that neihger of you have let go of the others hand. She looks up at you, and in her eyes you can see happiness, and thankfulness.
    'My hero' she says, and puckers her lips
"""
    while True:
        action = raw_input("-->")
        if "kiss" in action:
            break
        else:
            print "You evidently know nothing about women"
    print "You lean forward to kiss her, with the setting sun framing the two of you as the screen fades to black.\n\n\n...You win! CONGRADULATIONS! YOU HAVE WON OUR GAME! HOORAY!"

def dead():
    print "You died. Nothing more, nothing less. Now you can, forwards into the great divide, into the drift, into the endless sleep, knowing that you have failed your love, and your kingdom. Congradulations. You are a loser (at this game). You have doomed the princess to an eternity of torutre at the hands of the Giant King. But guess what? She never liked you anyways. This was all just an elopement, when she was to run away with her prince, the Giant King. They shall live happily ever after in the clouds above us all, and laugh at youyr failure. YOU LOSE!"

def boss(location):
    if location == 36:
        print "This room is stiflingly hot. You don't see how anyone can stand it. However, across the way, you can see who you have come here to get. The Princess. She is safe! Praise the Gods!\nUpon seeing you, hope floats across the Princesses face, but then turns to horror.\n'No! Don't come near!' she cries 'He will destroy you!'\nYou can't see any threat, so you start out across the room, when, from the lavapool below, a great Giant, twice the size of any before leaps out, flinging lava everywhere.\n'Do you really think to take my prize from me?' he bellows 'No, rather, I'll grind your bones to make my bread!! Mwa ha ha ha ha ha! Die foolish human!' He draws a great black sword out from the scabbard across his back, and lunges towards you."
    elif location == 24:
        print "This room is filled with necromantic energies. Standig before you is a hooded figure with a staff in one hand. It raises its head, and you can see sunken eyes in a pale face. 'Ny-ahahaha' it cackles. 'Weclome to your demise!'"
    elif location == 12:
        print "A great hulking beast fills this room. It turns to face you, showing its great scaly hide, and warty face. It stands, and you can see mighty claws at the end of each hand. The Beast charges!"
    else:
        print "Before you you see a great piece of what looks like Jello (tm) The great blob is slightly green tinged, but with undefined boundaries. It will be hard to hit"

#main

