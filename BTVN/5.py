class Node:
    def __init__(self, char):
        self.char = char
        self.count = 1
        self.left = None
        self.right = None

def insert(root, char):
    if root is None:
        return Node(char)
    if char == root.char:
        root.count += 1
    elif char < root.char:
        root.left = insert(root.left, char)
    else:
        root.right = insert(root.right, char)
    return root

def build_char_count_tree(text):
    root = None
    for char in text:
        if char.isalpha():  
            root = insert(root, char.lower())  
    return root

def count_occurrences(root, char):
    if root is None:
        return 0
    if char == root.char:
        return root.count
    elif char < root.char:
        return count_occurrences(root.left, char)
    else:
        return count_occurrences(root.right, char)

text = input("Nhập văn bản: ")

tree = build_char_count_tree(text)

char_to_check = input("Nhập ký tự cần kiểm tra: ")

occurrences = count_occurrences(tree, char_to_check.lower())

print(f"Số lần xuất hiện của '{char_to_check}': {occurrences}")