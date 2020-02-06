fname = input("Enter the name of the fil:")
fh= open(fname)

names_list= list()
counts= dict()
for line in fh:
    line.rstrip();
    if not line.startswith('From '):
        continue;
    words=line.split();
    names= words[1]
    names_list.append(names)

for name in names_list:
    counts[name]=counts.get(name,0)+1

bigname= None
bigcount= None
for word,count in counts.items():
    if bigcount is None or count>bigcount:
        bigname=word
        bigcount=count

print(bigname, bigcount)
