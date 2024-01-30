def second():
    A = list(map(str, input().split(' ')))
    n = len(A)
    us = set()

    for i in range(1,2**n):
        x = [A[j] for j in range(n) if (i & (1 << j)) > 0]
        if len(x) == len(set(x)):
            us.add(tuple(sorted(x)))

    print('Подмножества:',list(map(set, us)),'Количество подмножеств: ',len(us),sep = '\n')

if __name__ == '__main__':
    second()