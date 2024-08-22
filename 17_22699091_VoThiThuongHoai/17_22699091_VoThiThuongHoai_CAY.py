class Node:
    def __init__(self, sTT, maDH, tenDH, thangNam, soNuocTieuThu):
        self.sTT = sTT
        self.maDH = maDH
        self.tenDH = tenDH
        self.thangNam = thangNam
        self.soNuocTieuThu = soNuocTieuThu
        self.left = None
        self.right = None

def khoi_tao_cay():
    # Hai ký tự 1 và 2 của MaSV 22
    node1 = Node("22","N01","DH A", "2023-01", 22)
    # Hai ký tự 3 và 4 của MaSV 69
    node2 = Node("69","N02", "DH B", "2023-02", 69)
    # Hai ký tự 5 và 6 của MaSV 90
    node3 = Node("90","N03","DH C", "2023-03", 90)
    # Hai ký tự 7 và 8 của MaSV 09
    node4 = Node("91","N04","DH D", "2023-04", 91)
    
    root = node1
    root.left = node2
    root.right = node3
    root.left.left = node4

    return root

def ve_cay(root, space=0, level=0):
    if root is not None:
        space += 10
        ve_cay(root.right, space, level + 1)
        print()
        for i in range(10, space):
            print(end=" ")
        print(root.soNuocTieuThu)
        ve_cay(root.left, space, level + 1)

def them_node(root, node):
    if root is None:
        return node
    if node.soNuocTieuThu < root.soNuocTieuThu:
        root.left = them_node(root.left, node)
    else:
        root.right = them_node(root.right, node)
    return root

def duyet_NLR(root):
    if root:
        print(root.soNuocTieuThu, end=" ")
        duyet_NLR(root.left)
        duyet_NLR(root.right)

def duyet_LNR(root):
    if root:
        duyet_LNR(root.left)
        print(root.soNuocTieuThu, end=" ")
        duyet_LNR(root.right)

def duyet_LRN(root, condition, queue):
    if root:
        duyet_LRN(root.left, condition, queue)
        duyet_LRN(root.right, condition, queue)
        if condition(root):
            queue.append(root)

def tinh_tong_doanh_thu(root):
    if root is None:
        return 0
    don_gia = 0
    if root.soNuocTieuThu < 5:
        don_gia = 1000
    elif root.soNuocTieuThu <= 10:
        don_gia = 2000
    else:
        don_gia = 3000
    doanh_thu = root.soNuocTieuThu * don_gia
    return doanh_thu + tinh_tong_doanh_thu(root.left) + tinh_tong_doanh_thu(root.right)

def tim_node_theo_maDH(root, maDH):
    if root is None or root.maDH == maDH:
        return root
    if maDH < root.maDH:
        return tim_node_theo_maDH(root.left, maDH)
    return tim_node_theo_maDH(root.right, maDH)

def cap_nhat_node(root, maDH, soNuocTieuThu_moi):
    node = tim_node_theo_maDH(root, maDH)
    if node:
        node.soNuocTieuThu = soNuocTieuThu_moi
        return True
    return False

def xoa_node(root, soNuocTieuThu):
    if root is None:
        return root
    if soNuocTieuThu < root.soNuocTieuThu:
        root.left = xoa_node(root.left, soNuocTieuThu)
    elif soNuocTieuThu > root.soNuocTieuThu:
        root.right = xoa_node(root.right, soNuocTieuThu)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        root.soNuocTieuThu = tim_node_nho_nhat(root.right).soNuocTieuThu
        root.right = xoa_node(root.right, root.soNuocTieuThu)
    return root

def tim_node_nho_nhat(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def main():
    root = khoi_tao_cay()
    so_thu_tu_sv = 17  # số thứ tự trong danh sách là 17

    while True:
        print("\nMenu:")
        print("1. Tạo cây nhị phân tìm kiếm")
        print(f"2. Thêm node có SoNuocTieuThu là {so_thu_tu_sv}")
        print("3. Duyệt và xuất dữ liệu theo thứ tự NLR")
        print("4. Duyệt và xuất dữ liệu theo thứ tự LNR")
        print("5. Duyệt cây theo thứ tự LRN và đưa Node thoả điều kiện vào hàng đợi")
        print("6. Tính tổng doanh thu của tất cả các đồng hồ")
        print("7. Tìm kiếm một Node theo MaDH")
        print("8. Sửa thông tin số nước tiêu thụ của Node theo MaDH")
        print("9. Xoá một Node theo SoNuocTieuThu")
        print("10. Kết thúc chương trình")

        choice = int(input("Chọn một chức năng (1-10): "))

        if choice == 1:
            print("Cây nhị phân tìm kiếm sau khi đã khởi tạo:")
            ve_cay(root)
        elif choice == 2:
            node_moi = Node(str(so_thu_tu_sv), f"N{so_thu_tu_sv}", f"DH {chr(65 + so_thu_tu_sv % 26)}", "2023-05", so_thu_tu_sv)
            root = them_node(root, node_moi)
            print("Cây sau khi thêm Node mới:")
            ve_cay(root)
        elif choice == 3:
            print("Duyệt và xuất dữ liệu theo thứ tự NLR:")
            duyet_NLR(root)
            print()
        elif choice == 4:
            print("Duyệt và xuất dữ liệu theo thứ tự LNR:")
            duyet_LNR(root)
            print()
        elif choice == 5:
            condition = lambda node: node.soNuocTieuThu % 2 == 0  # Điều kiện ví dụ: số nước tiêu thụ là số chẵn
            queue = []
            duyet_LRN(root, condition, queue)
            print("Dữ liệu các Node thoả điều kiện (số nước tiêu thụ là số chẵn):")
            for node in queue:
                print(node.soNuocTieuThu, end=" ")
            print()
        elif choice == 6:
            print("Tổng doanh thu của tất cả các đồng hồ:", tinh_tong_doanh_thu(root))
        elif choice == 7:
            maDH = input("Nhập MaDH cần tìm kiếm: ")
            node = tim_node_theo_maDH(root, maDH)
            if node:
                print("Thông tin đồng hồ nước được tìm thấy:", node.maDH, node.tenDH, node.thangNam, node.soNuocTieuThu)
            else:
                print("Không tìm thấy đồng hồ nước có MaDH", maDH)
        elif choice == 8:
            maDH = input("Nhập MaDH cần sửa thông tin: ")
            node = tim_node_theo_maDH(root, maDH)
            if node:
                print("Thông tin hiện tại của đồng hồ nước:", node.maDH, node.tenDH, node.thangNam, node.soNuocTieuThu)
                cap_nhat = input("Bạn có muốn sửa lại số nước tiêu thụ không? (y/n): ")
                if cap_nhat.lower() == 'y':
                    soNuocTieuThu_moi = int(input("Nhập số nước tiêu thụ mới: "))
                    if cap_nhat_node(root, maDH, soNuocTieuThu_moi):
                        print("Cập nhật thành công.")
                    else:
                        print("Cập nhật thất bại.")
            else:
                print("Không tìm thấy đồng hồ nước có MaDH", maDH)
        elif choice == 9:
            soNuocTieuThu = int(input("Nhập giá trị của SoNuocTieuThu cần xóa: "))
            root = xoa_node(root, soNuocTieuThu)
            print("Cây sau khi xóa node có SoNuocTieuThu", soNuocTieuThu, ":")
            ve_cay(root)
        elif choice == 10:
            print("Kết thúc chương trình.")
            break
        else:
            print("Vui lòng chọn một chức năng từ 1 đến 10.")

if __name__ == "__main__":
    main()
