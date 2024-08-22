class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Hàm chèn một node vào cây
def insert_node(root, data):
    if root is None:
        return Node(data)
    if data < root.data:
        root.left = insert_node(root.left, data)
    elif data > root.data:
        root.right = insert_node(root.right, data)
    return root

# Hàm nhập dữ liệu cho cây
def input_tree():
    root = None
    n = int(input("Nhập số lượng node bạn muốn thêm vào cây: "))
    print("Nhập giá trị cho các node:")
    for _ in range(n):
        data = int(input())
        root = insert_node(root, data)
    return root

# Hàm duyệt và xuất dữ liệu theo thứ tự LNR
def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.data, end=" ")
        inorder_traversal(root.right)

# Hàm chèn một node vào cây
def insert_node_to_tree(root):
    if root is None:
        print("Cây rỗng. Vui lòng nhập dữ liệu cho cây trước khi chèn node.")
        return root
    data = int(input("Nhập giá trị của node mới: "))
    return insert_node(root, data)

# Hàm đếm số nút lá của cây
def count_leaf_nodes(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    return count_leaf_nodes(root.left) + count_leaf_nodes(root.right)

# Hàm tính chiều cao của cây
def tree_height(root):
    if root is None:
        return -1
    left_height = tree_height(root.left)
    right_height = tree_height(root.right)
    return max(left_height, right_height) + 1

# Hàm tìm kiếm một node trong cây
def search(root, key):
    if root is None or root.data == key:
        return root
    if key < root.data:
        return search(root.left, key)
    return search(root.right, key)

# Hàm xóa một node khỏi cây
def delete_node(root, key):
    if root is None:
        return root
    if key < root.data:
        root.left = delete_node(root.left, key)
    elif key > root.data:
        root.right = delete_node(root.right, key)
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
        root.data = temp.data
        root.right = delete_node(root.right, temp.data)
    return root

def minValueNode(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

# Hàm hiển thị menu
def display_menu():
    print("\n1. Nhập dữ liệu cho cây")
    print("2. Chèn một node vào cây")
    print("3. Duyệt và xuất dữ liệu theo thứ tự LNR")
    print("4. Đếm số nút lá của cây")
    print("5. Tính chiều cao của cây")
    print("6. Tìm kiếm một node")
    print("7. Xóa một node")
    print("8. Thoát")

# Hàm main
def main():
    root = None

    while True:
        display_menu()
        choice = int(input("\nNhập lựa chọn của bạn: "))

        if choice == 1:
            root = input_tree()
            print("Dữ liệu đã được nhập vào cây.")

        elif choice == 2:
            root = insert_node_to_tree(root)
            if root:
                print("Node mới đã được chèn vào cây.")

        elif choice == 3:
            print("Duyệt và xuất dữ liệu theo thứ tự LNR:")
            inorder_traversal(root)

        elif choice == 4:
            leaf_count = count_leaf_nodes(root)
            print("Số nút lá của cây là:", leaf_count)

        elif choice == 5:
            height = tree_height(root)
            print("Chiều cao của cây là:", height)

        elif choice == 6:
            key = int(input("Nhập giá trị cần tìm: "))
            result = search(root, key)
            if result:
                print("Node có giá trị", key, "được tìm thấy trong cây.")
            else:
                print("Node có giá trị", key, "không tồn tại trong cây.")

        elif choice == 7:
            key = int(input("Nhập giá trị của node cần xóa: "))
            root = delete_node(root, key)
            print("Node có giá trị", key, "đã được xóa khỏi cây.")

        elif choice == 8:
            print("Kết thúc chương trình.")
            break

        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

if __name__ == "__main__":
    main()
