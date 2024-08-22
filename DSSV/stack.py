class SinhVien:
    def __init__(self, mssv, ten):
        self.mssv = mssv
        self.ten = ten

class DanhSachSinhVien:
    def __init__(self):
        self.stack = []

    def them_sinh_vien(self, mssv, ten):
        sv = SinhVien(mssv, ten)
        self.stack.append(sv)

    def xuat_danh_sach(self):
        if not self.stack:
            print("Danh sách sinh viên trống.")
        else:
            print("Danh sách sinh viên:")
            for sv in reversed(self.stack):
                print(f"MSSV: {sv.mssv}, Tên: {sv.ten}")

    def xoa_sinh_vien(self, mssv):
        for sv in self.stack:
            if sv.mssv == mssv:
                self.stack.remove(sv)
                print(f"Đã xóa sinh viên có MSSV {mssv}.")
                return
        print("Không tìm thấy sinh viên có MSSV này.")

    def sua_sinh_vien(self, mssv, ten_moi):
        for sv in self.stack:
            if sv.mssv == mssv:
                sv.ten = ten_moi
                print(f"Đã sửa thông tin sinh viên có MSSV {mssv}.")
                return
        print("Không tìm thấy sinh viên có MSSV này.")

    def tim_sinh_vien(self, mssv):
        for sv in self.stack:
            if sv.mssv == mssv:
                print(f"Sinh viên có MSSV {mssv} là: {sv.ten}")
                return
        print("Không tìm thấy sinh viên có MSSV này.")

    def sap_xep(self):
        self.stack.sort(key=lambda sv: sv.mssv)

# Hàm main
def main():
    danh_sach = DanhSachSinhVien()

    while True:
        print("\nMENU:")
        print("1. Hiển thị danh sách sinh viên")
        print("2. Thêm sinh viên")
        print("3. Xóa sinh viên")
        print("4. Sửa thông tin sinh viên")
        print("5. Tìm sinh viên")
        print("6. Sắp xếp danh sách sinh viên")
        print("7. Thoát")

        lua_chon = input("Nhập lựa chọn của bạn: ")

        if lua_chon == '1':
            danh_sach.xuat_danh_sach()
        elif lua_chon == '2':
            mssv = input("Nhập MSSV: ")
            ten = input("Nhập tên: ")
            danh_sach.them_sinh_vien(mssv, ten)
        elif lua_chon == '3':
            mssv = input("Nhập MSSV của sinh viên cần xóa: ")
            danh_sach.xoa_sinh_vien(mssv)
        elif lua_chon == '4':
            mssv = input("Nhập MSSV của sinh viên cần sửa: ")
            ten_moi = input("Nhập tên mới: ")
            danh_sach.sua_sinh_vien(mssv, ten_moi)
        elif lua_chon == '5':
            mssv = input("Nhập MSSV của sinh viên cần tìm: ")
            danh_sach.tim_sinh_vien(mssv)
        elif lua_chon == '6':
            danh_sach.sap_xep()
            print("Danh sách sinh viên đã được sắp xếp.")
        elif lua_chon == '7':
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Hãy thử lại.")

if __name__ == "__main__":
    main()
