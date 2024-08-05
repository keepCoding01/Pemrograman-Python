n = int(input())
huruf = input()
x = []
for i in range(3):
    x.append(huruf[i])
maks = 0
if x[0] == x[1] or x[0] == x[2] or x[1] == x[2]:
    maks = -1
else:
    for i in range[3]:
        for j in range(3):
            if x[i] == huruf[j]:
                maks += 1

print(maks)
