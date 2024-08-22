class Node:
    def __init__(self, ma_ve, noi_di, noi_den, gia_ve):
        self.ma_ve = ma_ve
        self.noi_di = noi_di
        self.noi_den = noi_den
        self.gia_ve = gia_ve
        self.left = None
        self.right = None

def initialize_tree():
    root = Node("A123", "Hanoi", "Ho Chi Minh", 5000000)
    root.left = Node("A234", "Hanoi", "Da Nang", 2500000)
    root.right = Node("A345", "Hanoi", "Hai Phong", 1500000)
    root.left.left = Node("A456", "Hanoi", "Nha Trang", 3000000)
    root.left.right = Node("A567", "Hanoi", "Phu Quoc", 4000000)
    return root

def print_tree(root, space=0):
    if root is not None:
        space += 10
        print_tree(root.right, space)
        print()
        for i in range(10, space):
            print(end=" ")
        print(root.gia_ve)
        print_tree(root.left, space)

def insert_node_divisible_by_9(root, value):
    if root is None:
        return Node(None, None, None, value)
    if value < root.gia_ve:
        root.left = insert_node_divisible_by_9(root.left, value)
    elif value > root.gia_ve:
        root.right = insert_node_divisible_by_9(root.right, value)
    return root

def preorder_traversal(root):
    if root:
        print(root.gia_ve, end=" ")
        preorder_traversal(root.left)
        preorder_traversal(root.right)

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.gia_ve, end=" ")
        inorder_traversal(root.right)

def postorder_traversal(root, condition, filename):
    if root:
        postorder_traversal(root.left, condition, filename)
        if condition(root.gia_ve):
            with open(filename, "a") as file:
                file.write(str(root.gia_ve) + "\n")
        postorder_traversal(root.right, condition, filename)

def sum_of_prices(root):
    if root is None:
        return 0
    return root.gia_ve + sum_of_prices(root.left) + sum_of_prices(root.right)

def tree_height_and_node_count(root):
    if root is None:
        return 0, 0
    if root.left is None and root.right is None:
        return 1, 1
    left_height, left_node_count = tree_height_and_node_count(root.left)
    right_height, right_node_count = tree_height_and_node_count(root.right)
    height = max(left_height, right_height) + 1
    node_count = left_node_count + right_node_count
    return height, node_count

def search_node(root, value):
    while root is not None:
        if value == root.gia_ve:
            return root
        elif value < root.gia_ve:
            root = root.left
        else:
            root = root.right
    return None

def delete_node(root, value):
    if root is None:
        return root

    if value < root.gia_ve:
        root.left = delete_node(root.left, value)
    elif value > root.gia_ve:
        root.right = delete_node(root.right, value)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp

        temp = find_minimum_node(root.right)
        root.gia_ve = temp.gia_ve
        root.right = delete_node(root.right, temp.gia_ve)
    return root

def find_minimum_node(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def main():
    root = initialize_tree()

    while True:
        print("\nMenu:")
        print("1. In cây nhị phân tìm kiếm")
        print("2. Thêm node vào cây")
        print("3. Duyệt và xuất dữ liệu theo thứ tự NLR")
        print("4. Duyệt và xuất dữ liệu theo thứ tự LNR")
        print("5. Ghi giá trị của các node thoả điều kiện vào file")
        print("6. Tính tổng giá trị của các vé máy bay")
        print("7. Tính chiều cao của cây và số lượng node")
        print("8. Tìm kiếm một vé máy bay")
        print("9. Xóa một vé máy bay")
        print("10. Kết thúc chương trình")

        choice = int(input("Chọn một chức năng (1-10): "))

        if choice == 1:
            print("Cây nhị phân tìm kiếm sau khi đã khởi tạo:")
            print_tree(root)
        elif choice == 2:
            value = int(input("Nhập giá trị của vé máy bay cần thêm: "))
            root = insert_node_divisible_by_9(root, value)
            print("Vé máy bay đã được thêm vào cây.")
        elif choice == 3:
            print("Duyệt và xuất dữ liệu theo thứ tự NLR:")
            preorder_traversal(root)
            print()
        elif choice == 4:
            print("Duyệt và xuất dữ liệu theo thứ tự LNR:")
            inorder_traversal(root)
            print()
        elif choice == 5:
            condition = lambda x: x % 9 == 0  # Điều kiện: giá trị vé máy bay chia hết cho 9
            filename = input("Nhập tên file để ghi dữ liệu: ")
            with open(filename, "w") as file:
                file.write("Giá trị của các vé máy bay thoả điều kiện là:\n")
            postorder_traversal(root, condition, filename)
            print("Dữ liệu đã được ghi vào file", filename)
        elif choice == 6:
            print("Tổng giá trị của tất cả các vé máy bay:", sum_of_prices(root))
        elif choice == 7:
            height, node_count = tree_height_and_node_count(root)
            print("Chiều cao của cây:", height)
            print("Số lượng vé máy bay trong cây:", node_count)
        elif choice == 8:
            value = int(input("Nhập giá trị của vé máy bay cần tìm kiếm: "))
            node = search_node(root, value)
            if node is not None:
                print("Vé máy bay được tìm thấy: Mã vé:", node.ma_ve, ", Nơi đi:", node.noi_di, ", Nơi đến:", node.noi_den, ", Giá vé:", node.gia_ve)
            else:
                print("Không tìm thấy vé máy bay có giá trị", value)
        elif choice == 9:
            value = int(input("Nhập giá trị của vé máy bay cần xóa: "))
            root = delete_node(root, value)
            print("Cây sau khi xóa vé máy bay có giá trị", value, ":")
            print_tree(root)
        elif choice == 10:
            print("Kết thúc chương trình.")
            break
        else:
            print("Vui lòng chọn một chức năng từ 1 đến 10.")

if __name__ == "__main__":
    main()
