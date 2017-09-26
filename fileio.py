# this line grabs the file from its location and opens it in a READ(r) MODE
# Inorder to avoid misconception by Python, we can put double slashes which tells
# python that it is not to be taken as a command
# You'll need to use forward slashes in MAC or LINUX and in WINDOWS you'll need to use Backward slashes
# grabber = open("C:\\UdemyPython\\sample.txt", 'r')

grabber = open("sample.txt", 'r')

for line in grabber:
    # This will print out only those lines which have jabberwock in them
    if "jabberwock" in line.lower():
        # Help in ending the line before it continues to print the whole paragraph
        print(line, end=' ')

# Every time after opening a file we should close it too
grabber.close()

# Here the WITH command takes care of everything including the opening and closing of the files,
# so here we don't need to specify .CLOSE command separately
with open("sample.txt", 'r') as grabber:
    for line in grabber:
        if "JAB" in line.upper():
            print(line, end='')

# Reading lines and printing them as they're
with open("sample.txt", 'r') as grabber:
# READLINE reads a single line from the file and returns it 
    line = grabber.readline()
    while line:
        print(line, end='') # Avoids printing of extra spaces and lines
        line = grabber.readline()

with open("sample.txt", 'r') as grabber:
    # Grabs/reads the entire file in one go and prints them out in the form of a list
    lines = grabber.readlines()
print(lines)

# Iterating over the list and printing out each line separately
for line in lines:
    print(line, end='')

with open("sample.txt", 'r') as grabber:
    lines = grabber.readlines()
print(lines)

# Reversed lines
for line in lines[::-1]:
    print(line, end='')

with open("sample.txt", 'r') as grabber:
    lines = grabber.read()

# it is reading and printing the reversed lines
for line in lines[::-1]:
    print(line, end='')















