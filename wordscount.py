count = dict()
line = input("Enter  the line in console....\n")
words = line.split()
print('Words in the line are',words)
print('counting the numbers off the words.......\n')
for word in words :
    count[word] = count.get(word,0)+1
print('The  number of ghe counts of words in the  line are,,,,,\n',count)
