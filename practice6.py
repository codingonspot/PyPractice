import random


def guessGame(a, b, n):
    t = int(input(f"Guess a number b/w {a} & {b}\n"))
    count = 1
    while t != n:
        if t < n:
            t = int(input("Enter a bigger number: "))
            count += 1
        else:
            t = int(input("Enter a smaller number: "))
            count += 1
    print(f"You guessed the number in {count} attempts.")
    return count


if __name__ == '__main__':
    a = int(input("Lower limit: "))
    b = int(input("Upper limit: "))
    n1 = random.randrange(a, b)
    n2 = random.randrange(a, b)
    print("P1 turn")
    g1 = guessGame(a, b, n1)
    print("P2 turn")
    g2 = guessGame(a, b, n2)

    if g1 < g2:
        print("P1 wins !")
    else:
        print("P2 wins !")
