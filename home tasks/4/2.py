def second(A):
    R = [[]]

    for i in A:
        B = []
        for p in R:
            for j in range(len(p) + 1):
                B.append(p[:j] + [i] + p[j:])
        R = B

    print(R[::-1])


if __name__ == '__main__':
    second()