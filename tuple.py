fname = input("Enter the file name to open")
fh = open("mbox-short.txt")
dst = dict()
hlst = []
for ln in fh:
    words = ln.split()
    if len(words)>2 and words[0]=='From':
        hr = words[5].split(':')
        dst[hr[0]] = dst.get(hr[0],0)+1
    else :
        continue
for k,v in dst.items():
    hlst.append((k,v))
hlst.sort()
for k,v in hlst:
    print(k,v)
