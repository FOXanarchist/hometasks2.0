import time

def take_info(): 
    with open('input.txt','r',encoding='utf-8') as file:
        N,L,K = map(int, file.readline().split(' '))
        FIGURES = []
        for _ in range(K):
            FIGURES.append(tuple(map(int, file.readline().split(' '))))
        return N,L,K,FIGURES
def chess(x:int,y:int,N:int, DANGER_LIST:list):
    MOVES = [
        (x+1,y),(x+2,y),(x+3,y),#right
        (x-1,y),(x-2,y),(x-3,y),#left
        (x,y+1),(x,y+2),(x,y+3),#up
        (x,y-1),(x,y-2),(x,y-3),#down

        (x+1,y+1),(x+2,y+2),(x+3,y+3),#up right
        (x-1,y-1),(x-2,y-2),(x-3,y-3),#down left
        (x+1,y-1),(x+2,y-2),(x+3,y-3),#right down
        (x-1,y+1),(x-2,y+2),(x-3,y+3),#up left
    ]
    A = list()
    for i in range(len(MOVES)):
        
        if (MOVES[i][0] in range(0,N)) and (MOVES[i][1] in range(0,N)) and (not (MOVES[i] in DANGER_LIST)):
            ...
        else:
            A.append(i)
    с = 0
    for i in A:
        del MOVES[i-с]
        с+=1

    return MOVES
def field(N:int):
    FIELD = [0]*N
    for i in range(len(FIELD)):
        FIELD[i]=[0]*N
    return FIELD
def arrangemetn(position:tuple, N:int, FIELD:list, ANSWER:list, DANGER_LIST:list, flag:bool = False,rule:bool=False):
    # print(*FIELD,sep='\n',end='\n'*2)
    f = False
    condition1 = FIELD[position[0]][position[1]] == '#'
    condition2 = FIELD[position[0]][position[1]] == '*'
    if ((condition1 or condition2) == False) or rule:
        FIELD[position[0]][position[1]] = '#'
        DANGER_LIST.append(position)
        if flag:
            ANSWER.append(position)
        mooves = chess(position[0],position[1],N,DANGER_LIST)
        for i in mooves:
            if FIELD[i[0]][i[1]] == 0:
                FIELD[i[0]][i[1]] = '*'
                DANGER_LIST.append(i)
        f = True
    return FIELD,ANSWER,DANGER_LIST,f
def outpute(counter:int, L:int, ANSWER:list, rule:bool = False):
    if rule:
        with open('outpute.txt','w',encoding='utf-8') as file:
            for i in range(len(ANSWER)):
                
                ANSWER[i] = f'{ANSWER[i]} '

            if counter == L:
                file.writelines(ANSWER)
                file.write('\n')
            else:
                file.write('no solution')
    else:
        with open('outpute.txt','a',encoding='utf-8') as file:
            for i in range(len(ANSWER)):
                
                ANSWER[i] = f'{ANSWER[i]} '

            if counter == L:
                file.writelines(ANSWER)
                file.write('\n')
            
def main():
    start = time.time()

    N,L,K,FIGURES = take_info()
    # print(FIGURES)
    TEMP = []
    FIELD = field(N)
    DANGER_LIST = []
    for i in FIGURES:
        # print('First step:',i)
        FIELD,TEMP,DANGER_LIST,FLAG = arrangemetn(i,N,FIELD,[],DANGER_LIST,True,True)
        # print(*FIELD,sep='\n')
    ANSWER = []
    counter = 0
    t = 0
    for i in range(L):
        m = False
        for x in range(N):
            for y in range(N):
                pos = (x,y)
                if pos in ANSWER == False:
                    FIELD,ANSWER,DANGER_LIST,FLAG = arrangemetn(pos,N,FIELD,ANSWER,DANGER_LIST,True)
                    # print('Second step:',pos,FLAG)
                    if FLAG:
                        counter+=1
                        m = True
                        break
                    
    outpute(counter,L,ANSWER,True)

    print(*FIELD,sep='\n')
    # outpute(counter,L,ANSWER)
    finish = time.time()
    return finish-start
if __name__ == '__main__':
    print(main())
