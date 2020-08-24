fname = input("Enter file name: ")
fh = open(fname)
lst = list()
new_list = list()
for line in fh:
    lst=line.split()
    for i in lst:
        if not i in new_list:
            new_list.append(i)
new_list.sort()
print(new_list)