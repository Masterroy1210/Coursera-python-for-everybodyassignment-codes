small = None
large = 0
while True :
    try :
        no = input('enter the no')
        if no == "done" :
            break
        no = int(no)
        if small is None :
            small = no
        if large<no :
            large = no
        if small>no :
            small = no

    except :
        print('Invalid input')
        continue
print("Maximum is",large)
print("Minimum is",small)
