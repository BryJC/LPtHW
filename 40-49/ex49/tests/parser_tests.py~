from nose.tools import *
from ex49.parser import *

word_list1 = [('stop','the'),('noun','bear'),('verb','eats'),('noun','honey')]
word_list2 = [('stop','the'),('verb','eats'),('noun','honey')]
word_list3 = [('stop','the'),('noun','bear'),('verb','eats'),('noun','honey')]
word_list4 = [('stop','the'), ('direction','north'), ('noun','wind')]

class TestParserError(object):

    def __init__(self, test_name, word_list):
        self.test_name = test_name
        self.word_list = word_list
        return assert_raises(ParserError, test_name, word_list)

def test_peek():
    assert_equal(peek(word_list1), 'stop')

def test_match():
    assert_equal(match(word_list1, 'stop'), ('stop', 'the'))

def test_skip():
    assert_equal(skip(word_list1, 'stop'), None)

def test_parse_verb():
    assert_equal(parse_verb(word_list2), ('verb', 'eats'))
    x = TestParserError(parse_verb, word_list2)

def test_parse_object():
    assert_equal(parse_object(word_list2), ('noun', 'honey'))
    x = TestParserError(parse_verb, word_list4)
                          
def test_parse_subject():
    assert_equal(parse_subject(word_list1), ('noun', 'bear'))
    x = TestParserError(parse_verb, word_list4)

def test_parse_sentence():
    x = parse_sentence(word_list3)
    assert_equal(x.subject, 'bear') 
    assert_equal(x.verb, 'eats')
    assert_equal(x.object, 'honey')

#need to write exception tests still


                         
