fname = input('Enter the file  name to open')
fh = open(fname)
lst1 = list()
data = dict()
for ln in fh :
    if ln.startswith("From"):
        if ln.startswith('From:'):
            continue
        else :
            word = ln.split()
            lst1.append(word[1])
for word in lst1:
    data[word] = data.get(word,0)+1
bigcount = None
bigword = None
for word,count in data.items():
    if bigcount is None or bigcount<count:
        bigcount = count
        bigword = word
print(bigword,bigcount)
