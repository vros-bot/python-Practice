fh = open("romeo.txt")
lst= list()
for line in fh:
    line.rstrip()
    l= line.split()
    for i in l:
        if i not in lst:
            lst.append(i)
lst.sort()
print(lst)
