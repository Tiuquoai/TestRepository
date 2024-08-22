class Node:
    def __init__(self, value):
        self.value = value
        self.count = 1
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return Node(value)
    if value == root.value:
        root.count += 1
    elif value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

def build_unique_value_tree(values):
    root = None
    for value in values:
        root = insert(root, value)
    return root

def count_unique_values(root):
    if root is None:
        return 0
    return 1 + count_unique_values(root.left) + count_unique_values(root.right)

def count_element_occurrences(root, value):
    if root is None:
        return 0
    if value == root.value:
        return root.count
    elif value < root.value:
        return count_element_occurrences(root.left, value)
    else:
        return count_element_occurrences(root.right, value)

def count_distinct_values_and_occurrences(values):
    value_tree = build_unique_value_tree(values)
    distinct_values_count = count_unique_values(value_tree)
    result = {}
    for value in values:
        result[value] = count_element_occurrences(value_tree, value)
    return distinct_values_count, result

values = list(map(int, input("Nhập dãy số, cách nhau bằng dấu cách: ").split()))

distinct_count, occurrences = count_distinct_values_and_occurrences(values)

print("Số giá trị phân biệt trong dãy số là:", distinct_count)
print("Số lượng phần tử cho mỗi giá trị:")
for value, count in occurrences.items():
    print(f"{value}: {count}")
