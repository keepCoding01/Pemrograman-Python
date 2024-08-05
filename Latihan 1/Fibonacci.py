# def fibo(n):
#     if n <= 0:
#         return 0
#     elif n == 1 or n == 2:
#         return 1
#     else:
#         a = 1
#         b = 1
#         for ubah in range(2, n):
#             tambah = a + b
#             a = b
#             b = tambah
#         return b
#     n = 10
#     hasil_fibo = fibo(n)
#     print(f"bilangan fibo ke-{n} adalah : {hasil_fibo}")


# =====================================================================
def fibo(n):

    if n <= 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        a = 1
        b = 1
        ubah = 2
        while ubah < n:
            tmp = a + b
            a = b
            b = tmp
            ubah += 1
        return b


n = int(input("Masukkan nilai n untuk jumlah bilangan Fibonacci: "))
hasil_fibo = fibo(n)
print(f"bilangan fibo ke-{n} adalah: {hasil_fibo}")

# =================================================================================

# def fibonacci(n):
#     if n <= 0:
#         return "Masukkan bilangan bulat positif"
#     elif n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     else:
#         a, b = 0, 1
#         total = 1  # Inisialisasi dengan Fib(2) yang sudah diketahui
#         for _ in range(3, n + 1):
#             a, b = b, a + b
#             total += b
#         return total


# # Input dari pengguna
# input_n = int(input("Masukkan nilai n untuk jumlah bilangan Fibonacci: "))

# # Memanggil fungsi dan menampilkan hasil
# hasil = fibonacci(input_n)
# print(f"Jumlah {input_n} bilangan Fibonacci adalah {hasil}")

# =================================================================================
def tampilkan_deret(n):
    deret = [i*3 for i in range(1, n+1)]
    return deret


n = 5
hasil_deret = tampilkan_deret(n)
print(hasil_deret)


# =========================================================================================

def tampilkan_deret(n):
    deret = []
    i = 1
    while i <= n:
        deret += [i*3]
        i += 1
    return deret


n = 5
hasil_deret = tampilkan_deret(n)
print(hasil_deret)
