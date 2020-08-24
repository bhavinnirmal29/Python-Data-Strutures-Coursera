# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
total=0
count=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    
    pos=line.find(':')
    count=count+1
    val=float(line[pos+2:])
    total=total+val
print("Average spam confidence:",total/count)