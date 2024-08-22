class Node:
    def __init__(self, masv, data):
        self.masv = masv
        self.data = data
        self.left = None
        self.right = None

def chen_node(root, masv, data):
    if root is None:
        return Node(masv, data)
    if masv < root.masv:
        root.left = chen_node(root.left, masv, data)
    elif masv > root.masv:
        root.right = chen_node(root.right, masv, data)
    else:
        print("Mã sinh viên đã tồn tại, vui lòng nhập lại mã sinh viên khác.")
    return root

def duyet_LNR(root):
    if root:
        duyet_LNR(root.left)
        print(f"Mã sinh viên: {root.masv}, Dữ liệu: {root.data}")
        duyet_LNR(root.right)

def sap_xep_cay(root):
    if root is None:
        return
    sap_xep_cay(root.left)
    sap_xep_cay(root.right)
    root = chen_node(root, root.masv, root.data)

def dem_so_nut_la(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    return dem_so_nut_la(root.left) + dem_so_nut_la(root.right)

def chieu_cao_cay(root):
    if root is None:
        return 0
    return 1 + max(chieu_cao_cay(root.left), chieu_cao_cay(root.right))

def tim_kiem_node(root, masv):
    if root is None or root.masv == masv:
        return root
    if root.masv < masv:
        return tim_kiem_node(root.right, masv)
    return tim_kiem_node(root.left, masv)

def tim_node_the_mang(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def xoa_node(root, masv):
    if root is None:
        return root
    if masv < root.masv:
        root.left = xoa_node(root.left, masv)
    elif masv > root.masv:
        root.right = xoa_node(root.right, masv)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        temp = tim_node_the_mang(root.right)
        root.masv = temp.masv
        root.data = temp.data
        root.right = xoa_node(root.right, temp.masv)
    return root

def nhap_du_lieu_cay():
    root = None
    while True:
        masv = input("Nhập mã sinh viên: ")
        data = input("Nhập dữ liệu: ")
        root = chen_node(root, masv, data)
        tiep_tuc = input("Bạn muốn nhập tiếp không? (Y/N): ")
        if tiep_tuc.upper() != 'Y':
            break
    return root

if __name__ == "__main__":
    root = nhap_du_lieu_cay()

    print("\nDanh sách sinh viên sau khi nhập:")
    duyet_LNR(root)

    sap_xep_cay(root)
    print("\nDanh sách sinh viên sau khi sắp xếp:")
    duyet_LNR(root)

    print(f"\nSố nút lá của cây: {dem_so_nut_la(root)}")
    print(f"Chiều cao của cây: {chieu_cao_cay(root)}")

    masv_tim_kiem = input("\nNhập mã sinh viên cần tìm kiếm: ")
    ket_qua_tim_kiem = tim_kiem_node(root, masv_tim_kiem)
    if ket_qua_tim_kiem:
        print(f"Thông tin sinh viên có mã {masv_tim_kiem}: {ket_qua_tim_kiem.masv}, {ket_qua_tim_kiem.data}")
    else:
        print("Không tìm thấy sinh viên có mã tương ứng.")

    masv_xoa = input("\nNhập mã sinh viên cần xóa: ")
    root = xoa_node(root, masv_xoa)
    print("\nDanh sách sinh viên sau khi xóa:")
    duyet_LNR(root)
