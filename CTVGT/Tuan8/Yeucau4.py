class Node:
    def __init__(self, value):
        self.value = value
        self.count = 1
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, node):
        if value == node.value:
            node.count += 1
        elif value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert(value, node.left)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert(value, node.right)

    def count_unique_values(self):
        return self._count_unique_values(self.root)

    def _count_unique_values(self, node):
        if node is None:
            return 0
        else:
            return 1 + self._count_unique_values(node.left) + self._count_unique_values(node.right)

    def count_occurrences(self, value):
        return self._count_occurrences(value, self.root)

    def _count_occurrences(self, value, node):
        if node is None:
            return 0
        elif value == node.value:
            return node.count
        elif value < node.value:
            return self._count_occurrences(value, node.left)
        else:
            return self._count_occurrences(value, node.right)

def main():
    data = input("Nhập dãy số, cách nhau bằng khoảng trắng: ").split()
    data = [int(num) for num in data]
    
    binary_tree = BinaryTree()
    for num in data:
        binary_tree.insert(num)

    # Số lượng giá trị phân biệt
    unique_count = binary_tree.count_unique_values()
    print("Số lượng giá trị phân biệt trong dãy số:", unique_count)

    # Đếm số lần xuất hiện cho mỗi giá trị phân biệt
    print("Số lần xuất hiện cho mỗi giá trị phân biệt:")
    unique_values = set(data)
    for value in sorted(unique_values):
        count = binary_tree.count_occurrences(value)
        print(f"{value}: {count}")

if __name__ == "__main__":
    main()
