from sys import argv
#importing argv from sys module
script, input_file = argv

# creating a print function that will print everything in f (file)
def print_all(f):
    print f.read()
    
# 'rewinds' or 'seeks' back the start of the file in bytes    
def rewind(f):
    f.seek(0)
    
# prints a line from the file, depending on the line number    
def print_a_line(line_count, f):
    print line_count, f.readline()
    
# creates a variable to open the input file    
current_file = open(input_file)


print "First let's print the whole file:\n"

# uses the current_file variable as input for the print_all function
print_all(current_file)

print "\nNow let's rewind, kind of like a tape.\n"

# uses the current_file variable as input for the rewind function
rewind(current_file)

print "Let's print three lines:\n"

# prints out first three lines of the input file using the print_a_line function. cycles through lines by using 'while' command (from lines 1-3 --> 3 lines)
current_line = 0
while current_line <= 2:
    current_line += 1
    print_a_line(current_line, current_file)
  
# closes input file        
current_file.close()
    

