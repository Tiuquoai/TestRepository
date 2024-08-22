class SinhVien:
    def __init__(self, mssv, ten):
        self.mssv = mssv
        self.ten = ten
        self.next = None
        self.prev = None

class DanhSachSinhVien:
    def __init__(self):
        self.head = None
        self.tail = None

    def them_sinh_vien(self, mssv, ten):
        new_sv = SinhVien(mssv, ten)
        if self.head is None:
            self.head = new_sv
            self.tail = new_sv
        else:
            new_sv.prev = self.tail
            self.tail.next = new_sv
            self.tail = new_sv

    def xuat_danh_sach(self):
        current = self.head
        while current:
            print(f"MSSV: {current.mssv}, Tên: {current.ten}")
            current = current.next

    def xoa_sinh_vien(self, mssv):
        current = self.head
        while current:
            if current.mssv == mssv:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                return
            current = current.next
        print("Không tìm thấy sinh viên có MSSV này.")

    def sua_sinh_vien(self, mssv, ten_moi):
        current = self.head
        while current:
            if current.mssv == mssv:
                current.ten = ten_moi
                return
            current = current.next
        print("Không tìm thấy sinh viên có MSSV này.")

    def tim_sinh_vien(self, mssv):
        current = self.head
        while current:
            if current.mssv == mssv:
                print(f"Sinh viên có MSSV {mssv} là: {current.ten}")
                return
            current = current.next
        print("Không tìm thấy sinh viên có MSSV này.")

    def sap_xep(self):
        current = self.head
        while current:
            temp = current.next
            while temp:
                if current.mssv > temp.mssv:
                    current.mssv, temp.mssv = temp.mssv, current.mssv
                    current.ten, temp.ten = temp.ten, current.ten
                temp = temp.next
            current = current.next

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
            print("\nDanh sách sinh viên:")
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
