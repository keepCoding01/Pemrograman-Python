n = int(input("Masukkan angka : "))
i = 0
while (i <= n ):
    print("*" * i)
    i += 1


n = int(input("Masukkan angka : "))
i = 0
while (i < n):
    print("*" * (n - i))
    i+=1

i = n
while ( i >= 1):
    print("*" * i)
    i -= 1

n = int(input("Masukkan angka : "))
i = 0
while ( i < n + 1):
    print(" " * (n - i), "*" * i)
    i += 1


n = int(input("Masukkan angka : "))
i = 0
while ( i < n):
    print(" " * i, "*" * (n - i))
    i += 1

i = n
while i >= 1:
    print(" " * (n - i), "*" * i)
    i -= 1

n = int(input("Masukkan angka : "))
i = 1
while (i < n + 1 ):
    print(" " * (n - i) , "*" * i * 2)
    i += 1


i = n
while ( i >= 1):
    print(" " * (n - i), "*" * i * 2) 
    i -= 1