# Example of reading a file located
# in our local file system

NAME = 'mynotes.txt'

# Open the file

myfile = open(NAME, 'r')

print('File open: {}'.format(myfile.name))

contents = myfile.read()

print('The file contents are: {}'.format(contents))

#Close the file

myfile.close()