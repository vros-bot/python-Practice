fname = input("Enter a file name:")
fh = open(fname)
count=0
for line in fh:
    line.rstrip()
    if not line.startswith('From '):
        continue
    Words = line.split()
    print(Words[1])
    count=count+1
print("There were", count, "lines in the file with From as the first word")
