class Vemaybay:
    def __init__(self, ma_ve, ten_hanh_khach, tuoi_hanh_khach, gia_ve):
        self.ma_ve = ma_ve
        self.ten_hanh_khach = ten_hanh_khach
        self.tuoi_hanh_khach = tuoi_hanh_khach
        self.gia_ve = gia_ve

    def display(self):
        print(f"Mã vé: {self.ma_ve}")
        print(f"Tên hành khách: {self.ten_hanh_khach}")
        print(f"Tuổi hành khách: {self.tuoi_hanh_khach}")
        print(f"Giá vé: {self.gia_ve}")

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

# Khai báo biến lưu trữ danh sách vé máy bay
dsVeMayBay = Queue()

while True:
    print("1. Thêm vé máy bay mới")
    print("2. Hiển thị danh sách vé máy bay")
    print("3. Xem chi tiết vé máy bay")
    print("4. Cập nhật thông tin vé máy bay")
    print("5. Xóa vé máy bay")
    print("6. Hiển thị tổng số vé máy bay")
    print("7. Hiển thị tổng giá vé máy bay")
    print("Khác. Thoát chương trình")

    lua_chon_nguoi_dung = input("Nhập lựa chọn: ")

    if lua_chon_nguoi_dung == '1':
        ma_ve = input("Nhập mã vé: ")
        ten_hanh_khach = input("Nhập tên hành khách: ")
        tuoi_hanh_khach = int(input("Nhập tuổi hành khách: "))
        gia_ve = float(input("Nhập giá vé: "))
        ve_may_bay = Vemaybay(ma_ve, ten_hanh_khach, tuoi_hanh_khach, gia_ve)
        dsVeMayBay.enqueue(ve_may_bay)
        print('Đã thêm mới vé máy bay thành công.')
    elif lua_chon_nguoi_dung == '2':
        if dsVeMayBay.is_empty():
            print('Danh sách vé máy bay trống.')
        else:
            for item in dsVeMayBay.items:
                item.display()
    elif lua_chon_nguoi_dung == '3':
        if dsVeMayBay.is_empty():
            print('Danh sách vé máy bay trống.')
        else:
            ma_ve = input("Nhập mã vé cần xem chi tiết:")
            for item in dsVeMayBay.items:
                if item.ma_ve == ma_ve:
                    item.display()
    elif lua_chon_nguoi_dung == '4':
        if dsVeMayBay.is_empty():
            print('Danh sách vé máy bay trống.')
        else:
            ma_ve = input("Nhập mã vé cần cập nhật:")
            for item in dsVeMayBay.items:
                if item.ma_ve == ma_ve:
                    item.display()
                    print("Cập nhật thông tin vé máy bay...")
                    ten_hanh_khach = input("Nhập tên hành khách: ")
                    tuoi_hanh_khach = int(input("Nhập tuổi hành khách: "))
                    gia_ve = float(input("Nhập giá vé: "))
                    item.ten_hanh_khach = ten_hanh_khach
                    item.tuoi_hanh_khach = tuoi_hanh_khach
                    item.gia_ve = gia_ve
                    item.display()
                    break
    elif lua_chon_nguoi_dung == '5':
        if dsVeMayBay.is_empty():
            print('Danh sách vé máy bay trống.')
        else:
            ma_ve = input("Nhập mã vé cần xóa:")
            for item in dsVeMayBay.items:
                if item.ma_ve == ma_ve:
                    item.display()
                    tl = input('Bạn có chắc chắn muốn xóa vé máy bay này không? (Y/N)')
                    if tl.upper() == 'Y':
                        dsVeMayBay.items.remove(item)
                        print('Xóa thành công!')
                        break
                    else:
                        print('Hủy bỏ xóa vé máy bay.')
                        break
    elif lua_chon_nguoi_dung == '6':
        if dsVeMayBay.is_empty():
            print('Danh sách vé máy bay trống.')
        else:
            tong_so_ve = len(dsVeMayBay.items)
            print(f'Tổng số vé máy bay: {tong_so_ve}')
    elif lua_chon_nguoi_dung == '7':
        if dsVeMayBay.is_empty():
            print('Danh sách vé máy bay trống.')
        else:
            tong_gia_ve = sum(item.gia_ve for item in dsVeMayBay.items)
            print(f'Tổng giá vé máy bay: {tong_gia_ve} VND')
    else:
        print('THOÁT CHƯƠNG TRÌNH')
        break
