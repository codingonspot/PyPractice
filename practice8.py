import random


def rohanMulTable(n):
    wrong = random.randrange(0, 9)
    table = [i * n for i in range(1, 11)]
    table[wrong] = table[wrong] + random.randrange(0, 10)
    return table


def isCorrect(table, n):
    for i in range(1, 11):
        if table[i - 1] != i*n:
            return i - 1
    return None


if __name__ == '__main__':
    n = int(input("Enter a number: "))
    myTable = rohanMulTable(n)
    print(myTable)
    wrongIndex = isCorrect(myTable, n)
    print(f"The table is wrong at index {wrongIndex}")
