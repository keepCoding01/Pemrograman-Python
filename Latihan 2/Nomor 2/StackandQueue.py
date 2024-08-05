class QueueStack:
    def __init__(self):
        self.stack = []
        self.queue = []

    def push_front(self, data):
        self.stack.append(data)

    def push_back(self, data):
        self.queue.append(data)

    def pop_front(self):
        if not self.stack:
            self.stack.extend(reversed(self.queue))
            self.queue = []
        return self.stack.pop()

    def pop_back(self):
        if not self.queue:
            self.queue.extend(reversed(self.stack))
            self.stack = []
        return self.queue.pop()

    def __str__(self):
        return str(self.stack[::-1] + self.queue)


while True:
    jumlahPerintah = int(
        input("\nJumlah perintah yang ingin dijalankan : "))
    qs = QueueStack()

    for i in range(jumlahPerintah):
        perintah = input(
            "\nPilih perintah ke-{} (push back, push front, pop back, pop front): ".format(i+1))

        if perintah == 'push back':
            nilaiPerintah = int(input("Masukkan nilai data" + " " +
                                      perintah + " " + "Anda (bebas) : "))
            qs.push_back(nilaiPerintah)
            print("Perintah {}: nilai {}: {}".format(
                i+1, perintah, nilaiPerintah))

        elif perintah == 'push front':
            nilaiPerintah = int(input("Masukkan nilai data" + " " +
                                      perintah + " " + "Anda (bebas) : "))
            qs.push_front(nilaiPerintah)
            print("Perintah {}: nilai {}: {}".format(
                i+1, perintah, nilaiPerintah))

        elif perintah == 'pop back':
            qs.pop_back()
            print("Perintah {} yaitu {}".format(i+1, perintah))

        elif perintah == 'pop front':
            qs.pop_front()
            print("Perintah {} yaitu {}".format(i+1, perintah))

    print("\nKondisi terakhir dari QueueStack :", qs)
    tanya = input("\nApakah anda ingin lanjut (ya/tidak) ? ")

    if tanya == "tidak":
        break

print("Program selesai, senang kamu telah menggunakan program saya 😊")
