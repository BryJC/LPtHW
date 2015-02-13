from ex45_bm import *
from ex45_other import Gun
from sys import exit


###
class Scene(object):

    def level(self):
        exit(1)
        
        
###        
class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map
        
    def play(self):
        current_scene = self.scene_map.first_scene()
        last_scene = self.scene_map.input_scene('vic')
        
        while current_scene != last_scene:
            next_scene_name = current_scene.level()
            current_scene = self.scene_map.input_scene(next_scene_name)
            
        current_scene.level()
        
###
#
class Lobby(Scene):

    def level(self):
        print "\n<You enter a lobby and approach your instructor>"
        print "\n\t'Hello trainee! Time to test your biotic skills in the Grissom Academy training grounds.\n\tYou will undergo a series of three exercises designed to test your biotic abilities.\n\tIf you can pass these obstacles,\n\tyou will be permitted to join the ranks of the Systems Alliance Biotic Corps!'"
        print raw_input("\nAre you ready?>> ")
        return 'ex1'
        
#        
class Exercise_1(object):

    def level(self):
        print "\n<You enter a large room with three small objects,\nand observe three similarly shaped holes in the distance.>\nFrom a loudspeaker>>"
        print "\n\t'Okay trainee! Time for the first exercise.\n\tLet's see if you can put three small objects into their respective slots\n\tusing lift and throw only. Begin!>>'\n"
        
        stones = 3
        while stones > 0:
        
            lft = Lift()
            in_lft = lft.action() 
            if in_lft == 'success':
            
                thw = Throw()
                in_thw = thw.action()  
                if in_thw == 'success' and stones != 1:
                    print "\n\t'Now for the next stone!'"
                    stones -= 1
                elif in_thw == 'success' and stones == 1:
                    print "\n\t'Finished!'"
                    stones -= 1
                elif in_thw == 'failure':
                    return 'ex1'
                    break
                else:
                    exit(1)
                    
            elif in_lft == 'failure':
                return 'ex1'
                break
            else:
                exit(1)
                
        if stones == 0:
            print "\n\t'Good job trainee, time to move on to the next exercise.'"
            return 'ex2'
        else:
            exit(1)

#
class Exercise_2(object):

    def level(self):
        print "\n<You run into a room with three huge shoots pointed at you,\nlooking like they're about to unleash something...>\nFrom a loudspeaker>>"
        print "\n\t'Next up is the 'Lock 'n' Shock' task!\n\tYou must envelop the drone swarms in a singularity,\n\tthen knock them out with a powerful shockwave. Begin!'\n"
        
        swarms = 3
        while swarms > 0:
        
            sgy = Singularity()
            in_sgy = sgy.action()
            if in_sgy == 'success':
            
                sxw = Shockwave()
                in_sxw = sxw.action()
                if in_sxw == 'success' and swarms != 1:
                    print "\n\t'Good job trainee, you're doing good.'\n"
                    swarms -= 1
                elif in_sxw == 'success' and swarms == 1:
                    print "\n\t'Finished!'"
                    swarms -= 1
                elif in_sxw == 'failure':
                    return 'ex2'
                    break
                else:
                    self.level()
                    
            elif in_sgy == 'failure':
                return 'ex2'
                break
            else:
                self.level()
                
        if swarms == 0:
            print "\n\t'Time for something quicker...'"
            return 'ex3'
        else:
            self.level()

#
class Exercise_3(Scene):

    def level(self):
        print "\n<Feeling confident, you stroll into the next chamber.\n...All around you, the walls and floor begin to melt!>\nFrom a loudspeaker>>"
        print "\n\t'Your final task is The Melt Challenge!\n\tYou must use your biotic charge skills to jump to the nearest clear spot.\n\tNova can be used to temporarily give you more time to jump.\n\tBegin!'\n"
        
        floor = 3
        while floor > 0:
        
            chg = Charge()
            in_chg = chg.action()
            if in_chg == 'success':
            
                nva = Nova()
                in_nva = nva.action()
                if in_nva == 'success' and floor != 1:
                    print "\t'Jump again!'\n"    
                    floor -= 1
                elif in_nva == 'success' and floor == 1:
                    print "\n\t'Finished!'\n"
                    floor -= 1
                elif in_nva == 'failure':
                    return 'ex3'
                    break
                else:
                    self.level()
                    
            elif in_chg == 'failure':
                return 'ex3'
                break
            else:
                self.level()
                
        if floor == 0:
            print "\n\t'Congrats trainee, you did great.\n\tCome meet me back in the lobby.'"
            return 'fi1'
        else:
            self.level()
        
