from sys import argv
from os.path import exists

scripts, from_file, to_file = argv

in_file = open(from_file).read()

out_file = open(to_file, 'w').write(in_file)
