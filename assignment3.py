hour = input("Enter the no of hours")
rate = input('Enter the rate  f hour')
hour = float(hour)
rate = float(rate)

if hour<=40 :
    gpay =  hour*rate
else :
    hr = hour-40
    exr = 5*(rate*1.5)
    gpay = 40*rate+exr
print(gpay)
