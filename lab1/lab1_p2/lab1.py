def req(st:str, S:int, t:int):
    # перебор знаков
    if st.count(' ')!=0:
        s1 = t + int(list(map(str, st.split(' ')))[1])
        req(st.replace(' ','+',1),S, s1)

        s1 = t - int(list(map(str, st.split(' ')))[1])
        req(st.replace(' ','-',1),S, s1)

    # сравнение полученного значения с исходным
    elif t == S:
        # запись результата
        with open('outpute.txt', 'w') as file:
            file.write(st+'='+str(S))
            exit()
    else:
        with open('outpute.txt', 'w') as file:
            file.write(st+'='+str(S))
def main():
    
    # reading file
    with open('input.txt') as file:
        st = file.readline()
        A = list(map(str, st.split(' ')))
        n = int(A[0])
        S = int(A[-1])
        s = ' '.join(A[1:-1])
        print(s,S,int(A[1]))
    # поиск решений
    req(s, S, int(A[1]))

if __name__ == "__main__":
    main()