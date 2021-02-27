hour = input('Enter the hour')
rate = input('enter the rate')
hour = float(hour)
rate = float(rate)
def computepay() :
    if hour<=40 :
        gpay = hour*rate
        return gpay
    else :
        hr = hour-40
        exp = hr*(rate/2)
        gpay = hour*rate+exp
        return gpay
pay = computepay()
print('Pay',pay)
