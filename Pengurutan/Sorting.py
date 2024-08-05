def Bubblesort(bilangan):
    print("Sebelum")
    bil = bilangan
    print(bil)

    for i in range(len(bilangan)):
        for j in range(len(bilangan) - 1):
            if bilangan[j] > bilangan[j+1]:
                tampung = bilangan[j]
                bilangan[j] = bilangan[j+1]
                bilangan[j+1] = tampung

    print("Sesudah")
    bil = bilangan
    print(bil)


nilai = [99, 76, 87, 69, 80]
Bubblesort(nilai)


# ----------------------------------------------------

def SelectionSort(bilangan):
    print("Sebelum")
    bil = bilangan
    print(bil)

    for i in range(len(bilangan)):
        indexArray = i
        for j in range(len(bilangan)):
            if bilangan[indexArray] < bilangan[j]:
                indexArray = j
                tampung = bilangan[i]
                bilangan[i] = bilangan[indexArray]
                bilangan[indexArray] = tampung

    print("Sesudah")
    bil = bilangan
    print(bil)


nilai = [69, 89, 31, 56, 99]
SelectionSort(nilai)

# ===============================================================

def SelectionSort(bilangan):
    print("Sebelum")
    bil = bilangan
    print(bil)

    for i in range(len(bilangan)):
        # Hapus j=i
        for j in range(i, 0, -1):  # Perbaiki perulangan j
            if bilangan[j] < bilangan[j-1]:
                tampung = bilangan[j]
                bilangan[j] = bilangan[j-1]
                bilangan[j-1] = tampung

    print("Sesudah")
    bil = bilangan
    print(bil)


nilai = [90, 54, 67, 98, 76]
SelectionSort(nilai)

# -------------------------------------------------------------

def Mergesort(bilangan):
    print("Sebelum:", bilangan)

    if len(bilangan) <= 1:
        return bilangan

    nilaiTengah = len(bilangan) // 2
    kiri = Mergesort(bilangan[:nilaiTengah])
    kanan = Mergesort(bilangan[nilaiTengah:])

    return gabung(kiri, kanan)


def gabung(kiri, kanan):
    hasilGabung = []
    indexKiri = 0
    indexKanan = 0

    while indexKiri < len(kiri) and indexKanan < len(kanan):
        if kiri[indexKiri] < kanan[indexKanan]:
            hasilGabung.append(kiri[indexKiri])
            indexKiri += 1
        else:
            hasilGabung.append(kanan[indexKanan])
            indexKanan += 1

    # Tambahkan elemen yang tersisa
    if indexKiri < len(kiri):
        hasilGabung.extend(kiri[indexKiri:])
    if indexKanan < len(kanan):
        hasilGabung.extend(kanan[indexKanan:])

    print("Penggabungan:", kiri, "+", kanan, "=", hasilGabung)
    return hasilGabung


nilai = [66, 43, 90, 76, 87, 21]
hasil = Mergesort(nilai)
print(f"Hasil pengurutan akhir: {hasil}")

# ===============================================================
def merge_sort(data):
    if len(data) <= 1:
        return data

    # Bagi data menjadi dua sub-daftar kiri dan kanan
    mid = len(data) // 2
    left = merge_sort(data[:mid])
    right = merge_sort(data[mid:])

    # Gabungkan sub-daftar kiri dan kanan secara terurut
    return merge(left, right)


def merge(left, right):
    merged = []
    i = 0
    j = 0

    # Bandingkan elemen dari left dan right dan tambahkan ke merged
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Tambahkan elemen yang tersisa dari left atau right
    merged += left[i:]
    merged += right[j:]

    return merged


# Contoh penggunaan
data = [64, 34, 25, 12, 22, 11, 90]
print(f"Data awal: {data}")

sorted_data = merge_sort(data)
print(f"Data setelah diurutkan: {sorted_data}")

# =============================================================

def quickSort(angka):
    print("Sebelum")
    print(angka)

    quickSortAlgorithm(angka, 0, len(angka)-1)

    print("Sesudah")
    print(angka)


def quickSortAlgorithm(angka, indexAwal, indexAkhir):
    i = indexAwal
    j = indexAkhir
    pivot = angka[(indexAwal + indexAkhir) // 2]

    while i <= j:
        while angka[i] < pivot:
            i += 1
        while angka[j] > pivot:
            j -= 1

        if i <= j:
            angka[i], angka[j] = angka[j], angka[i]
            i += 1
            j -= 1

    if indexAwal < j:
        quickSortAlgorithm(angka, indexAwal, j)
    if i < indexAkhir:
        quickSortAlgorithm(angka, i, indexAkhir)


nilai = [15, 76, 45, 98, 34]
quickSort(nilai)
