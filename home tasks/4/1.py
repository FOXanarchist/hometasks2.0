def first():
    N = int(input())
    A = list(map(int, input().split(' ')))
    C = int(input())

    l = -99999999999999999999
    
    for x in range(N):
        for y in range(N):
            for z in range(N):
                for w in range(N):
                    if (x in [y,z,w] or y in [x,z,w] or z in [x,y,w] or w in [x,y,z]) == False:
                        temp = A[x]+A[y]+A[z]+A[w]
                        if (abs(temp - C)<abs(l)) or (abs(temp + C) < abs(l)):
                            l = min((abs(temp - C)<abs(l)), (abs(temp + C) < abs(l)))
                            K = [A[x],A[y],A[z],A[w]]
                            f = temp
    print(K, f, sep='\n')

if __name__ == '__main__':
    first()