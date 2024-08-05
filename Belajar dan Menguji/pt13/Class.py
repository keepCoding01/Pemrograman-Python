class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def display(self):
        nilai = []
        current_node = self.head
        while current_node:
            nilai.append(str(current_node.data))
            current_node = current_node.next
        return " -> ".join(nilai)

    def bagianHapus(self, posisiHapus):
        if self.head:
            current = self.head

            if posisiHapus == 0:
                self.head = current.next
                current = None
                return

            for i in range(posisiHapus - 1):
                current = current.next
                if current is None:
                    break

            if current is None:
                return
            if current.next is None:
                return

            next = current.next.next
            current.next = None
            current.next = next

    def hapusNode(self):
        while True:
            hapusData = input("Masukkan data yang akan dihapus: ")
            if hapusData.isdigit():
                hapusData = int(hapusData)
                break
            else:
                print("Mohon masukkan angka yang valid")

        current = self.head
        while current:
            if current.data == hapusData:
                current.data = current.next.data
                current.next = current.next.next
                return
            current = current.next
        print("Data yang akan dihapus tidak ditemukan")


jumlah = int(input("Jumlah data yang ingin dimasukkan = "))
ll = LinkedList()

for i in range(jumlah):
    tanya = int(input(f"Masukkan data ke-{i+1} anda : "))
    ll.append(tanya)

print("Banyak data:", jumlah)
print("Data kata ke:", ll.display())

while True:
    pilihan = input("Apakah anda ingin menghapus data? (y/n) = ").lower()
    if pilihan == 'y':
        while True:
            posisiHapus = input(
                "Masukkan posisi data yang akan dihapus (mulai dari 1): ")
            if posisiHapus.isdigit():
                posisiHapus = int(posisiHapus) - 1
                if posisiHapus < 0 or posisiHapus >= jumlah:
                    print("Posisi data tidak valid")
                else:
                    ll.bagianHapus(posisiHapus)
                    print("\nData yang dihapus adalah:", posisiHapus + 1)
                    print("Data kata ke:", ll.display())
                    break
            else:
                print("Mohon masukkan angka yang valid")
    elif pilihan == 'n':
        print("Program anda selesai")
        break
    else:
        print("Mohon masukkan 'y' atau 'n'")
