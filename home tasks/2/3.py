s = input()
a = ''

A = []
U ={
    ')':'(',
    '}':'{',
    ']':'['
}
m = 0
c = 0
f=-1
for i in s:
    if i in '({[':
        a += i
        c+=1
        if m < c: m = c
    elif i in ')}]' and a != '' and U[i] == a[-1]:
        a = a[:-1]
        c+=1
        if m < c: m = c
    else:
        f +=1
        A.append(a)
        a = ''
        c = 0
if f == -1:
    print(True)
else:print(A[f])