# generate a poem
""" Create a version that takes any three text files later using argv, imported from sys... also find out what the os module is """
# open's our three files


x = open("ex36f1.txt").read()
y = open("ex36f2.txt").read()
z = open("ex36f3.txt").read()

# puts opened files into a list
tt = [x, y, z]


# loops over each file
def looping(f_list):
    qq = ''
    for var in f_list:
        r_x = poem_creator(str(var))
        qq += '\n' + r_x
    return qq
        

# creates top function
def poem_creator(filename):

    # counts the number of lines in a file
    def file_len(filename):
        title_count = 0
        slf = filename.split('.')
        for line in slf:
            title_count += 1
        return title_count

    # print file_len(x)
    # file_len WORKS    

    from random import randint
    def title_list_creation(filename):
        slf = filename.split('.')
        i = randint(0, file_len(filename))
        rlf = slf[i]
        return rlf
        
    return title_list_creation(filename)
    
    # print title_list_creation(x)
    # title_list_creation WORKS

# print poem_creator(x)
# poem_creator WORKS


print looping(tt)
