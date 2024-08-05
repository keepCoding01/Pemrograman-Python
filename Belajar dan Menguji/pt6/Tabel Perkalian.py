baris = int(input("Masukkan baris : "))
kolom = int(input("Masukkan kolom : "))

for i in range(1, baris+1):
    for j in range(1, kolom+1):
        print(i*j, end="\t")
        print()
        print("---------------------------------------------------------------")
