name = input("Enter file:")
if len(name) < 1 :
    name = "mbox-short.txt"

handle = open(name)
d1=dict()
l1=[]
temp=""
count=1
for line in handle:
    w=line.rstrip()
    if line.startswith('From '):
        pos=w.find(':')
        temp = str(w[pos-2:pos])
        l1.append(""+temp)
tup=tuple(l1)
for i in tup:
    if not i in d1:
        d1[i]=count
    else:
        d1[i]=d1[i]+1

for i in sorted(d1):
    print(i,d1[i])
