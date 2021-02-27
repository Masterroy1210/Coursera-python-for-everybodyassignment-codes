fname = input("Enter the file name")
avg = 0
count = 0
nm = 0
fh = open(fname)
for ln in fh:
    if not ln.startswith("X-DSPAM-Confidence:"):
        continue
    count = count+1
    cpos = ln.find(":")
    no = ln[cpos+1 : 50]
    no = no.lstrip()
    nm += float(no)

avg = nm/count
print('Average spam confidence:',avg)
