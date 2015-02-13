# example module - count and return number of times key words are mentioned in a scientific article (pdf version)

import operator
from sys import argv

script, rd_doc = argv
o_doc = open(rd_doc, 'r+')
doc = o_doc.read()
print '\n' + doc


class Engine(object):

    # runs the program    
    def __init__(self, doc):
        self.doc = doc
        
        s_r = Search_Report()
        a = s_r.prompt()
        b = s_r.splitting(doc)
        c = s_r.find(a, b)
        d = s_r.applied(c)

class Search_Report(object):

    # opens the dialog prompt and returns the submitted words    
    def prompt(self):
        ask = raw_input("What words would you like counted?\n")
        ask = ask.lower()
        prompt_words = ask.split()
        return prompt_words

    # turns doc single string into multiple words
    def splitting(self, doc):
        doc_line = doc.translate(None, "`~!@#$%^&*()_-+=[]\\{}|;'.,/:\"<>?")
        doc_line = doc_line.lower()
        doc_words = doc_line.split()
        return doc_words
        
    # finds the submitted words in the document        
    def find(self, prompt_words, doc_words):
        word_dict = {}
        for word in prompt_words:
            count = 0
            for i in doc_words:
                if i == word:
                    count += 1
                elif word != word:
                    pass
                else:
                    pass
            word_dict[word] = count
        return word_dict
    
    # prints the total number of instances of each word to one table with 'word = number' format
    def applied(self, word_dict):
        sorted_word_list = sorted(word_dict.items(), key=operator.itemgetter(1), reverse=True)
        final_list = '\n'.join("%s=%d" % tup for tup in sorted_word_list)
        print '\n'
        print final_list
        print '\n'
        
o_doc.close()

some_search = Engine(doc)
