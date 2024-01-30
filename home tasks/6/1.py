def first():
    A = list(map(str, input().split(' ')))
    B = list(map(str, input().split(' ')))
    
    c_r = 0
    c_nr = 0
    for i in A:
        if i in B:
            c_r +=1
        else:
            c_nr+=1
    ka = len(A)-c_nr
    temp = c_nr
    for i in B:
        if i in A == False:
            c_nr +=1
    kb = len(A) - c_nr + temp

    print(c_r, c_nr, ka, kb)

if __name__ == '__main__':
    first()