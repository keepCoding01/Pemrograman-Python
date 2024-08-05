def min_nilai(N, K, array):
    """
    Menghitung nilai minimum pada kontes memilih bilangan.

    Args:
      N: Jumlah bilangan dalam array.
      K: Jumlah bilangan yang harus dipilih.
      array: Array berisi N bilangan.

    Returns:
      Nilai minimum yang bisa diperoleh pada kontes.
    """

    # Mengurutkan array.
    array.sort()

    # Menghitung selisih maksimum untuk setiap pasangan K bilangan.
    max_diff = [0] * (N - K + 1)
    for i in range(N - K + 1):
        max_diff[i] = array[i + K - 1] - array[i]

    # Mencari nilai minimum dari selisih maksimum.
    minimum_value = max_diff[0]
    for i in range(1, N - K + 1):
        minimum_value = min(minimum_value, max_diff[i])

    return minimum_value


# Membaca input.
N, K = map(int, input().split())
array = list(map(int, input().split()))

# Menghitung nilai minimum.
minimum_value = min_nilai(N, K, array)

# Menampilkan hasil.
print(minimum_value)
