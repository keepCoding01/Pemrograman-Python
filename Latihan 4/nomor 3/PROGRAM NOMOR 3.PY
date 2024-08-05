# sesuai instruksi soal pakai var pattern
# kata1 = str(input("masukkan kata ke-1     : "))
# kata2 = str(input("masukkan kata ke-2     : "))
# kata3 = str(input("masukkan kata ke-3     : "))
# kata4 = str(input("masukkan kata ke-4     : "))
# kata5 = str(input("masukkan kata ke-5     : "))

# pattern = "ma"
# daftar_kata = [kata1, kata2, kata3, kata4, kata5]
# kata = ""

# if daftar_kata[0][:len(pattern)] == pattern:
#     kata += daftar_kata[0] + " "
# if daftar_kata[1][:len(pattern)] == pattern:
#     kata += daftar_kata[1] + " "
# if daftar_kata[2][:len(pattern)] == pattern:
#     kata += daftar_kata[2] + " "
# if daftar_kata[3][:len(pattern)] == pattern:
#     kata += daftar_kata[3] + " "
# if daftar_kata[4][:len(pattern)] == pattern:
#     kata += daftar_kata[4] + " "

# print("daftar kata yang cocok :", kata)


kata1 = str(input("masukkan kata ke-1     : "))
kata2 = str(input("masukkan kata ke-2     : "))
kata3 = str(input("masukkan kata ke-3     : "))
kata4 = str(input("masukkan kata ke-4     : "))
kata5 = str(input("masukkan kata ke-5     : "))

pattern = "ma"
daftar_kata = [kata1, kata2, kata3, kata4, kata5]
kata = ""
kataBeda = ""

if daftar_kata[0][:len(pattern)] == pattern:
    kata += daftar_kata[0] + " "
elif daftar_kata[0][:len(pattern)] != pattern:
    kataBeda += daftar_kata[0] + " "

if daftar_kata[1][:len(pattern)] == pattern:
    kata += daftar_kata[1] + " "
elif daftar_kata[1][:len(pattern)] != pattern:
    kataBeda += daftar_kata[1] + " "

if daftar_kata[2][:len(pattern)] == pattern:
    kata += daftar_kata[2] + " "
elif daftar_kata[2][:len(pattern)] != pattern:
    kataBeda += daftar_kata[2] + " "

if daftar_kata[3][:len(pattern)] == pattern:
    kata += daftar_kata[3] + " "
elif daftar_kata[3][:len(pattern)] != pattern:
    kataBeda += daftar_kata[3] + " "

if daftar_kata[4][:len(pattern)] == pattern:
    kata += daftar_kata[4] + " "
elif daftar_kata[4][:len(pattern)] != pattern:
    kataBeda += daftar_kata[4] + " "

print("daftar kata yang cocok :", kata)
print("daftar kata yang tidak cocok :", kataBeda)
