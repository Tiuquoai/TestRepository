class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def is_empty(root):
    return root is None

def is_leaf(node):
    return node.left is None and node.right is None if node else None

def is_parent(root, node):
    if not root:
        return False
    if root.left == node or root.right == node:
        return True
    return is_parent(root.left, node) or is_parent(root.right, node)

def height(root):
    if not root:
        return 0
    return max(height(root.left), height(root.right)) + 1

def count_nodes(root):
    if not root:
        return 0
    return count_nodes(root.left) + count_nodes(root.right) + 1

def in_order_traversal(root):
    if root:
        in_order_traversal(root.left)
        print(root.data, end=" ")
        in_order_traversal(root.right)

def pre_order_traversal(root):
    if root:
        print(root.data, end=" ")
        pre_order_traversal(root.left)
        pre_order_traversal(root.right)

def post_order_traversal(root):
    if root:
        post_order_traversal(root.left)
        post_order_traversal(root.right)
        print(root.data, end=" ")

def count_leaves(root):
    if not root:
        return 0
    if is_leaf(root):
        return 1
    return count_leaves(root.left) + count_leaves(root.right)

def count_internal_nodes(root):
    if not root or is_leaf(root):
        return 0
    return 1 + count_internal_nodes(root.left) + count_internal_nodes(root.right)

def find_max_value(root):
    if not root:
        return float('-inf')
    return max(root.data, find_max_value(root.left), find_max_value(root.right))

def find_min_value(root):
    if not root:
        return float('inf')
    return min(root.data, find_min_value(root.left), find_min_value(root.right))

def sum_of_values(root):
    if not root:
        return 0
    return root.data + sum_of_values(root.left) + sum_of_values(root.right)

def average_value(root):
    return sum_of_values(root) / count_nodes(root)

def main():
    root = None

    print("1. Kiểm tra cây rỗng:")
    print("Cây rỗng" if is_empty(root) else "Cây không rỗng")

    print("\n2. Kiểm tra nút có phải là nút lá không:")
    print("Không thể kiểm tra nút lá vì cây đang rỗng." if is_empty(root) else "Có" if is_leaf(root) else "Không")

    print("\n3. Kiểm tra nút có phải là nút cha của nút m không:")
    print("Không thể kiểm tra nút cha vì cây đang rỗng." if is_empty(root) else "Có" if is_parent(root, root.left) else "Không")

    print("\n4. Chiều cao của cây:", height(root))

    print("\n5. Số nút của cây:", count_nodes(root))

    print("\n6. Duyệt tiền tự:")
    pre_order_traversal(root)
    print("\nDuyệt trung tự:")
    in_order_traversal(root)
    print("\nDuyệt hậu tự:")
    post_order_traversal(root)

    print("\n\n7. Số nút lá của cây:", count_leaves(root))

    print("\n8. Số nút trung gian của cây:", count_internal_nodes(root))

    print("\n9. Nút có giá trị lớn nhất:", find_max_value(root))
    print("   Nút có giá trị nhỏ nhất:", find_min_value(root))
    print("   Tổng giá trị các nút:", sum_of_values(root))
    print("   Trung bình giá trị các nút:", average_value(root))

if __name__ == "__main__":
    main()
