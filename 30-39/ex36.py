# generate a poem

# open's our three files
x = open("ex36f1.txt")
y = open("ex36f2.txt")
z = open("ex36f3.txt")

# puts opened files into a list
tt = [x, y, z]

# loops over each file
def looping(file_list):
    for file_choice in file_list:
        poem_creator(file_choice)

# creates top function
def poem_creator(filename):

    # counts the number of lines in a file
    def file_len(filename):
        title_count = 0
        for line in x:
            title_count += 1
        return title_count

    # picks out a line from the file, splits it, picks a word, adds it to title_list
    from random import randint
    def title_list_creation(filename):
        lx = x.readline(randint(0, file_len(filename)))
        title_list = []
        title_list.append(lx)
        return title_list
        # adds lines to a title string, creates poem
        title = " "
        for i in title_list:
            title += str(i) + '\n'
        return title

# closes files
x.close()
y.close()
z.close()

print looping(tt)
