text = "X-DSPAM-Confidence:    0.8475";
cpos = text.find(':')
str = text[cpos+1 : 30]
str = str.lstrip()
str = float(str)
print(str)
