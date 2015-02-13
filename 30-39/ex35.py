from sys import exit
from random import randint

def gold_room():
    print "This room is full of gold! How much do you take?"
    
    choice = raw_input("> ")
    
    try:
        val = int(choice)
    except ValueError:
        print "Man, learn to type a number."
        gold_room()
        
    how_much = int(choice)
        
    if how_much < 50:
        print "Nice, you're not greedy, you win!"
        exit(0)
    else:
        dead("You greedy bastard!")
        
        
def bear_room():
    print """There is a bear here.\nThe bear has a bunch of honey.\nThe fat bear is in front of another door.\nHow are you going to move the bear?"""
    
    while True:
        choice = raw_input("> ")
        
        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear":
            xip = randint(1,11)
            if xip < 5:
                bear_moved = False
                dead("The bear gets pissed off and chews your leg off.")
            elif xip >= 5:
                bear_moved = True
                print "The bear has moved from the door. You can go through it now."
               
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print "I have no idea what that means"
            

def cthulhu_room():
    print """Here you see the great evil Cthulhu.\nHe, it, whatever stares at you and you go insane.\nDo you flee for your life or eat your head?"""
    
    choice = raw_input("> ")
    
    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()
        
        
def dead(why):
    print why, "Good job!"
    exit(0)
    
 
def start():
    print """You are in a dark room.\nThere is a door to your right and left.\nWhich one do you take?"""
    
    choice = raw_input("> ")
    
    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")
        
        
start()
            
