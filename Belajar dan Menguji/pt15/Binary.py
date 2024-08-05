class Node:
    def __init__(self, kode):
        self.left = None
        self.right = None
        self.val = kode


def insert(root, kode):
    if root is None:
        return Node(kode)
    else:
        if root.val < kode:
            root.right = insert(root.right, kode)
        else:
            root.left = insert(root.left, kode)
    return root


def minValueNode(node):
    current = node
    while (current.left is not None):
        current = current.left
    return current


def delete(root, kode):
    if root is None:
        return root
    if kode < root.val:
        root.left = delete(root.left, kode)
    elif (kode > root.val):
        root.right = delete(root.right, kode)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        temp = minValueNode(root.right)
        root.val = temp.val
        root.right = delete(root.right, temp.val)
    return root


def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.val, end=" ")
        inorder_traversal(root.right)


def preorder_traversal(root):
    if root:
        print(root.val, end=" ")
        preorder_traversal(root.left)
        preorder_traversal(root.right)


def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.val, end=" ")


if __name__ == "__main__":
    jumlah = int(input("Masukkan jumlah data : "))
    root = None
    for i in range(jumlah):
        kode = int(input(f"Masukkan kode ke - {i+1} : "))
        root = insert(root, kode)
    print("Inorder traversal: ", end="")
    inorder_traversal(root)
    while True:
        print("\n\nPilihan Fitur:")
        print("1. Masukkan data baru")
        print("2. Hapus data")
        print("3. Traversal")
        print("4. Keluar")
        pilihan = int(input("Masukkan pilihan menu (1 s.d. 4): "))
        if pilihan == 1:
            kode = int(input("Masukkan data baru: "))
            root = insert(root, kode)
            print("Inorder traversal: ", end="")
            inorder_traversal(root)
        elif pilihan == 2:
            kode = int(input("Masukkan data yang akan dihapus: "))
            root = delete(root, kode)
            print("Inorder traversal: ", end="")
            inorder_traversal(root)
        elif pilihan == 3:
            print("\nPilihan Traversal:")
            print("1. Inorder traversal")
            print("2. Preorder traversal")
            print("3. Post order traversal")
            print("4. Keluar")
            pilihanTraverse = int(input("Masukkan pilihan menu (1 s.d. 4): "))
            if pilihanTraverse == 1:
                print("Inorder traversal: ", end="")
                inorder_traversal(root)
            elif pilihanTraverse == 2:
                print("Preorder traversal: ", end="")
                preorder_traversal(root)
            elif pilihanTraverse == 3:
                print("Postorder traversal: ", end="")
                postorder_traversal(root)
        elif pilihan == 4:
            print("Terima kasih telah menggunakan program ini")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
