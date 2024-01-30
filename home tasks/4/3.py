def third():
    A = list(map(str, input().split(' ')))
    C = []
    while A != []:
        
        a = A[0]
        l = len(a)
        ch = set(a)
        B = [a]
        A = A[1:]
        for i in A:
            if (set(i) == ch)  and len(i) == l:
                B.append(i)
                print(B)
                del A[A.index(i)]
                
        C.append(B)
    print(C)

if __name__ == '__main__':
    third()