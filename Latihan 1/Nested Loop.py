

n = int(input("Masukkan angka : "))
for i in range(n):
    for j in range(n-i-1):
        print(" ", end=" ")
    for k in range(i+1):
        print("*", end=" ")
    print()

n = int(input("Masukkan angka : "))
i = 0
while i < n:
    j = 0
    while j < n-i-1:
        print(" ", end="")
        j += 1
    k = 0
    while k < i+1:
        print("*", end="")
        k += 1
    print()
    i += 1

n = int(input("Masukkan angka : "))

for i in range(1, n+1):
    for j in range(i):
        print("o", end= " ")
    for k in range(n - i):
        print("+", end=" ")
    print()


total_kembalian = int(input("Total Kembalian = "))
strkem = str(total_kembalian)
print("Kembalian tersebut dibentuk dari : ")

for i in range(0, len(strkem)):
    for j in range(1):
        print(strkem[i], "x", 1, end="")

    for k in range(len(strkem)-1, i, -1):
        print("0",end=" ")
    print()


baris = int(input("Masukkan baris : "))
kolom = int(input("Masukkan kolom : "))

for i in range(1, baris + 1):
    for j in range(1, kolom + 1):
        print(i * j, end="\t")
    print()
    print("------------------------------------------")