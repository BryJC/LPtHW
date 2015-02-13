from random import choice

class Gun(object):

    def shoot(self):
    
        target = ('high', 'low', 'gut')
        hit_point = choice(target)
        
        while True:
        
            choices = raw_input("Do I aim high, low, or at the gut? ")
        
            print '\nx-- x-- x-- \n'
            if choices.lower() == hit_point:
                return 'success'
                break
            elif choices.lower() != hit_point:
                print "Miss!\nAh! I'm taking fire!\nMy barrier won't last forever..."
            else:
                return False
        
            
            
            
            
        
