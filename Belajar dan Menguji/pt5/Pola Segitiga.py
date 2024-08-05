n = int(input("Masukkan n : "))

# nomor 1
for i in range(n+1):
    print("*"*i)

print("------------------------------")

# nomor 2
for i in range(n):
    print("*"*(n-i))

print("------------------------------")

# nomor 3
for i in range(n+1):
    print(" "*(n-i), "*"*(i))

print("------------------------------")

# nomor 4
for i in range(n+1):
    print(" "*(n-i), "*"*(i*2))

print("------------------------------")

# nomor 5
i = 0
while (i < n+1):
    print("*"*i)
    i += 1

print("------------------------------")

# nomor 6
i = 0
while (i < n):
    print("*"*(n-i))
    i += 1

print("------------------------------")

# nomor 7
i = 0
while (i < (n+1)):
    print(" "*(n-i), "*"*(i))
    i += 1

print("------------------------------")

# nomor 8
i = 0
while (i < (n+1)):
    print(" "*(n-i), "*"*(i*2))
    i += 1


# ==========================================================================================
# cara lain
n = int(input("Masukkan Jumlah baris dan Kolom : "))
for i in range(1, n + 1):
    print("*" * i)

n = int(input("Masukkan Jumlah baris dan Kolom : "))
for i in range(n, 0, -1):
    print("*" * i)

n = int(input("Masukkan Jumlah baris dan Kolom : "))
for i in range(1, n + 1):
    spasi = " " * (n - i)
    bintang = "*" * i
    print(spasi + bintang)

n = int(input("Masukkan Jumlah baris dan Kolom : "))
for i in range(2, n + 1):
    spasi = " " * (n - i)
    bintang = "*" * (2 * i - 2)
    print(spasi + bintang)
