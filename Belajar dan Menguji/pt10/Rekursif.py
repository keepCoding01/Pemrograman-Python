# nomor 1
def fakto(n):
    if n == 0:
        return 1
    else:
        return n*fakto(n-1)


print(f"Hasil Fakto: ", fakto(5))


def kombinasi(n, k):
    if k > n:
        return 0
    else:
        return fakto(n)/(fakto(k)*fakto(n-k))


n = int(input("Masukkan n: "))
k = int(input("Masukkan k: "))
print(f'Hasil kombinasi: ', (round(kombinasi(n, k))))


# nomor 2
def angka(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * angka(n-1)


def Catalan(n):
    return int(angka(2*n) / (angka(n+1) * angka(n)))


n = int(input("Masukkan nilai n: "))
for i in range(n+1):
    print(Catalan(i), end=" ")

# soal tambahan


def fungsi(n):
    if n == 0:
        return 3
    else:
        return 2*fungsi(n-1)+4


n = int(input("Masukkan n: "))
print(f"Hasil fungsi: ", fungsi(n))

# soal tambahan


def fungsi(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return (n-1) + (n-2)


n = int(input("Masukkan n: "))
print(f"Hasil fungsi: ", fungsi(n))
