def second():
    A = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    B = [[]]
    for i in range(len(A)):
        for j in range(len(A[i])):
            B[i].append(A[j][i])
        B[i].reverse()
        B.append([])
    del B[-1]
    print(*B, sep='\n')

if __name__ == '__main__':
    second()