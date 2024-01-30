def santa_users(A):
    U = {}
    for i in A:
        try:
            U[i[0]] = i[1]
        except IndexError:
            U[i[0]] = None
    return U

if __name__ == '__main__':
    santa_users([['abc',123],['dfg']])
    