n = int(input("masukkan angka : "))

for i in range(1, n, 1):
    print(" "*(n-i), end='')
    for x in range(i):
        print("+ ", end='')
    print()

for i in range(n, 0, -1):
    print(" "*(n-i), end='')
    for x in range(i):
        print("+ ", end='')
    print()

print("\n")

for i in range(1, n):
    print("*"*i)

for i in range(n, 0, -1):
    print("*" * i)

print("\n")

for i in range(1, n, 1):
    print(" "*(n-i) + "*"*i)

for i in range(n, 0, -1):
    print(" "*(n-i) + "*"*i)
