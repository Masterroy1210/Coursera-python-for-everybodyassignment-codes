fname = input('Enter the file name')
try :
    fh = open(fname)
except :
    print('Enter the correct file name.....')
for line in fh :
    line = line.rstrip()
    line = line.upper()
    print(line)
