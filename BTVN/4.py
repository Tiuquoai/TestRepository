class Student:
    def __init__(self, masv, hoten, malop, diemtb):
        self.masv = masv
        self.hoten = hoten
        self.malop = malop
        self.diemtb = diemtb
        self.left = None
        self.right = None

# Hàm chèn một sinh viên vào cây
def insert_student(root, student):
    if root is None:
        return student
    if student.masv < root.masv:
        root.left = insert_student(root.left, student)
    elif student.masv > root.masv:
        root.right = insert_student(root.right, student)
    else:
        print("Mã sinh viên", student.masv, "đã tồn tại trong cây. Vui lòng nhập mã sinh viên khác.")
    return root

# Hàm nhập thông tin sinh viên
def input_student():
    masv = input("Nhập mã sinh viên: ")
    hoten = input("Nhập họ tên: ")
    malop = input("Nhập mã lớp: ")
    diemtb = float(input("Nhập điểm trung bình: "))
    return Student(masv, hoten, malop, diemtb)

# Hàm nhập danh sách sinh viên
def input_student_list():
    n = int(input("Nhập số lượng sinh viên bạn muốn nhập: "))
    students = []
    for i in range(n):
        print(f"\nNhập thông tin cho sinh viên thứ {i+1}:")
        student = input_student()
        students.append(student)
    return students

# Hàm duyệt và xuất dữ liệu theo thứ tự LNR
def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print("Mã SV:", root.masv, "| Họ tên:", root.hoten, "| Mã lớp:", root.malop, "| Điểm TB:", root.diemtb)
        inorder_traversal(root.right)

# Hàm tìm node có giá trị MASV trong cây
def search_student(root, masv):
    if root is None or root.masv == masv:
        return root
    if masv < root.masv:
        return search_student(root.left, masv)
    return search_student(root.right, masv)

# Hàm xóa một node có giá trị MASV từ cây
def delete_student(root, masv):
    if root is None:
        return root
    if masv < root.masv:
        root.left = delete_student(root.left, masv)
    elif masv > root.masv:
        root.right = delete_student(root.right, masv)
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
        root.masv = temp.masv
        root.right = delete_student(root.right, temp.masv)
    return root

def minValueNode(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

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

# Hàm sắp xếp cây theo trường dữ liệu MASV
def sort_tree_by_masv(root):
    if root is not None:
        sort_tree_by_masv(root.left)
        print("Mã SV:", root.masv, "| Họ tên:", root.hoten, "| Mã lớp:", root.malop, "| Điểm TB:", root.diemtb)
        sort_tree_by_masv(root.right)

# Hàm hiển thị menu
def display_menu():
    print("\n1. Nhập dữ liệu cho cây")
    print("2. Duyệt và xuất dữ liệu theo thứ tự LNR")
    print("3. Sắp xếp cây theo trường dữ liệu MASV")
    print("4. Đếm số nút lá của cây")
    print("5. Tính chiều cao của cây")
    print("6. Chèn một Node vào cây")
    print("7. Tìm kiếm một Node có giá trị MASV")
    print("8. Xóa một Node có MASV")
    print("9. Thoát")

# Hàm main
def main():
    root = None

    while True:
        display_menu()
        choice = int(input("\nNhập lựa chọn của bạn: "))

        if choice == 1:
            students = input_student_list()
            for student in students:
                root = insert_student(root, student)

        elif choice == 2:
            print("Duyệt và xuất dữ liệu theo thứ tự LNR:")
            inorder_traversal(root)

        elif choice == 3:
            print("Sắp xếp cây theo trường dữ liệu MASV:")
            sort_tree_by_masv(root)

        elif choice == 4:
            leaf_count = count_leaf_nodes(root)
            print("Số nút lá của cây là:", leaf_count)

        elif choice == 5:
            height = tree_height(root)
            print("Chiều cao của cây là:", height)

        elif choice == 6:
            student = input_student()
            root = insert_student(root, student)

        elif choice == 7:
            masv = input("Nhập mã sinh viên cần tìm: ")
            result = search_student(root, masv)
            if result:
                print("Thông tin sinh viên có mã", masv, ":", result.masv, result.hoten, result.malop, result.diemtb)
            else:
                print("Không tìm thấy sinh viên có mã", masv)

        elif choice == 8:
            masv = input("Nhập mã sinh viên cần xóa: ")
            root = delete_student(root, masv)
            print("Sinh viên có mã", masv, "đã được xóa khỏi cây.")

        elif choice == 9:
            print("Kết thúc chương trình.")
            break

        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

if __name__ == "__main__":
    main()
