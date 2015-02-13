# example module - count and return number of times key words are mentioned in a scientific article (pdf version)

import operator
from sys import argv

script, doc = argv
o_doc = open(doc, 'r+')
x = o_doc.read()
print x
o_doc.close()
