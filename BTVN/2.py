class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Khởi tạo một cây nhị phân
def initialize_tree():
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    root.left.left = Node(3)
    root.left.right = Node(7)
    root.right.left = Node(12)
    root.right.right = Node(20)
    return root

# Tính và trả về tổng giá trị các node trên cây nhị phân
def sum_tree(root):
    if root is None:
        return 0
    return root.data + sum_tree(root.left) + sum_tree(root.right)

# Tìm giá trị nguyên lớn nhất và nhỏ nhất trong cây nhị phân tìm kiếm
def max_integer_value(root):
    while root and root.right:
        root = root.right
    return root.data if root else None

def min_integer_value(root):
    while root and root.left:
        root = root.left
    return root.data if root else None

# Tính và trả về số lượng các node của cây nhị phân
def count_nodes(root):
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)

# Tính và trả về số lượng các node lá trên cây nhị phân
def count_leaf_nodes(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    return count_leaf_nodes(root.left) + count_leaf_nodes(root.right)

# Main function
def main():
    # Khởi tạo cây nhị phân
    root = initialize_tree()

    # Tính tổng giá trị các node trên cây nhị phân
    total_sum = sum_tree(root)
    print("Tổng giá trị các node trên cây nhị phân:", total_sum)

    # Tìm giá trị nguyên lớn nhất và nhỏ nhất trong cây nhị phân
    max_value = max_integer_value(root)
    min_value = min_integer_value(root)
    print("Giá trị nguyên lớn nhất trong cây nhị phân:", max_value)
    print("Giá trị nguyên nhỏ nhất trong cây nhị phân:", min_value)

    # Tính và trả về số lượng các node của cây nhị phân
    node_count = count_nodes(root)
    print("Số lượng các node của cây nhị phân:", node_count)

    # Tính và trả về số lượng các node lá trên cây nhị phân
    leaf_count = count_leaf_nodes(root)
    print("Số lượng các node lá trên cây nhị phân:", leaf_count)

if __name__ == "__main__":
    main()
