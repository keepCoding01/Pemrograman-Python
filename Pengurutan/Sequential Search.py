def sequentialSearch(data: list, keyword: str) -> bool:

    status = False
    for item in data:
        if keyword.lower() == item.lower():
            print(f"{keyword} ditemukan pada posisi ke-{data.index(item) +
                  1} dan pada index ke-{data.index(item)}")
            status = True
            break
    if status == False:
        print(f"{keyword} tidak ditemukan")
    return status


nama = ["mamat", "budi", "siti", "wawan"]
sequentialSearch(nama, "budi")


# ----------------------------------------------------------------

def binarySearch(angka, key):
    low = 0
    high = len(angka) - 1
    mid = 0
    status = False

    while low <= high:
        mid = (low + high) // 2

        if (key == angka[mid]):
            print(f"{key} ditemukan pada posisi ke- {mid +
                  1} dan pada index ke-{mid}")
            status = True
            break
        else:
            if key > angka[mid]:
                low = mid + 1
            else:
                high = mid - 1

    if status == False:
        print(f"{key} tidak ditemukan dalam array")


nilai = [66, 77, 80, 84, 88, 99, 100]
binarySearch(nilai, 2)
