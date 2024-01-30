def ch(b):
        k = 0

        while b > 0:
            b = b // 10
            k += 1
        return k

a = int(input())
pol = 0
n_a = a
pr = a

if a >= 0:
    while n_a > 0:
        n = n_a % 10
        pol += 10 ** (ch(n_a) - 1) * n
        n_a = (n_a // 10)

else:
    pr = a * (-1)
    n_a = a * (-1)
    while n_a > 0:
        n = n_a % 10
        pol += 10 ** (ch(n_a) - 1) * n
        n_a = (n_a // 10)
    pol = pol * (-1)

if -128 <= pol <= 128:
    print(pol)

else:
    print('no solution')
