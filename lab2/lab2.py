import time

#Получаем данные из "input.txt" и строим "начальную" доску



def display_solutions(solutions: list, startTime) -> None:
    print("Всего решений:", len(solutions))

    with open("output.txt", "w") as output_file:
        if not solutions:
            output_file.write("no solutions")
        else:
            for solution in solutions:
                output_file.write(" ".join(map(str, solution)) + "\n")

    endTime = time.time()
    print("Программа выполнилась за:", endTime - startTime)

#ограничиваем и добавляем элементы в нашу доску
def make_move(board, N: int, row: int, col: int, solutions: list) -> None:
    solutions.append((row, col))
    board[row] = board[row][:col] + "#" + board[row][col+1:]

    moves = [
        (row, col - 1), (row, col - 2),(row, col - 3), (row, col - 4),  # Влево
        (row, col + 1), (row, col + 2),(row, col + 3), (row, col + 4),  # Вправо
        (row - 1, col), (row - 2, col),(row - 3, col), (row - 4, col),  # Вверх
        (row + 1, col), (row + 2, col),(row + 3, col), (row + 4, col),  # Вниз
        (row-1, col - 1), (row-1, col - 2),(row-1, col - 3), (row-1, col - 4),
        (row-2, col - 1), (row-2, col - 2),(row-2, col - 3), (row-2, col - 4),
        (row-3, col - 1), (row-3, col - 2),(row-3, col - 3), (row-3, col - 4),
        (row-4, col - 1), (row-4, col - 2),(row-4, col - 3), (row-4, col - 4),
        (row+1, col - 1), (row+1, col - 2),(row+1, col - 3), (row+1, col - 4),
        (row+2, col - 1), (row+2, col - 2),(row+2, col - 3), (row+2, col - 4),
        (row+3, col - 1), (row+3, col - 2),(row+3, col - 3), (row+3, col - 4),
        (row+4, col - 1), (row+4, col - 2),(row+4, col - 3), (row+4, col - 4),
        
        (row-1, col + 1), (row-1, col + 2),(row-1, col + 3), (row-1, col + 4),
        (row-2, col + 1), (row-2, col + 2),(row-2, col + 3), (row-2, col + 4),
        (row-3, col + 1), (row-3, col + 2),(row-3, col + 3), (row-3, col + 4),
        (row-4, col + 1), (row-4, col + 2),(row-4, col + 3), (row-4, col + 4),
        (row+1, col + 1), (row+1, col + 2),(row+1, col + 3), (row+1, col + 4),
        (row+2, col + 1), (row+2, col + 2),(row+2, col + 3), (row+2, col + 4),
        (row+3, col + 1), (row+3, col + 2),(row+3, col + 3), (row+3, col + 4),
        (row+4, col + 1), (row+4, col + 2),(row+4, col + 3), (row+4, col + 4),
        
        
    ]

    for row_index, col_index in moves:
        if 0 <= row_index < N and 0 <= col_index < N and board[row_index][col_index] != "#":
            board[row_index] = board[row_index][:col_index] + "*" + board[row_index][col_index+1:]

def solve(L: int, N: int, board: list, solutions: list, allSolutions: list, startTime: list):
    find_solution(L, N, board, 0, -1, solutions, allSolutions)

    display_solutions(allSolutions, startTime)
#ищем ходы
def find_solution(L: int, N: int, board: list, row: int, col: int, solutions: list, allSolutions: list) -> None:
    while True:
        col += 1

        if col >= N:
            col = 0
            row += 1

        if row >= N:
            break

        if board[row][col] != "0":
            continue

        now_board = list(board)
        now_solutions = list(solutions)

        make_move(now_board, N, row, col, now_solutions)

        if L - 1 == 0:
            allSolutions.append(now_solutions)
            if len(allSolutions) == 1:
                for i_row in now_board:
                    print(i_row)
            continue

        find_solution(L - 1, N, now_board, row, col, now_solutions, allSolutions)
#инициализируем данные
def init_data():
    startTime = time.time()

    solutions = []
    allSolutions = []

    with open("input.txt", "r") as input_file:
        N, L, K = map(int, input_file.readline().split())

        board = ["0" * N for _ in range(N)]

        for _ in range(K):
            row, col = map(int, input_file.readline().split())
            make_move(board, N, row, col, solutions)


    return startTime, board, solutions, allSolutions, N, L, K


def main():
    startTime, board, solutions, allSolutions, N, L, K = init_data()

    print("Размер доски:", N, "Фигур стоит:", K, "Нужно разместить фигур:", L)

    if L == 0:
        if not (len(solutions) == 0):
            allSolutions.append(solutions)
        for i_row in board:
            print(i_row)
        display_solutions(allSolutions, startTime)
        return

    solve(L, N, board, solutions, allSolutions, startTime)



if __name__ == "__main__":
    main()
