s = input("masukkan nama variabel : ")

camel_case = ""
cekUnderscore = False

for karakter in s:
    if karakter == '_':
        cekUnderscore = True
    elif cekUnderscore:
        if 'a' <= karakter <= 'z':
            karakter = chr(ord(karakter) - 32)
        camel_case += karakter
        cekUnderscore = False
    else:
        camel_case += karakter

print("setelah diubah         :", camel_case)

# angka -32 digunakan dalam operasi pengurangan 32 dari kode ASCII karakter
# untuk mengubah karakter yang sebelumnya huruf kecil menjadi huruf kapital.
