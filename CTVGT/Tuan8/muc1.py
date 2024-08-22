class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert_recursively(self.root, value)

    def _insert_recursively(self, node, value):
        if value < node.value:
            if node.left:
                self._insert_recursively(node.left, value)
            else:
                node.left = TreeNode(value)
        elif value >= node.value:
            if node.right:
                self._insert_recursively(node.right, value)
            else:
                node.right = TreeNode(value)

    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.value, end=" ")
            self.inorder_traversal(node.right)

# Dãy số cho trước
numbers = [55, 26, 37, 10, 28, 39, 60, 13, 21, 65, 45, 72, 30, 85, 13, 69]

# Khởi tạo cây tìm kiếm nhị phân
bst = BinarySearchTree()

# Chèn các phần tử từ dãy số vào cây
for number in numbers:
    bst.insert(number)

# In ra kết quả biểu diễn cây TKNP (theo thứ tự LNR)
print("Cây TKNP sau khi biểu diễn từ dãy số:")
bst.inorder_traversal(bst.root)
