class SinhVien:
    def __init__(self, masv, hoten, malop, diemtb):
        self.masv = masv
        self.hoten = hoten
        self.malop = malop
        self.diemtb = diemtb
        self.left = None
        self.right = None

class CayNhiPhanTimKiem:
    def __init__(self):
        self.root = None

    def chen(self, sinh_vien):
        if not self.root:
            self.root = sinh_vien
        else:
            self._chen_de_quy(self.root, sinh_vien)

    def _chen_de_quy(self, node, sinh_vien):
        if sinh_vien.masv < node.masv:
            if not node.left:
                node.left = sinh_vien
            else:
                self._chen_de_quy(node.left, sinh_vien)
        elif sinh_vien.masv > node.masv:
            if not node.right:
                node.right = sinh_vien
            else:
                self._chen_de_quy(node.right, sinh_vien)
        else:
            print("MASV đã tồn tại trong cây. Vui lòng nhập lại.")

    def duyet_theo_thu_tu_LNR(self, node):
        if node:
            self.duyet_theo_thu_tu_LNR(node.left)
            print("MASV:", node.masv)
            print("Họ tên:", node.hoten)
            print("Mã lớp:", node.malop)
            print("Điểm TB:", node.diemtb)
            print("---------------------------")
            self.duyet_theo_thu_tu_LNR(node.right)

    def tim_kiem(self, masv):
        return self._tim_kiem_de_quy(self.root, masv)

    def _tim_kiem_de_quy(self, node, masv):
        if not node or node.masv == masv:
            return node
        if masv < node.masv:
            return self._tim_kiem_de_quy(node.left, masv)
        return self._tim_kiem_de_quy(node.right, masv)

def nhap_du_lieu_cay():
    cay = CayNhiPhanTimKiem()
    n = int(input("Nhập số lượng sinh viên: "))
    for _ in range(n):
        masv = input("Nhập MASV: ")
        hoten = input("Nhập họ tên: ")
        malop = input("Nhập mã lớp: ")
        diemtb = float(input("Nhập điểm TB: "))
        sinh_vien = SinhVien(masv, hoten, malop, diemtb)
        cay.chen(sinh_vien)
    return cay

def hien_thi_menu():
    print("============== Menu ==============")
    print("1. Nhập dữ liệu cho cây")
    print("2. Duyệt và xuất dữ liệu theo thứ tự LNR")
    print("3. Tìm kiếm sinh viên theo MASV")
    print("4. Thoát")

if __name__ == "__main__":
    cay_sv = None
    while True:
        hien_thi_menu()
        lua_chon = input("Nhập lựa chọn của bạn: ")

        if lua_chon == "1":
            cay_sv = nhap_du_lieu_cay()
        elif lua_chon == "2":
            if cay_sv:
                print("Dữ liệu của cây theo thứ tự LNR:")
                cay_sv.duyet_theo_thu_tu_LNR(cay_sv.root)
            else:
                print("Cây chưa được khởi tạo. Vui lòng chọn '1' để nhập dữ liệu cho cây trước.")
        elif lua_chon == "3":
            if cay_sv:
                masv_tim_kiem = input("Nhập MASV cần tìm kiếm: ")
                sinh_vien_tim_kiem = cay_sv.tim_kiem(masv_tim_kiem)
                if sinh_vien_tim_kiem:
                    print("Thông tin sinh viên có MASV", masv_tim_kiem, ":", sinh_vien_tim_kiem.hoten, sinh_vien_tim_kiem.malop, sinh_vien_tim_kiem.diemtb)
                else:
                    print("Không tìm thấy sinh viên có MASV", masv_tim_kiem)
            else:
                print("Cây chưa được khởi tạo. Vui lòng chọn '1' để nhập dữ liệu cho cây trước.")
        elif lua_chon == "4":
            print("Kết thúc chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")