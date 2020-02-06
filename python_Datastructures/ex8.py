fname = input('Enter the File name:')
fh = open(fname)
count=0
sum=0
for line in fh:
    if not 'X-DSPAM-Confidence:' in line:
        continue
    count=count+1
    first= line.find('0')
    num= line[first:first+6]
    sum=sum+float(num)
print('Average spam confidence: ', sum/count)
