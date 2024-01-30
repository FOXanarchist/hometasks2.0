s = input()
s = s.lower()
A = list(map(str, s.split(' ')))
A.reverse()
s = ''
for i in A:
    s+=i+' '
s =s[0].upper()+ s[1:-1]
print(s)