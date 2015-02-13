from random import randint, choice
from sys import exit

class Biotics(object):

    def action(self):
        print "I'm powering up..."
        
        
class Lift(Biotics):

    def action(self):
        tries = 4
        y = randint(1,20)
        while tries > 0:
            x = int(raw_input("\n<You attempt a lift... (enter a # 1-20)?> "))
            if x+4 >= y and x-4 <= y:
                print "\n\tI lift the stone up into the air..."
                return 'success'
                break
            elif not x+4 >= y or not x-4 <= y:
                if tries == 1:
                    tries -= 1
                elif tries != 1:
                    print "\n\tI couldn't lift it. I will try again..."
                    tries -= 1
                else:
                    exit(1)
            else:
                exit(1)
        if tries == 0:
            print "\n\tBleergh"
            return 'failure'
        else:
            exit(1)
        
class Throw(Biotics):

    def action(self):
        tries = 4
        y = randint(1,20)
        while tries > 0:
            x = int(raw_input("\n<You attempt a throw... (enter a # 1-20)?> "))
            if x+3 >= y and x-3 <= y:
                print "\n\t...and then I punch it into its spot!"
                return 'success'
                break
            elif not x+3 >= y or not x-3 <= y:
                if tries == 1:
                    tries -= 1
                elif tries != 1:
                    print "\n\tI couldn't throw it. I will try again..."
                    tries -= 1
                else:
                    exit(1)
            else:
                exit(1)
        if tries == 0:
            print "\n\tBleergh"
            return 'failure'
        else:
            exit(1)
        
class Singularity(Biotics):

    def action(self):
        
        tries = 3
        swarm_num = randint(1,3)
        while tries > 0:
            x = int(raw_input("What shoot should I send the singularity towards\n(give 1, 2, or 3)? "))
            if x == swarm_num:
                print "\n\tI cast a singularity towards the shoot just as a swarm appears there, hitting the' bots!"
                return 'success'
                break
            elif x != swarm_num:
                if tries == 1:
                   print "\n\tI missed!"
                   tries -= 1
                elif tries != 1:
                    print "\n\tI missed! I will send another...\n"
                    tries -= 1
                else:
                    exit(1)
            else:
                print "\n\tBleergh"
                return 'failure'
        if tries == 0:
            print "\n\tBleergh"
            return 'failure'
        
class Shockwave(Biotics):

    def action(self):
            print "\n\tI blast them with a shockwave, taking them out!"
            return 'success'
        
class Charge(Biotics):

    def action(self):
        y = ('weak','solid','strong')
        z = choice(y)
        while True:
            x = raw_input("How powerful should I make this first jump (weak, solid, strong) ")
            if x == z:
                print "\n\tI move through a biotic field, charging to the next open spot.\n"
                return 'success'
                break
            elif x != z:
                print "\n\tI missed the landing spot! I have to quickly get to a clear area!\n"
            else:
                print "\n\tBleergh"
                return 'failure'
        
class Nova(Biotics):

    def action(self):
        x = int(raw_input("How many biotic points will you put into this nova(1-5)? "))
        y = randint(1,2) + randint(1,3)
        if x > y:
            print "\n\tI clear away the melting floor by shaking the ground with a Nova!\n"
            return 'success'
        elif x <= y:
            print "\n\tMy Nova was too small! I have to try again...\n"
            return self.action()
        else:
            print "\n\tBleergh"
            return 'death'
        
class Barrier(Biotics):

    def action(self):
        print "\nI surround myself with a powerful biotic shield."

        
class Dominate(Biotics):

    def action(self):
        print "\nAlright, I need to use my biotic powers to overload some neurons in this guy.\nI'll have to feel my way around his mind and find the ones that will allow me to control his decisions."
        
        n_board = []
        
        for i in range(5):
            n_board.append(["@"] * 6)   
        
        def new_bod(board):
            for row in board:
                print " ".join(row)
                pass
                            
        print new_bod(n_board)
        
        correct_seq = (
            ('up', 1, 0, '^'),
            ('up', 0, 0, '^'),
            ('right', 0, 1, '>'),
            ('right', 0, 2, '>'),
            ('down', 1, 2, 'v'),
            ('down', 2, 2, 'v'),
            ('down', 3, 2, 'v'),
            ('down', 4, 2, 'v'),
            ('right', 4, 3, '>'),
            ('right', 4, 4, '>'),
            ('right', 4, 5, '>'),
            ('up', 3, 5, '^'),
            ('up', 2, 5, '^'),
            ('left', 2, 4, '<'),
            ('up', 1, 4, '^'),
            ('up', 0, 4, '^'),
            )
        
        print "\n\tI think I'll start...HERE!"
        n_board[2][0] = ':' 
        new_bod(n_board)
            
        print "\n\tNow I must move through the neurons and get the correct pattern,\n\tonly then will I have control over his mind!"
        
        for key, v1, v2, v3 in correct_seq:
            while n_board[v1][v2] != v3:
                askd = raw_input("\nWhich direction should I move in the neural map?\n(up, down, left, right)\n ")  
                if askd == key:
                    print "\n\tA hit! Let's continue on...\n"
                    n_board[v1][v2] = v3
                    print new_bod(n_board) 
                elif askd != key:
                    print "\n\tDoesn't seem to have any effect. Better try another...\n"
                else:
                    print "Huh?"
                
        while n_board[4][4] != 'X':
            final_guess = raw_input("\nWhich final direction should I go? ")
            if final_guess == 'right':
                print "\n\tLooks good! Yes, his brain is mine!"
                n_board[0][5] = ':'
                new_bod(n_board)
                return 'success'
            else:
                print "\n\tI don't think that's the best choice..."
                
        # issue with 'None' type

   
        
        
        
