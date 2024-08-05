# # Minta pengguna memasukkan bilangan
# n = int(input("Masukkan bilangan bulat non-negatif untuk menghitung faktorial: "))

# # Validasi bahwa n adalah bilangan bulat non-negatif
# while n < 0:
#     n = int(input("Masukkan bilangan bulat non-negatif untuk menghitung faktorial: "))

# # Inisialisasi nilai faktorial
# factorial = 1

# # Menghitung faktorial
# for i in range(1, n + 1):
#     factorial *= i

# # Tampilkan hasil faktorial
# print("Faktorial dari", n, "adalah:", factorial)



n=7
for i in range (n):
 for j in range (n):
     print (i,end="")
 print()

 n=7
for i in range (n):
 for j in range (n,i,-1):
    print(i,end="")
 print()