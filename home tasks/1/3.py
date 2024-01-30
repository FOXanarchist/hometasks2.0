s = input()
A1 = ''
A2 = ''
A3 = ''

i = 1
while s != '':
    if i == 1:
        A1+=s[0]
    elif i == 2:
        A2+=s[0]
    elif i == 3:
        A3+=s[0]
    elif i == 4:
        A2+=s[0]
        i = 0
    i+=1
    s = s[1:]
print(A1+A2+A3)