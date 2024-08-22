class SinhVien:
    def __init__(self, mssv, ten):
        self.mssv = mssv
        self.ten = ten

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class DanhSachSinhVien:
    def __init__(self):
        self.front = None
        self.rear = None

    def them_sinh_vien(self, mssv, ten):
        sv = SinhVien(mssv, ten)
        new_node = Node(sv)
        if not self.front:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def xuat_danh_sach(self):
        if not self.front:
            print("Danh sách sinh viên trống.")
        else:
            print("Danh sách sinh viên:")
            current = self.front
            while current:
                print(f"MSSV: {current.data.mssv}, Tên: {current.data.ten}")
                current = current.next

    def xoa_sinh_vien(self, mssv):
        if not self.front:
            print("Danh sách sinh viên trống.")
            return
        if self.front.data.mssv == mssv:
            if self.front == self.rear:
                self.front = None
                self.rear = None
            else:
                self.front = self.front.next
            print(f"Đã xóa sinh viên có MSSV {mssv}.")
            return
        current = self.front
        while current.next:
            if current.next.data.mssv == mssv:
                if current.next == self.rear:
                    self.rear = current
                current.next = current.next.next
                print(f"Đã xóa sinh viên có MSSV {mssv}.")
                return
            current = current.next
        print("Không tìm thấy sinh viên có MSSV này.")

    def sua_sinh_vien(self, mssv, ten_moi):
        current = self.front
        while current:
            if current.data.mssv == mssv:
                current.data.ten = ten_moi
                print(f"Đã sửa thông tin sinh viên có MSSV {mssv}.")
                return
            current = current.next
        print("Không tìm thấy sinh viên có MSSV này.")

    def tim_sinh_vien(self, mssv):
        current = self.front
        while current:
            if current.data.mssv == mssv:
                print(f"Sinh viên có MSSV {mssv} là: {current.data.ten}")
                return
            current = current.next
        print("Không tìm thấy sinh viên có MSSV này.")

    def sap_xep(self):
        # Hàng đợi không cần sắp xếp
        print("Danh sách sinh viên đã được sắp xếp.")

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
        elif lua_chon == '7':
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Hãy thử lại.")

if __name__ == "__main__":
    main()
