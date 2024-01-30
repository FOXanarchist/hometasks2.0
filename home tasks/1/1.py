def ch(b):
        k = 0

        while b > 0:
            b = b // 10
            k += 1
        return k

n = int(input())
pol = 0
a = n
b = n

while a > 0:
    x = a % 10
    pol += 10 ** (ch(a) - 1) * x
    a = (a // 10)
    print(pol, a)

if pol == a:
    print(True)
else:
    print(False)