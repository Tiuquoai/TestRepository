class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class CayNhiPhanTimKiem:
    def __init__(self):
        self.root = None

    def chen(self, value):
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._chen_de_quy(self.root, value)

    def _chen_de_quy(self, node, value):
        if value < node.value:
            if not node.left:
                node.left = TreeNode(value)
            else:
                self._chen_de_quy(node.left, value)
        elif value > node.value:
            if not node.right:
                node.right = TreeNode(value)
            else:
                self._chen_de_quy(node.right, value)

    def duyet_theo_thu_tu_LNR(self, node):
        if node:
            self.duyet_theo_thu_tu_LNR(node.left)
            print(node.value, end=" ")
            self.duyet_theo_thu_tu_LNR(node.right)

    def duyet_theo_thu_tu_NLR(self, node):
        if node:
            print(node.value, end=" ")
            self.duyet_theo_thu_tu_NLR(node.left)
            self.duyet_theo_thu_tu_NLR(node.right)

    def dem_so_nut_la(self, node):
        if not node:
            return 0
        if not node.left and not node.right:
            return 1
        return self.dem_so_nut_la(node.left) + self.dem_so_nut_la(node.right)

    def chieu_cao(self, node):
        if not node:
            return 0
        return 1 + max(self.chieu_cao(node.left), self.chieu_cao(node.right))

    def tim_kiem(self, value):
        return self._tim_kiem_de_quy(self.root, value)

    def _tim_kiem_de_quy(self, node, value):
        if not node or node.value == value:
            return node
        if value < node.value:
            return self._tim_kiem_de_quy(node.left, value)
        return self._tim_kiem_de_quy(node.right, value)

    def xoa(self, value):
        self.root = self._xoa_de_quy(self.root, value)

    def _xoa_de_quy(self, node, value):
        if not node:
            return node

        if value < node.value:
            node.left = self._xoa_de_quy(node.left, value)
        elif value > node.value:
            node.right = self._xoa_de_quy(node.right, value)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            temp = self._tim_nut_co_gia_tri_nho_nhat(node.right)
            node.value = temp.value
            node.right = self._xoa_de_quy(node.right, temp.value)
        return node

    def _tim_nut_co_gia_tri_nho_nhat(self, node):
        current = node
        while current.left:
            current = current.left
        return current

def hien_thi_menu():
    print("==================Menu=================:")
    print("1. Khởi tạo cây nhị phân tìm kiếm")
    print("2. Thêm ước số của 3 số cuối của MASV vào cây")
    print("3. Duyệt cây và xuất dữ liệu theo thứ tự LNR")
    print("4. Duyệt cây và xuất dữ liệu theo thứ tự NLR")
    print("5. Đếm số nút lá của cây")
    print("6. Tính chiều cao của cây")
    print("7. Tìm kiếm một nút")
    print("8. Xóa một nút")
    print("9. Thoát")
    
if __name__ == "__main__":
    cay = CayNhiPhanTimKiem()
    while True:
        hien_thi_menu()
        lua_chon = input("Nhập lựa chọn của bạn: ")
        
        if lua_chon == "1":
            values = [10, 12, 9, 8, 29]  # Các giá trị mẫu cho cây
            for value in values:
                cay.chen(value)
            print("Cây nhị phân tìm kiếm đã được khởi tạo với các giá trị:", values)
        elif lua_chon == "2":
            masv = input("Nhập mã số sinh viên (MASV): ")
            last_three_digits = masv[-3:]
            try:
                last_three_digits = int(last_three_digits)
            except ValueError:
                print("MASV phải có ít nhất 3 chữ số cuối là số.")
                continue
            factors = [i for i in range(1, last_three_digits + 1) if last_three_digits % i == 0]
            factor = factors[-3]
            cay.chen(factor)
            print("Đã thêm ước số của 3 số cuối của MASV vào cây.")
        elif lua_chon == "3":
            print("Dữ liệu của cây theo thứ tự LNR:")
            cay.duyet_theo_thu_tu_LNR(cay.root)
            print()
        elif lua_chon == "4":
            print("Dữ liệu của cây theo thứ tự NLR:")
            cay.duyet_theo_thu_tu_NLR(cay.root)
            print()
        elif lua_chon == "5":
            print("Số nút lá của cây:", cay.dem_so_nut_la(cay.root))
        elif lua_chon == "6":
            print("Chiều cao của cây:", cay.chieu_cao(cay.root))
        elif lua_chon == "7":
            value = int(input("Nhập giá trị muốn tìm kiếm trong cây: "))
            if cay.tim_kiem(value):
                print("Giá trị", value, "được tìm thấy trong cây.")
            else:
                print("Giá trị", value, "không tồn tại trong cây.")
        elif lua_chon == "8":
            value = int(input("Nhập giá trị muốn xóa khỏi cây: "))
            cay.xoa(value)
            print("Đã xóa giá trị", value, "khỏi cây.")
        elif lua_chon == "9":
            print("Chương trình kết thúc.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")
   