from nose.tools import *
from ex48.lexicon import lexicon

def test_directions():
    assert_equal(lexicon.scan("north"), [('directions', 'north')])
    result = lexicon.scan("north south east")
    assert_equal(result, [('directions', 'north'),
                          ('directions', 'south'),
                          ('directions', 'east')])

def test_verbs():
    assert_equal(lexicon.scan("go"), [('verbs', 'go')])
    result = lexicon.scan("go kill eat")
    assert_equal(result, [('verbs', 'go'),
                          ('verbs', 'kill'),
                          ('verbs', 'eat')])

def test_stops():
    assert_equal(lexicon.scan("the"), [('stops', 'the')])
    result = lexicon.scan("the in of")
    assert_equal(result, [('stops', 'the'),
                          ('stops', 'in'),
                          ('stops', 'of')])

def test_nouns():
    assert_equal(lexicon.scan("bear"), [('nouns', 'bear')])
    result = lexicon.scan("bear princess")
    assert_equal(result, [('nouns', 'bear'),
                          ('nouns', 'princess')])

def test_numbers():
    assert_equal(lexicon.scan("1234"), [('numbers', 1234)])
    result = lexicon.scan("3 91234")
    assert_equal(result, [('numbers', 3),
                          ('numbers', 91234)])
                          
def test_errors():
    assert_equal(lexicon.scan("ASDFADFASDF"), [('error', 'ASDFADFASDF')])
    result = lexicon.scan("bear IAS princess")
    assert_equal(result, [('nouns', 'bear'),
                          ('error', 'IAS'),
                          ('nouns', 'princess')])  
