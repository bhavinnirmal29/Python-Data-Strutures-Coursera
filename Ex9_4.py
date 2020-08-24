name = input("Enter file:")
if len(name) < 1 :
    name = "mbox-short.txt"
    
handle = open(name)
d1=dict()
l1=list()
tmp=list()
for line in handle:
    if line.startswith('From '):
        tmp=line.split()
        l1.append(tmp[1])
count=1
for i in l1:
    if not i in d1:
        d1[i]=count
    else:
        d1[i]=d1[i]+1
l1=[]
temp=""
max1=0
for k,v in d1.items():
    if v > max1:
        max1=v
        temp = k

print(temp,max1)
        
