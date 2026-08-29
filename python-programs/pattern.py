def square(s):
    for i in range(s):
        print("* " * s)


def righttriangle(s):
    for i in range(1, s + 1):
        print("* " * i)


def lefttriangle(s):
    for i in range(1, s + 1):
        print("  " * (s - i) + "* " * i)


def inverttriangle(s):
    for i in range(s, 0, -1):
        print("* " * i)


def pyramid(s):
    for i in range(1, s + 1):
        print(" " * (s - i) * 2 + "* " * i)


def diamond(s):
    for i in range(1, s + 1):
        print(" " * (s - i) * 2 + "* " * (2 * i - 1))

    for i in range(s - 1, 0, -1):
        print(" " * (s - i) * 2 + "* " * (2 * i - 1))


def numberpattern(s):
    num = 1
    for i in range(1, s + 1):
        for j in range(i):
            print(num, end=" ")
            num += 1
        print()


def floydspattern(s):
    num = 1
    for i in range(1, s + 1):
        for j in range(i):
            print(num, end=" ")
            num += 1
        print()


def pascal(s):
    for i in range(s):
        print(" " * (s - i), end="")
        num = 1

        for j in range(i + 1):
            print(num, end=" ")
            num = num * (i - j) // (j + 1)

        print()


def xpattern(s):
    for i in range(s):
        for j in range(s):
            if j == i or j == s - i - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


def heart(s):
    for i in range(s // 2, s, 2):
        print(" " * (s - i), end="")
        print("* " * (i // 2), end="")
        print(" " * (s - i), end="")
        print("* " * (i // 2))

    for i in range(s, 0, -1):
        print(" " * (s - i), end="")
        print("* " * i)


def zigzag(s):
    for i in range(3):
        for j in range(s):
            if (i + j) % 4 == 0 or (i == 1 and j % 4 == 2):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


def spiral(s):
    matrix = [[" " for _ in range(s)] for _ in range(s)]

    top = 0
    bottom = s - 1
    left = 0
    right = s - 1
    ch = "*"

    while top <= bottom and left <= right:

        for i in range(left, right + 1):
            matrix[top][i] = ch
        top += 1

        for i in range(top, bottom + 1):
            matrix[i][right] = ch
        right -= 1

        if top <= bottom:
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = ch
            bottom -= 1

        if left <= right:
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = ch
            left += 1

    for row in matrix:
        print(" ".join(row))


def alphabetpyramid(s):
    for i in range(1, s + 1):
        print(" " * (s - i) * 2, end="")

        for j in range(i):
            print(chr(65 + j), end=" ")

        for j in range(i - 2, -1, -1):
            print(chr(65 + j), end=" ")

        print()


def alphabettriangle(s):
    for i in range(1, s + 1):
        for j in range(i):
            print(chr(65 + j), end=" ")
        print()


def alphabetsquare(s):
    for i in range(s):
        for j in range(s):
            print(chr(65 + j), end=" ")
        print()


def hollowdiamond(s):
    for i in range(1, s + 1):
        spaces = 2 * (s - i)

        if i == 1:
            print(" " * spaces + "*")
        else:
            print(" " * spaces + "*" + " " * (2 * i - 3) + "*")

    for i in range(s - 1, 0, -1):
        spaces = 2 * (s - i)

        if i == 1:
            print(" " * spaces + "*")
        else:
            print(" " * spaces + "*" + " " * (2 * i - 3) + "*")


def butterfly(s):
    for i in range(1, s + 1):
        print("* " * i + "  " * (2 * (s - i)) + "* " * i)

    for i in range(s, 0, -1):
        print("* " * i + "  " * (2 * (s - i)) + "* " * i)


def hourglass(s):
    for i in range(s, 0, -1):
        print(" " * (s - i) * 2 + "* " * (2 * i - 1))

    for i in range(2, s + 1):
        print(" " * (s - i) * 2 + "* " * (2 * i - 1))


def rightpascal(s):
    for i in range(1, s + 1):
        print("* " * i)

    for i in range(s - 1, 0, -1):
        print("* " * i)


def invertedpyramid(s):
    for i in range(s, 0, -1):
        print(" " * (s - i) * 2 + "* " * (2 * i - 1))


while True:

    print("""
==================================================
                PATTERN MENU
==================================================

1.  Square Pattern
2.  Right Triangle Pattern
3.  Left Angle Triangle Pattern
4.  Inverted Triangle Pattern
5.  Pyramid Pattern
6.  Diamond Pattern
7.  Number Pattern
8.  Floyd's Triangle Pattern
9.  Pascal's Triangle Pattern
10. X Pattern
11. Heart Pattern
12. Zig Zag Pattern
13. Spiral Pattern
14. Alphabet Pyramid Pattern
15. Alphabet Triangle Pattern
16. Alphabet Square Pattern
17. Hollow Diamond Pattern
18. Butterfly Pattern
19. Hourglass Pattern
20. Right Pascal Pattern
21. Inverted Pyramid
22. Exit

==================================================
""")

    choice = int(input("ENTER YOUR CHOICE: "))

    if choice == 22:
        print("PROGRAM EXITED.")
        break

    s = int(input("ENTER THE SIZE: "))

    if choice == 1:
        square(s)

    elif choice == 2:
        righttriangle(s)

    elif choice == 3:
        lefttriangle(s)

    elif choice == 4:
        inverttriangle(s)

    elif choice == 5:
        pyramid(s)

    elif choice == 6:
        diamond(s)

    elif choice == 7:
        numberpattern(s)

    elif choice == 8:
        floydspattern(s)

    elif choice == 9:
        pascal(s)

    elif choice == 10:
        xpattern(s)

    elif choice == 11:
        heart(s)

    elif choice == 12:
        zigzag(s)

    elif choice == 13:
        spiral(s)

    elif choice == 14:
        alphabetpyramid(s)

    elif choice == 15:
        alphabettriangle(s)

    elif choice == 16:
        alphabetsquare(s)

    elif choice == 17:
        hollowdiamond(s)

    elif choice == 18:
        butterfly(s)

    elif choice == 19:
        hourglass(s)

    elif choice == 20:
        rightpascal(s)

    elif choice == 21:
        invertedpyramid(s)

    else:
        print("INVALID OPTION.")

    print("\n" + "=" * 50)