#       
class Fight_1(Scene):

    def level(self):
        print "\n<Feeling great from finishing the course, you leave the test chamber.\nSuddenly, you hear a huge BOOM coming from next door!>\nFrom a loudspeaker>>"
        print "\n\t'Trainee! Mercenaries have infiltrated the station!\n\tWe are on our way, but you need to delay them!\n\tUse your biotic skills to defend the station!'"
        print "\n<You move out into the shuttle bay,\nwhere you see a group of three mercs, carrying stolen eezo.\nBeside you is a weapons locker. You grab the Avenger within it.>"
        
        choices = raw_input("\nWhich power should I use? (Barrier or Dominate) ")
        if choices.lower() == 'barrier':
            brr = Barrier()
            brr.action()
            
            merc = 3
            while merc > 0:
            
                atk = Gun()
                in_atk = atk.shoot()

                if in_atk == 'success' and merc != 1:
                    print "\tHit! The merc is down!"   
                    merc -= 1
                elif in_atk == 'success' and merc == 1:
                    merc -= 1
                elif in_atk == 'failure':
                    return 'fi1'
                    break
                else:
                    self.level()
                
            if merc == 0:
                print "\tThe merc's are out!\n\tTime to find their ride..."
                return 'fi2'
  
        elif choices.lower() == 'dominate':
            print "\n<You attempt to use dominate to force one of the shooters to attack the others.\nUnfortunately, the other two catch on and quickly knock the affected one out.\nThey spot you and flood you with bullets,\nbreaking your barrier and killing you.>"
            return 'death'
        else:
            return self.level()
        
#        
class Fight_2(Scene):

    def level(self):
        print "\n<You enter the shuttle bay and see the shuttle pilot at the helm. This is going to be tricky...>"
        choices = raw_input("\nWhich power should I use? (Barrier or Dominate) ")
        
        if choices.lower() == 'dominate':
            dmn = Dominate()
            in_dmn = dmn.action()
            if in_dmn == 'success':
                print "\n<You direct him using biotic impulses to land the ship, leave it unarmed, and turn himself over to you>"
                print "\n\t'Thanks for being so cooperative pal.'"
                print "\n<You then knock him out with the butt of your gun,\nleaving him for station security.>"
                return 'vic'
        elif choices.lower() == 'barrier':
            print "\n<You power up your barrier and try to take out the shuttle pilot head on.\nUnfortunately for you, his shields are up, rendering your Avenger almost worthless.\nBefore you even finish unloading your clip he train's the shuttle's guns on you and blasts you to smithereens.>"
            return 'death'
        else:
            return self.level()
        
#       
class Victory(Scene):

    def level(self):
        for i in range(5):
            print '-...-'
        print "\n<You have acheived victory!>"
        print "\n<Your instructor runs in with station forces>\n\t'Great Job, you managed to hold them off!\n\t It looks like you\'re definitely ready for the big leagues... CADET :-)'\n"
        exit(1)
        
#        
class Failure(Scene):

    def level(self):
        print "\n<You failed, oh no!>\n"
        return a_game.play()
        
#        
class Death(Scene):

    def level(self):
        print "\n<You died, oh NO!>\n"
        return a_game.play()
        

###
class Map(object):

    scenes = {
        'lobby': Lobby(),
        'ex1': Exercise_1(),
        'ex2': Exercise_2(),
        'ex3': Exercise_3(),
        'fi1': Fight_1(),
        'fi2': Fight_2(),
        'vic': Victory(),
        'failure': Failure(),
        'death': Death()
        }
        
    def __init__(self, start_scene):
        self.start_scene = start_scene
        
    def input_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val
        
    def first_scene(self):
        return self.input_scene(self.start_scene)        


###
a_Map = Map('lobby')
a_game = Engine(a_Map)
a_game.play()

# things left to fix - 'None' type issue, try/except error with nova situation
