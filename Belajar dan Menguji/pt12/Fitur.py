print("-"*15,'Nomor 1',"-"*15)
def menu():
    print("\nFitur yang ingin digunakan ( 1/2/3 ) : ", end="")
    fitur = input()
    if fitur == "1":
        register()
    elif fitur == "2":
        login()
    elif fitur == "3":
        exit_program()
    else:
        print("Kode yang anda masukkan salah")
        menu()
def register():
    username = input("Masukkan username anda : ")
    print("\nBerhasil mendaftarkan username", username)
    menu()
def login():
    username = input("Masukkan username anda : ")
    print("\nBerhasil login. Selamat datang kembali", username)
    play_music()
def exit_program():
    print("\nKeluar dari program")
    exit()
def play_music():
    music_list = [
        "Blinding Lights",
        "Pesawat Kertas",
        "Pesan Terakhir",
        "Menghapus Jejakmu",
        "Narco"
    ]
    print("\nKumpulan Lagu")
    print("====")
    for i, music in enumerate(music_list, start=1):
        print(f"{i}. {music}")
    print("====")
    queue = []
    while True:
        add_music = input("\nApakah anda ingin menambahkan lagu ke dalam queue ? ( Y / N ) : ").lower()
        if add_music == "y":
            while True:
                try:
                    music_no = int(input("Lagu no berapa yang ingin ditambahkan ke dalam queue ? "))
                    if music_no >= 1 and music_no <= len(music_list):
                        if music_list[music_no - 1] not in queue:
                            queue.append(music_list[music_no - 1])
                            print("Berhasil menambahkan lagu ke dalam queue")
                            break
                        else:
                            print("Lagu tersebut sudah ada di dalam queue")
                            break
                    else:
                        print("Kode yang anda masukkan salah")
                except ValueError:
                    print("Kode yang anda masukkan salah")
        elif add_music == "n":
            break
        else:
            print("Kode yang anda masukkan salah")
    print("\nQueue Lagu")
    print("=======")
    for music in queue:
        print(music)
    print("=======")
    if queue:
        print("\nNow Playing :", queue[0])
        queue.pop(0)
    else:
        print("\nTidak ada lagu dalam queue")
    play_again = input("\nApakah anda ingin menambahkan lagu lagi ? ( Y / N ) : ").lower()
    if play_again == "y":
        play_music()
    elif play_again == "n":
        exit_program()
    else:
        print("Kode yang anda masukkan salah")
        play_music()
menu()



