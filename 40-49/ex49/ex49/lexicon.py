class Lexicon(object):
    
    def __init__(self):
        
        self.lex_dict = {
            'direction': ['north', 'south', 'east', 'west', 'northeast', 'southeast', 'northwest', 'southwest'],
            'verb': ['go', 'kill', 'eat', 'drive', 'shoot', 'walk', 'talk', 'act', 'fight', 'hug', 'kiss', 'run', 'sprint'],
            'stop': ['the', 'in', 'of', 'a', 'some', 'for', 'from'],
            'noun': ['bear', 'princess', 'honey', 'german', 'american', 'bee', 'prince', 'knight', 'warrior', 'gun', 'bow', 'woman', 'women', 'man', 'men', 'miles', 'kilometers' ],
            'number': [range(0,)],
            }
        
        self.lex_dict_cats = self.lex_dict.keys()
    
    def scan(self, words):
        
        self.path = []
        splitwords = words.split()
        for i in splitwords:
            try:
                self.path.append(('number', int(i)))
            except ValueError:
                for key, value in self.lex_dict.iteritems():
                    if i.lower() in value:
                        found_cat = key
                        break
                    else:
                        found_cat = 'error'
                self.path.append((found_cat, i))
        return self.path
        
lexicon = Lexicon() 
#change script so it matches LPtHW 
