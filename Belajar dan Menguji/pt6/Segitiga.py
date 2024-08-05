n = int(input("Masukkan angka :"))

# nomor 1
s = 2*n-2
for i in range(0, n):
    for j in range(0, s):
        print(" ", end="")
    s -= 2
    for j in range(0, i+1):
        print("* ", end="")
    print("")


print("---------------------------------------------")

# nomor 2
i = 0
while (i <= n):
    j = n-1
    while (j >= i):
        print(" ", end="")
        j -= 1
    j = 1
    while (j <= i):
        print("*", end="")
        j += 1
    print()
    i += 1

print("-----------------------------------------------")

# nomor 3
for i in range(1, n+1):
    for o in range(1, i+1):
        print("o", end="")
    for plus in range(1, n-i+1):
        print("+", end="")
    print()

print("-----------------------------------------------")

# nomor 4
for i in range(n):
    for j in range(n-i):
        print(" ", end="")
    for k in range(i+1):
        print("o", end=" ")
    print()
for a in range(n):
    for b in range(a+1):
        print(" ", end="")
    for c in range(n-a):
        print("+", end=" ")
    print()

print("-----------------------------------------------")

# nomor 5
i = 1
while i <= n:
    j = 1
    while j <= ((n+1)-i):
        print(" ", end="")
        j += 1
    while j <= (n+1):
        print("o", end="")
        j += 1
    print()
    i += 1

i = 1
while i <= n:
    j = 1
    while j <= i:
        print(" ", end="")
        j += 1
    while j <= (n+1):
        print("+", end="")
        j += 1
    print()
    i += 1

# print("-----------------------------------------------")

# nomor 6
for a in range(n):
    for b in range(a+1):
        print(" ", end=" ")
    for c in range(n-a):
        print("+", end=" ")
    for d in range(n-a):
        print("o", end=" ")
    print()

for a in range(n):
    for j in range(n-a):
        print(" ", end=" ")
    for k in range(a+1):
        print("+", end=" ")
    for o in range(a+1):
        print("0", end=" ")
    print()
