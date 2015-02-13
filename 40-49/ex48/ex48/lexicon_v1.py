class lexicon(object):
    

    def __init__(self):
        pass

    def scan(self, questions):
        
        lexicon = {
            'directions': ['north', 'south', 'east', 'west'],
            'verbs': ['go', 'kill', 'eat'],
            'stops': ['the', 'in', 'of'],
            'nouns': ['bear', 'princess'],
            'numbers': [range(0,)],
            }        
        
        words = questions.split()
        for thing in words:
            for key, value in lexicon.iteritems():        
                for y in value:
                    if thing == y:
                        produce = (key, y)
                        print produce
                    else:
                        pass

    def sentence_(lists_of_words):
        sentence = ' '.join(lists_of_words)
        print sentence                    
    
example = lexicon()
example.scan(raw_input(''))    
