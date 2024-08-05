# def kombinasi(n, k):
#     if k > n:
#         return 0
#     elif k == 0:
#         return 1
#     else:
#         return kombinasi(n-1, k-1) + kombinasi(n-1, k)


# # Contoh penggunaan
# n = int(input("Masukkan nilai n: "))
# k = int(input("Masukkan nilai k: "))
# print("Kemungkinan kombinasi yang ada untuk nilai k <= n adalah", kombinasi(n, k))

# # =======================================================================================
# print("\n")


# def pencipta(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * pencipta(n-1)


# def catalan(n):
#     return int(pencipta(2*n) / (pencipta(n+1) * pencipta(n)))


# n = int(input("Masukkan nilai n: "))
# for i in range(n+1):
#     print(catalan(i), end=" ")

def catalan(n):
    if n == 0 or n == 1:
        return 1
    else:
        return catalan(n-1) * (2*(2*n-1)) // (n+1)


n = int(input("Masukkan nilai n: "))
for i in range(n+1):
    print(catalan(i), end=" ")
