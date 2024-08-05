def ubah_huruf(s):
    hasil = ''
    for karakter in s:
        if karakter.islower():
            hasil += karakter.upper()
        else:
            hasil += karakter.lower()
    return hasil


# Input dari pengguna
kata_dengklek = input("Masukkan kata dalam Bahasa Dengklek: ")

# Memanggil fungsi dan menampilkan hasil
hasil_perubahan = ubah_huruf(kata_dengklek)
print(hasil_perubahan)
