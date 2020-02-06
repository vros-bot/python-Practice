max= None
min= None
while True:
    line = raw_input("Enter a line:")
    if line == "done":
        line = str(line)
        break
    try:
        num= int(line)
    except:
        print('Invalid Input')
        continue
    if max is None:
        max=line
        min=line
    if line>max:
        line=max
    if line<min:
        line=min
print("Maximum is", max)
print("Minimum is", min)
