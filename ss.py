import re

fname = input('enter the file name')
hand = open(fname)
x=list()
for line in hand:
     y = re.findall('[0-9]+',line)
     x = x+y
sum=0
for z in x:
    sum = sum + int(z)
print(sum)
