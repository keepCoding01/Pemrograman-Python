jumlahKandang, banyakOperasi = map(int, input(
    "\nBanyak kandang, banyak operasi : ").split())
graph = [[] for _ in range(jumlahKandang+1)]
cek = []
results = []

for i in range(banyakOperasi):
    operasi = list(map(int, input(f"operasi ke - {i+1}: ").split()))
    a, b = operasi[1:]

    if operasi[0] == 1:
        # buat jalan dari kandang a ke kandang b
        graph[a].append(b)
        # buat jalan dari kandang b ke kandang a
        graph[b].append(a)
    elif operasi[0] == 2:
        terhubung = False
        kunjunganDFS = [False] * (jumlahKandang + 1)

        def dfs(node):
            global terhubung
            kunjunganDFS[node] = True
            if node == b:
                terhubung = True
            for tetangga in graph[node]:
                if not kunjunganDFS[tetangga]:
                    dfs(tetangga)

        dfs(a)
        if terhubung:
            results.append(f"('Kandang {a} Kandang {b}','Terhubung')")
        else:
            results.append(f"('Kandang {a} Kandang {b}','Tidak Terhubung')")

for hasil in results:
    print(hasil)
