import matplotlib_inline as plt

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

# Menu quản lý vé máy bay
menu_options = {
    1: 'Thêm vé máy bay mới',
    2: 'Hiển thị danh sách vé máy bay',
    3: 'Xem chi tiết vé máy bay',
    4: 'Cập nhật thông tin vé máy bay',
    5: 'Xóa vé máy bay',
    6: 'Hiển thị tổng số vé máy bay',
    7: 'Hiển thị tổng giá vé máy bay',
    'Khác': 'Thoát chương trình'
}

def in_menu():
    for key in menu_options.keys():
        print(key, '--', menu_options[key])

# Khai báo biến lưu trữ danh sách vé máy bay
dsVeMayBay = []

while True:
    in_menu()
    lua_chon_nguoi_dung = ''
    try:
        lua_chon_nguoi_dung = int(input('Nhập lựa chọn: '))
    except:
        print('Lựa chọn không hợp lệ, hãy thử lại')
        continue

    # Kiểm tra lựa chọn và thực hiện hành động tương ứng
    if lua_chon_nguoi_dung == 1:
        ma_ve = input("Nhập mã vé: ")
        ten_hanh_khach = input("Nhập tên hành khách: ")
        tuoi_hanh_khach = int(input("Nhập tuổi hành khách: "))
        gia_ve = float(input("Nhập giá vé: "))
        ve_may_bay = Vemaybay(ma_ve, ten_hanh_khach, tuoi_hanh_khach, gia_ve)
        dsVeMayBay.append(ve_may_bay)
        print('Đã thêm mới vé máy bay thành công.')
    elif lua_chon_nguoi_dung == 2:
        if not dsVeMayBay:
            print('Danh sách vé máy bay trống.')
        else:
            for item in dsVeMayBay:
                item.display()
    elif lua_chon_nguoi_dung == 3:
        # Xem chi tiết vé máy bay
        if not dsVeMayBay:
            print('Danh sách vé máy bay trống.')
        else:
            ma_ve = input("Nhập mã vé cần xem chi tiết:")
            for item in dsVeMayBay:
                if item.ma_ve == ma_ve:
                    item.display()
    elif lua_chon_nguoi_dung == 4:
        # Cập nhật thông tin vé máy bay
        if not dsVeMayBay:
            print('Danh sách vé máy bay trống.')
        else:
            ma_ve = input("Nhập mã vé cần cập nhật:")
            for item in dsVeMayBay:
                if item.ma_ve == ma_ve:
                    item.display()
                    menu = {
                        1: 'Cập nhật tên hành khách',
                        2: 'Cập nhật tuổi hành khách',
                        3: 'Cập nhật giá vé',
                        'Khác': 'Thoát'
                    }
                    def xuat_menu():
                        for key in menu.keys():
                            print(key, '--', menu[key])

                    while True:
                        xuat_menu()
                        traloi = ''
                        try:
                            traloi = int(input('Nhập lựa chọn: '))
                        except:
                            print('Nhập sai định dạng, nhập lại:')
                            continue
                        if traloi == 1:
                            ten_hanh_khach = input("Nhập tên hành khách: ")
                            item.ten_hanh_khach = ten_hanh_khach
                            item.display()
                        elif traloi == 2:
                            tuoi_hanh_khach = int(input("Nhập tuổi hành khách: "))
                            item.tuoi_hanh_khach = tuoi_hanh_khach
                            item.display()
                        elif traloi == 3:
                            gia_ve = float(input("Nhập giá vé: "))
                            item.gia_ve = gia_ve
                            item.display()
                        else:
                            print('Kết thúc cập nhật')
                            break
    elif lua_chon_nguoi_dung == 5:
        # Xóa vé máy bay
        if not dsVeMayBay:
            print('Danh sách vé máy bay trống.')
        else:
            ma_ve = input("Nhập mã vé cần xóa:")
            for item in dsVeMayBay:
                if item.ma_ve == ma_ve:
                    item.display()
                    tl = input('Bạn có chắc chắn muốn xóa vé máy bay này không? (Y/N)')
                    if tl.upper() == 'Y':
                        dsVeMayBay.remove(item)
                        print('Xóa thành công!')
                        break
                    else:
                        print('Hủy bỏ xóa vé máy bay.')
                        break
    elif lua_chon_nguoi_dung == 6:
        # Hiển thị tổng số vé máy bay
        if not dsVeMayBay:
            print('Danh sách vé máy bay trống.')
        else:
            tong_so_ve = len(dsVeMayBay)
            print(f'Tổng số vé máy bay: {tong_so_ve}')
    elif lua_chon_nguoi_dung == 7:
        # Hiển thị tổng giá vé máy bay
        if not dsVeMayBay:
            print('Danh sách vé máy bay trống.')
        else:
            tong_gia_ve = sum(item.gia_ve for item in dsVeMayBay)
            print(f'Tổng giá vé máy bay: {tong_gia_ve} VND')
    else:
        print('THOÁT CHƯƠNG TRÌNH')
        break
