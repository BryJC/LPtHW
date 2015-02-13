from sys import exit
from random import randint

### draw out relationship between Scene, Map, Engine, and Scene_Subclasses


class Scene(object):

    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter."
        exit(1)
        
    
class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map
        
    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')
        
        while current_scene != last_scene:
             next_scene_name = current_scene.enter()
             current_scene = self.scene_map.next_scene(next_scene_name)
             
        # be sure to print out the last scene
        current_scene.enter()
             
        
class Death(Scene):

    quips = [
        "You died. You kinda suck at this.",
        "Your mom would be proud...if she were smarter.",
        "Such a luser.",
        "I have a small puppy that's better at this."
    ]
    def enter(self):
        print Death.quips[randint(0, len(self.quips)-1)]
        exit(1)
        
        
class CentralCorridor(Scene):

    def enter(self):
    
        print """The Gothons of Planet Percal #25 have invaded your ship and destroyed your entire crew. You are the last surviving member and your last mission is to get the neutron bomb from the Weapons Armory, infiltrate the bridge, and blow the ship up after escaping through a working escape pod.\n"""
        print raw_input("Do you understand your mission? Hit any button to continue ")
        print """You're running down the central corridor to the Weapons Armory when a Gothon jumps out, red scaly skin, dark grimy teeth, and an evil clown costume cloak his evil ways. He's blocking the door to the Armory and about to pull a weapon on you.\n"""
        
        action = raw_input("shoot, dodge, or tell a joke? ")
        action = action.lower()
        
        if action == "shoot":
            print """Quick on the draw you yank out your blaster and fire it at the Gothon. His clown costume is flowing around his body, which throws off your aim. Your laer singes his costume but does no serious damage. This sends him into an insane rage, and as a result he blasts you into infinity and beyond."""
            return 'death'
            
        elif action == "dodge":
            print """Like a world class boxer you dodge, weave, slip, and slide right as the Gothon's blaster cranks a bolt past your head. In the middle of your artful dodge your foot slips and you bang your head into the bulkhead, knocking you out. Permanently."""
            return 'death'
            
        elif action == "tell a joke":
            print """Lucky for you the brass made you learn Gothon insults in the academy. You tell the one Gothon joke you know - "I wouldn't want to start an ARMS race..." The Gothon dies laughing. You hop past him and through the Weapon Armory doors."""
            return 'laser_weapon_armory'
            
        else:
            print "Does not compute!"
            return 'central_corridor'
        
        
class LaserWeaponArmory(Scene):

    def enter(self):
    
        print """You do a dive roll into the Weapon Armory, crouch and scan the room for more Gothons that might be hiding. It's dead quiet... almost too quiet. You stand up and run to the far side of the room to find the neutron bomb in its container. There's a keypad lock on the box and you need the code to get the bomb out. If you get the code wrong ten times then the lock closes forever and the bomb is lost. The code is 3 digits long.\n"""
        
        code = randint(100, 110)
        guess = int(raw_input("Guess the Code! "))
        guesses = 0
        while guess != code and guesses < 10 :
            print 'WRONG'
            guesses += 1
            guess = int(raw_input("Guess the code! "))
        if guess == code:
            print """That's the correct code! The box opens up and you grab the neutron bomb. Time to run to the bridge..."""
            return 'the_bridge'
        else:
            print "Oh no! The box locks forever! Gothon's flood the armory and shoot you down."
            print code
            return 'death'
            
        
class TheBridge(Scene):

    def enter(self):
    
        print """You burst onto the Bridge with the neutron bomb under your arm and surprise five Gothons who are trying to take control of the ship. Each of them has an even uglier clown costume than the last. They haven't pulled their blaster's out yet, as they see the active bomb under your arm and don't want to set it off.\n"""
        
        action = raw_input("throw the bomb OR slowly place the bomb down? ")
        action = action.lower()
        
        if action == 'throw the bomb':
            print """In a panic you throw the bomb right at the center of the group of Gothons and make a leap for the door. Right as you drop it a Gothon shoots you right in the back killing you. As you die you see another Gothon frantically try to disarm the bomb. You die knowing they will probably blow up when it goes off. Your efforts have not been in vain."""
            return 'death'
            
        if action == 'slowly place the bomb down':
            print """You point your blaster at the bomb under your arm. The Gothons slowly put their hands up, starting to sweat. You inch backwards towards the door, punch the close button and blast the lock so the Gothons cannot get out.\nNow that the bomb is placed you run to the escape pod to get off this tin can."""
            return 'escape_pod'
        
        else:
            print "Does not compute!"
            return "the_bridge"
        
class EscapePod(Scene):
    
    def enter(self):
        print """You rush through the ship desperately trying to make it to the escape pod before the whole ship explodes. It seems like hardly any Gothons are on the ship, so your run is clear of interference. You get to the chamber with the escape pods, and now need to pick one to take. Some of them could be damaged but you don't have time to look. There are 2 pods, which one do you take?\n"""
        
        wking_pod = randint(1,2)
        guess = int(raw_input("Which pod do you take (1 or 2)? "))
        
        if guess == wking_pod:
            print """You climb in the %s pod and it shoots off successfully into space. You pilot the small craft out of the blast radius of the ship as you watch it explode, killing all the Gothons inside. Success!""" % guess
            return 'finished'
            
        else:
            print """You climb into the pod and try to shoot off. Unfortunately the pod implodes, killing you inside. Thankfully the ship explodes moments later. You're efforts are not in vain..."""
            return 'death'
            
class Finished(Scene):
    
    def enter(self):
        print "You won! Good job."
        return 'finished'   
                 
        
class Map(object):
    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished(),
    }
    
    def __init__(self, start_scene):
        self.start_scene = start_scene
        
    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val
        
    def opening_scene(self):
        return self.next_scene(self.start_scene) 
        
        
#####      
a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
#####  
        
        


