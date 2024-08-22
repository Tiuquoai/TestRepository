class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Kiểm tra cây rỗng
def is_empty(root):
    return root is None

# Kiểm tra nút n có phải là nút lá không
def is_leaf(node):
    return node is not None and node.left is None and node.right is None

# Kiểm tra nút n có phải là nút cha của nút m không
def is_parent_of(root, node_n, node_m):
    if root is None:
        return False
    if root.left == node_n or root.right == node_n:
        return True
    return is_parent_of(root.left, node_n, node_m) or is_parent_of(root.right, node_n, node_m)

# Tính chiều cao của cây
def tree_height(root):
    if root is None:
        return -1
    left_height = tree_height(root.left)
    right_height = tree_height(root.right)
    return max(left_height, right_height) + 1

# Tính số nút của cây
def count_nodes(root):
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)

# Duyệt tiền tự, trung tự, hậu tự
def preorder_traversal(root):
    if root:
        print(root.data, end=" ")
        preorder_traversal(root.left)
        preorder_traversal(root.right)

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.data, end=" ")
        inorder_traversal(root.right)

def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.data, end=" ")

# Đếm số nút lá của cây
def count_leaf_nodes(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    return count_leaf_nodes(root.left) + count_leaf_nodes(root.right)

# Đếm số nút trung gian của cây
def count_intermediate_nodes(root):
    if root is None or (root.left is None and root.right is None):
        return 0
    return 1 + count_intermediate_nodes(root.left) + count_intermediate_nodes(root.right)

# Nút có giá trị lớn nhất, nhỏ nhất, tổng giá trị các nút, trung bình giá trị các nút
def max_node(root):
    if root is None:
        return None
    while root.right:
        root = root.right
    return root.data

def min_node(root):
    if root is None:
        return None
    while root.left:
        root = root.left
    return root.data

def sum_of_nodes(root):
    if root is None:
        return 0
    return root.data + sum_of_nodes(root.left) + sum_of_nodes(root.right)

def average_of_nodes(root):
    if root is None:
        return 0
    count = count_nodes(root)
    if count == 0:
        return 0
    return sum_of_nodes(root) / count

# Example of usage:
def main():
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    root.left.left = Node(3)
    root.left.right = Node(7)
    root.right.left = Node(12)
    root.right.right = Node(20)

    print("1. Cây rỗng?", is_empty(root))
    print("2. Có phải nút lá?", is_leaf(root.left.left))
    print("3. Có phải nút cha của nút m?", is_parent_of(root, root.left, root.left.left))
    print("4. Chiều cao của cây:", tree_height(root))
    print("5. Số nút của cây:", count_nodes(root))
    print("6. Duyệt tiền tự:")
    preorder_traversal(root)
    print("\n7. Duyệt trung tự:")
    inorder_traversal(root)
    print("\n8. Duyệt hậu tự:")
    postorder_traversal(root)
    print("\n9. Số nút lá của cây:", count_leaf_nodes(root))
    print("10. Số nút trung gian của cây:", count_intermediate_nodes(root))
    print("11. Nút có giá trị lớn nhất:", max_node(root))
    print("12. Nút có giá trị nhỏ nhất:", min_node(root))
    print("13. Tổng giá trị các nút:", sum_of_nodes(root))
    print("14. Trung bình giá trị các nút:", average_of_nodes(root))

if __name__ == "__main__":
    main()
