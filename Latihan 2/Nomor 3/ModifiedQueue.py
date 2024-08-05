def reverse_queue(queue):
    queue[:] = queue[::-1]


jumlahData = int(input("\nJumlah data anda yang ingin anda masukkan = "))
queue = []
result = []

for data in range(jumlahData):
    tanya = input(
        f"\nMasukkan data ke-{data+1} anda dengan format (add/del/rev) diikuti dengan nilai data anda = ").split()
    if tanya[0] == 'add':
        # ambil elemen pertama dan kedua dari tanya
        x, y = int(tanya[1]), int(tanya[2])
        for data in range(y):  # nambahkan nilai x sebanyak y
            queue.append(x)
        result.append(len(queue))
    elif tanya[0] == 'del':
        y = int(tanya[1])
        if y > len(queue):
            result.append(-1)
        else:
            result.append(queue.pop(0))
    elif tanya[0] == 'rev':
        reverse_queue(queue)

print("\nresult : ")
for r in result:
    print(r)
