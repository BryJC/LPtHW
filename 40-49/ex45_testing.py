from ex45_other import Gun
from ex45_bm import Barrier, Dominate

class Fight_1(object):

    def level(self):
        print "\n<Feeling great from finishing the course, you leave the test chamber.\nSuddenly, you hear a huge BOOM coming from next door!>\n<From a loudspeaker>"
        print "\n\t<<Trainee! Mercenaries have infiltrated the station!\n\tWe are on our way, but you need to delay them!\n\tUse your biotic skills to defend the station!>>\n"
        print "<You move out into the shuttle bay,\nwhere you see a group of three mercs, carrying stolen eezo.\nBeside you is a weapons locker. You grab the Avenger within it.>\n"
        
        choices = raw_input("\n\tWhich power should I use? (Barrier or Dominate) ")
        if choices.lower() == 'barrier':
            brr = Barrier()
            brr.action()
            
            merc = 3
            while merc > 0:
            
                atk = Gun()
                in_atk = atk.shoot()

                if in_atk == 'success' and merc != 1:
                    print 'Hit! The merc is down!'   
                    merc -= 1
                elif in_atk == 'success' and merc == 1:
                    merc -= 1
                elif in_atk == 'failure':
                    return 'fi1'
                    break
                else:
                    exit(1)
                
            if merc == 0:
                print "The merc's are out!\nTime to find their ride..."
                return 'fi2'
  
        elif choices.lower() == 'dominate':
            print "\n<You attempt to use dominate to force one of the shooters to attack the others.\nUnfortunately, the other two catch on and quickly knock the affected one out.\nThey spot you and flood you with bullets,\nbreaking your barrier and killing you.>"
            return 'death'
        else:
            return exit(1)
            
            
fi1 = Fight_1()
fi1.level()
