class Lexicon(object):
    
    def __init__(self):
        
        self.lex_dict = {
            'direction': ['north', 'south', 'east', 'west', 'northeast', 'southeast', 'northwest', 'southwest'],
            'verb': ['go', 'kill', 'eat', 'drive', 'shoot', 'walk', 'talk', 'act', 'fight', 'hug', 'kiss', 'run', 'sprint'],
            'stop': ['the', 'in', 'of', 'a', 'some', 'for', 'from', 'to', 'with'],
            'noun': ['bear', 'princess', 'honey', 'german', 'american', 'bee', 'prince', 'knight', 'warrior', 'gun', 'bow', 'woman', 'women', 'man', 'men', 'mile', 'kilometer' ],
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
                    plural = list(i.lower())
                    if i.lower() in value:
                        found_cat = key
                        break
                    else:
                            plural = list(i.lower())
                            if plural[(len(plural)-2):(len(plural))] == ['e', 's']:
                                i_adj = ''.join(plural[:(len(plural)-2)])
                                if i_adj in value:
                                    found_cat = key
                                    break
                                else:
                                    found_cat = 'error1'
                            elif plural[(len(plural)-1):(len(plural))] == ['s']:
                                i_adj = ''.join(plural[:(len(plural)-1)])
                                if i_adj in value:
                                    found_cat = key
                                    break
                                else:
                                    found_cat = 'error2'
                            else:
                                found_cat = 'error3'
                self.path.append((found_cat, i))
        return self.path
        
lexicon = Lexicon() 
