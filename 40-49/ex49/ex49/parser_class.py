from lexicon import lexicon

class ParserError(Exception):
    pass
    
class Sentence(object):
    
    def __init__(self, word_list):
        self.word_list = word_list
        
    def peek(self, word_list):
        if word_list:
            word = word_list[0]
            return word[0]
        else:
            return None
            
    def match(self, word_list, expecting):
        if word_list:
            word = word_list.pop(0)
            
            if word[0] == expecting:
                return word
            else:
                return None
        else:
            return None
            
    def skip(self, word_list, word_type):
        while self.peek(word_list) == word_type:
            self.match(word_list, word_type)
            
    def parse_verb(self, word_list):
        # take out all stop words in list
        self.skip(word_list, 'stop')
        
        if self.peek(word_list) == 'verb':
            # return's 'popped' verb tuples
            return self.match(word_list, 'verb')
        else:
            raise ParserError("Expected a verb next")
            
    def parse_object(self, word_list):
        self.skip(word_list, 'stop')
        self.next_word = self.peek(word_list)
        
        if self.next_word == 'noun':
            return match(word_list, 'noun')
        elif self.next_word == 'direction':
            return self.match(word_list, 'direction')
        else:
            raise ParserError("Expected a noun or direction next.")

    def self.parse_subject(self, word_list):
        self.skip(word_list, 'stop')
        self.start_word = peek(word_list)
        
        if self.start_word == 'noun':
            return self.match(word_list, 'noun')
        elif self.start_word == 'verb':
            return ('noun', 'player')
        else:
            raise ParserError("Expected a verb next.")
            
    def parse_sentence(self, word_list):
        subj = parse_subject(word_list)
        self.verb = parse_verb(self, word_list)
        self.obj = parse_object(self, word_list)
        
        return self.subj[1], self.verb[1], self.obj[1]
        
parser = Sentence()
