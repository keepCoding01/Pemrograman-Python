n = int(input("Masukkan bilangan positif : "))

while n <= 0:
    n = int(input("Masukkan bilangan bulat positif n : "))

total = 0

print("Deret bilangan positif dari 1 hingga", n, "adalah : ")
for i in range(n + 1):
    print(i, end=" ")
    total += i

print("\n Total dari deret tersebut adalah : ",total)

