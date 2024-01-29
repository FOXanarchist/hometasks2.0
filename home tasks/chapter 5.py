def main():
    c = int(input("количество банков:"))
    banks = []
    for i in range(c):
        name = input("название:")
        money = int(input("сумма:"))
        banks.append((name, money))
    m_money = [0] * c
    A = [0] * c
    for i in range(c):
        if i == 0:
            m_money[i] = banks[i][1]
        elif i == 1:
            m_money[i] = max(banks[i][1], banks[i-1][1])
            if m_money[i] == banks[i][1]:
                A[i] = i
            else:
                A[i] = i-1
        else:
            include = banks[i][1] + m_money[i-2]
            exclude = m_money[i-1]
            if include > exclude:
                m_money[i] = include
                A[i] = i
            else:
                m_money[i] = exclude
                A[i] = A[i-1]
    print("Максимальная сумма:", m_money[-1], "млн рублей")

    return

if __name__ == "__main__":
    main()