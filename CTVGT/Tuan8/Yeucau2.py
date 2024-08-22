class SinhVien:
    def __init__(self, masv, hoten, diem):
        self.masv = masv
        self.hoten = hoten
        self.diem = diem
        self.left = None
        self.right = None

class QuanLySinhVien:
    def __init__(self):
        self.root = None

    def chen_sinh_vien(self, masv, hoten, diem):
        if self.root is None:
            self.root = SinhVien(masv, hoten, diem)
            print("Thêm sinh viên thành công!")
        else:
            if self.tim_sinh_vien(self.root, masv) is not None:
                print("Mã sinh viên đã tồn tại! Vui lòng nhập lại.")
            else:
                self._chen_sinh_vien(self.root, masv, hoten, diem)
                print("Thêm sinh viên thành công!")

    def _chen_sinh_vien(self, node, masv, hoten, diem):
        if masv < node.masv:
            if node.left is None:
                node.left = SinhVien(masv, hoten, diem)
            else:
                self._chen_sinh_vien(node.left, masv, hoten, diem)
        else:
            if node.right is None:
                node.right = SinhVien(masv, hoten, diem)
            else:
                self._chen_sinh_vien(node.right, masv, hoten, diem)

    def tim_sinh_vien(self, node, masv):
        if node is None or node.masv == masv:
            return node
        if masv < node.masv:
            return self.tim_sinh_vien(node.left, masv)
        return self.tim_sinh_vien(node.right, masv)

    def _duyet_LNR(self, node):
        if node:
            self._duyet_LNR(node.left)
            print("Mã SV:", node.masv, ", Họ tên:", node.hoten, ", Điểm:", node.diem)
            self._duyet_LNR(node.right)

    def duyet_LNR(self):
        if self.root is None:
            print("Cây sinh viên đang trống!")
        else:
            print("Danh sách sinh viên theo thứ tự LNR:")
            self._duyet_LNR(self.root)

# Hàm main để kiểm tra các chức năng
def main():
    qlsv = QuanLySinhVien()
    
    # Thêm sinh viên vào cây
    qlsv.chen_sinh_vien("SV001", "Vo Thuong Hoai", 10)
    qlsv.chen_sinh_vien("SV002", "Anh Thien Tran", 9.9)
    qlsv.chen_sinh_vien("SV003", "Le Thi Linh", 7)
    qlsv.chen_sinh_vien("SV004", "Tran P Minh Chau", 9.2)

    # Duyệt và xuất dữ liệu của cây theo thứ tự LNR
    qlsv.duyet_LNR()

if __name__ == "__main__":
    main()
