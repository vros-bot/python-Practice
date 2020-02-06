hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter rate:")
r= float(rate)
if (hrs>40):
    gpay= 40* r
    gpay= gpay + ((h-40)*(1.5*r))
else:
    gpay=h*r
print(gpay)
