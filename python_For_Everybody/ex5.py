hrs= input("Enter the number of hours")
rate= input("Enter the rate per hour")
h= float(hrs)
r=float(rate)
def computepay(h,r):
    if h>40:
        gpay=40*r
        gpay=gpay+((h-40)*(1.5*r))
    else:
        gpay=h*r
    return gpay
pay= computepay(h,r)
print(pay)
