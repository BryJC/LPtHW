class Lexicon(object):
    
    def __init__(self):
        
        self.lex_dict = {
            'directions': ['north', 'south', 'east', 'west'],
            'verbs': ['go', 'kill', 'eat'],
            'stops': ['the', 'in', 'of'],
            'nouns': ['bear', 'princess'],
            'numbers': [range(0,)],
            }
        
        self.lex_dict_cats = self.lex_dict.keys()
    
    def scan(self, words):
        
        self.path = []
        splitwords = words.split()
        for i in splitwords:
            try:
                self.path.append(('numbers', int(i)))
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
