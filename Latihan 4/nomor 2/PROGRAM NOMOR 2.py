print("=========================================================")
print("                   HAPUS SATU SAJA                       ")
print("=========================================================")

kata_pertama = str(input("Kata Pertama : "))
kata_kedua = str(input("Kata Kedua   : "))

if kata_pertama == kata_kedua:
    for hilang in kata_kedua:
        if hilang == "p":
            continue
        print(hilang, end="")
    print("\n")
    print("tentu saja bisa!")

while kata_pertama != kata_kedua:
    print("wah! tidak bisa :(")
    break

print()
