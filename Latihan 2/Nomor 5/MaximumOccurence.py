def jumlahMuncul(teks):
    karakterMuncul = {}
    maksimalKarakter = None
    maksimalJumlah = 0

    for karakter in teks:
        if karakter in karakterMuncul:
            karakterMuncul[karakter] += 1
        else:
            karakterMuncul[karakter] = 1

    for karakter, jumlah in karakterMuncul.items():
        if jumlah > maksimalJumlah:
            maksimalKarakter = karakter
            maksimalJumlah = jumlah
        elif jumlah == maksimalJumlah and karakter < maksimalKarakter:
            maksimalKarakter = karakter

    return maksimalKarakter, maksimalJumlah


teks = str(input("Masukkan teks : "))
result = jumlahMuncul(teks)
print("Character:", result[0], ", Occurrence:", result[1])
