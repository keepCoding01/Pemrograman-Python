import numpy as np

num = input("Tekan Tombol : ").split()

alpha = [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"], ["j", "k", "l"], [
    "m", "n", "o"], ["p", "q", "r", "s"], ["t", "u", "v"], ["w", "x", "y", "z"]]

for hasil in num:
    if int(hasil) == 1:
        print()
    if hasil == "*":
        print()
    if hasil == "#":
        print()
    if int(hasil) == 0:
        print(" ", end="")

    if int(hasil) == 2:
        print(alpha[0][0], end="")
    if int(hasil) == 22:
        print(alpha[0][1], end="")
    if int(hasil) == 222:
        print(alpha[0][2], end="")

    if int(hasil) == 3:
        print(alpha[1][0], end="")
    if int(hasil) == 33:
        print(alpha[1][1], end="")
    if int(hasil) == 333:
        print(alpha[1][2], end="")

    if int(hasil) == 4:
        print(alpha[2][0], end="")
    if int(hasil) == 44:
        print(alpha[2][1], end="")
    if int(hasil) == 444:
        print(alpha[2][2], end="")

    if int(hasil) == 5:
        print(alpha[3][0], end="")
    if int(hasil) == 55:
        print(alpha[3][1], end="")
    if int(hasil) == 555:
        print(alpha[3][2], end="")

    if int(hasil) == 6:
        print(alpha[4][0], end="")
    if int(hasil) == 66:
        print(alpha[4][1], end="")
    if int(hasil) == 666:
        print(alpha[4][2], end="")

    if int(hasil) == 7:
        print(alpha[5][0], end="")
    if int(hasil) == 77:
        print(alpha[5][1], end="")
    if int(hasil) == 777:
        print(alpha[5][2], end="")
    if int(hasil) == 7777:
        print(alpha[5][3], end="")

    if int(hasil) == 8:
        print(alpha[6][0], end="")
    if int(hasil) == 88:
        print(alpha[6][1], end="")
    if int(hasil) == 888:
        print(alpha[6][2], end="")

    if int(hasil) == 9:
        print(alpha[7][0], end="")
    if int(hasil) == 99:
        print(alpha[7][1], end="")
    if int(hasil) == 999:
        print(alpha[7][2], end="")
    if int(hasil) == 9999:
        print(alpha[7][3], end="")
