import random

# Định nghĩa lớp TreeNode
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Định nghĩa lớp cây nhị phân tìm kiếm
class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Hàm chèn một Node mới vào cây
    def insert(self, data):
        if not self.root:
            self.root = TreeNode(data)
        else:
            self._insert_recursive(self.root, data)

    # Hàm chèn đệ quy
    def _insert_recursive(self, node, data):
        if data[2] < node.data[2]:
            if not node.left:
                node.left = TreeNode(data)
            else:
                self._insert_recursive(node.left, data)
        elif data[2] > node.data[2]:
            if not node.right:
                node.right = TreeNode(data)
            else:
                self._insert_recursive(node.right, data)

    # Duyệt và xuất dữ liệu của cây theo thứ tự NLR
    def print_NLR(self, node):
        if node:
            print(node.data[2], end=" ")
            self.print_NLR(node.left)
            self.print_NLR(node.right)

    # Duyệt và xuất dữ liệu của cây theo thứ tự LNR
    def print_LNR(self, node):
        if node:
            self.print_LNR(node.left)
            print(node.data[2], end=" ")
            self.print_LNR(node.right)

    # Duyệt cây theo thứ tự LRN và ghi giá trị vào file
    def traverse_and_write_to_file(self, node, condition, filename):
        if node:
            self.traverse_and_write_to_file(node.left, condition, filename)
            self.traverse_and_write_to_file(node.right, condition, filename)
            if condition(node):
                with open(filename, "a") as file:
                    file.write(str(node.data[2]) + "\n")

    # Tính tổng giá trị của trường thứ 3 của tất cả các Node trong cây
    def sum_of_third_field(self, node):
        if not node:
            return 0
        return node.data[2] + self.sum_of_third_field(node.left) + self.sum_of_third_field(node.right)

    # Tính chiều cao của cây và số lượng Node lá
    def height_and_leaf_count(self, node):
        if not node:
            return 0, 0
        if not node.left and not node.right:
            return 1, 1
        left_height, left_leaf_count = self.height_and_leaf_count(node.left)
        right_height, right_leaf_count = self.height_and_leaf_count(node.right)
        height = max(left_height, right_height) + 1
        leaf_count = left_leaf_count + right_leaf_count
        return height, leaf_count

    # Tìm kiếm một Node có giá trị trường thứ 3 được nhập từ bàn phím
    def search_node(self, node, value):
        if not node or node.data[2] == value:
            return node
        if value < node.data[2]:
            return self.search_node(node.left, value)
        return self.search_node(node.right, value)

    # Xóa một Node có giá trị trường thứ 3 được nhập từ bàn phím
    def delete_node(self, node, value):
        if not node:
            return node
        if value < node.data[2]:
            node.left = self.delete_node(node.left, value)
        elif value > node.data[2]:
            node.right = self.delete_node(node.right, value)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            temp = self._find_minimum(node.right)
            node.data = temp.data
            node.right = self.delete_node(node.right, temp.data[2])
        return node

    def _find_minimum(self, node):
        current = node
        while current.left:
            current = current.left
        return current
    
# Hàm tạo cây nhị phân tìm kiếm với dữ liệu mẫu
def create_sample_binary_search_tree():
    tree = BinarySearchTree()
    sample_data = [
        ("M123", "Thương Hoài", random.randint(100, 1000)),
        ("M234", "Minh Châu", random.randint(100, 1000)),
        ("M345", "Thanh Trúc", random.randint(100, 1000)),
        ("M456", "My Le", random.randint(100, 1000)),
        ("M567", "Quốc Thái", random.randint(100, 1000))
    ]
    for data in sample_data:
        tree.insert(data)
    return tree

# Hàm chạy chương trình
def main():
    tree = create_sample_binary_search_tree()
    while True:
        print("\n==================Menu=================")
        print("1. Hiển thị thông tin của Node trong cây")
        print("2. Thêm vào cây Node có trường thứ 3 là số chia hết cho ký tự thứ 5 trong MaSV")
        print("3. Duyệt và xuất dữ liệu của cây theo thứ tự NLR")
        print("4. Duyệt và xuất dữ liệu của cây theo thứ tự LNR")
        print("5. Duyệt cây theo thứ tự LRN và ghi giá trị vào file")
        print("6. Tính tổng giá trị của trường thứ 3 của tất cả các Node")
        print("7. Tính chiều cao của cây và số lượng Node lá")
        print("8. Tìm kiếm một Node theo giá trị của trường thứ 3")
        print("9. Xóa một Node theo giá trị của trường thứ 3")
        print("10. Kết thúc chương trình")
        choice = input("Nhập lựa chọn của bạn: ")
        if choice == "1":
            print("\nThông tin của các Node trong cây:")
            print("------------------------------")
            tree.print_LNR(tree.root)
            print("\n------------------------------")
        elif choice == "2":
            # Thêm Node có trường thứ 3 là số chia hết cho ký tự thứ 5 trong MaSV
            pass
        elif choice == "3":
            print("\nDữ liệu của cây theo thứ tự NLR:", end=" ")
            tree.print_NLR(tree.root)
        elif choice == "4":
            print("\nDữ liệu của cây theo thứ tự LNR:", end=" ")
            tree.print_LNR(tree.root)
        elif choice == "5":
            condition = lambda node: node.data[2] % 5 == 0  # Điều kiện: giá trị chia hết cho 5
            filename = "SV.txt"
            tree.traverse_and_write_to_file(tree.root, condition, filename)
            print(f"\nĐã ghi giá trị của Node thỏa điều kiện vào file {filename}")
        elif choice == "6":
            print("\nTổng giá trị của trường thứ 3 của tất cả các Node:", tree.sum_of_third_field(tree.root))
        elif choice == "7":
            height, leaf_count = tree.height_and_leaf_count(tree.root)
            print("\nChiều cao của cây:", height)
            print("Số lượng Node lá của cây:", leaf_count)
        elif choice == "8":
            value = int(input("\nNhập giá trị của trường thứ 3 cần tìm kiếm: "))
            found_node = tree.search_node(tree.root, value)
            if found_node:
                print("Node được tìm thấy:", found_node.data)
            else:
                print("Không tìm thấy Node có giá trị trường thứ 3 là", value)
        elif choice == "9":
            value = int(input("\nNhập giá trị của trường thứ 3 cần xóa: "))
            tree.delete_node(tree.root, value)
            print("Đã xóa Node có giá trị trường thứ 3 là", value)
        elif choice == "10":
            print("\nKết thúc chương trình.")
            break
        else:
            print("\nLựa chọn không hợp lệ. Vui lòng chọn lại.")

# Chạy chương trình
if __name__ == "__main__":
    main()
