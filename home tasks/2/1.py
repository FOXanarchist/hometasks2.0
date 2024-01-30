s = input('Input your string: ')
A = []
c = 0
m = 0
for i in s:
    if (i in A )== False:
        A.append(i)
        c+=1
        if m < c: m =c
    else:
        c = 0
        A = []

print(m)