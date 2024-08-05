def bmi_calculator(name, height_m, weight_kg):
    bmi = weight_kg/(height_m ** 2)
    print("BMI : %.2f   " % bmi)

    if bmi > 25:
        return name + " is overweight"
    else:
        return name + " is not overweight"


name = ["YK", "YK's Sister", "YK's Brother"]
height = [2, 1.8, 1.5]
weight = [90, 85, 100]

for i in range(len(name)):
    result = bmi_calculator(name[i], height[i], weight[i])
    print(result)

print("====================================================")


def bmi_calculator(name, height_m, weight_kg):
    bmi = weight_kg/(height_m ** 2)
    print("BMI : %.2f   " % bmi)

    if bmi > 25:
        over = 25 * (height_m**2)
        return name + f" is overweight = {over}"
    else:
        not_over = bmi * (height_m**2)
        return name + f" is not overweight = {not_over}"


name = ["YK", "YK's Sister", "YK's Brother"]
height = [2, 1.8, 1.5]
weight = [90, 85, 100]

for i in range(len(name)):
    result = bmi_calculator(name[i], height[i], weight[i])
    print(result)

# RUMUS :
# bmi = berat/tinggi pngkt 2
# ov = 25 x tinggi pangkat 2
# not = bmi x tinggi pangkat 2


print("====================================================")


def add(Angka1, Angka2):
    res_angka1 = str(Angka1)[::-1]
    res_angka2 = str(Angka2)[::-1]
    jumlah = Angka1 + Angka2
    print("Reserve angka 1 : ", int(res_angka1))
    print("Reserve Angka 2 : ", int(res_angka2))
    return jumlah


Angka1 = int(input("Masukkan nilai angka pertama : "))
Angka2 = int(input("Masukkan nilai angka kedua : "))

jumlah = add(Angka1, Angka2)
print("total =", jumlah)
