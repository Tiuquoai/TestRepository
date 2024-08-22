import matplotlib_inline as plt 

class Vetau:
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

# Menu quản lý vé tàu
menu_options = {
    1: 'Thêm vé tàu mới',
    2: 'Hiển thị danh sách vé tàu',
    3: 'Xem chi tiết vé tàu',
    4: 'Cập nhật thông tin vé tàu',
    5: 'Xóa vé tàu',
    6: 'Hiển thị tổng số vé tàu',
    7: 'Hiển thị tổng giá vé tàu',
    8: 'Thêm 1 phần tử vào danh sách',
    9: 'Xuất danh sách các phần tử',
    10: 'Tìm phần tử theo khóa chính',
    11: 'Sắp xếp danh sách theo khóa chính',
    12: 'Xóa phần tử khỏi danh sách',
    13: 'Khởi tạo Queue và thống kê phần tử chia hết cho 2',
    'Khác': 'Thoát chương trình'
}

def in_menu():
    for key in menu_options.keys():
        print(key, '--', menu_options[key])

# Khai báo biến lưu trữ danh sách vé tàu
dsVeTau = []

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

    def size(self):
        return len(self.items)

def thong_ke_chia_het_cho_hai(ds_ve_tau):
    queue = Queue()
    for ve_tau in ds_ve_tau:
        if int(ve_tau.ma_ve) % 2 == 0:
            queue.enqueue(ve_tau)
    print("Danh sách các vé tàu có mã chia hết cho 2:")
    while not queue.is_empty():
        queue.dequeue().display()

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
        ve_tau = Vetau(ma_ve, ten_hanh_khach, tuoi_hanh_khach, gia_ve)
        dsVeTau.append(ve_tau)
        print('Đã thêm mới vé tàu thành công.')
    elif lua_chon_nguoi_dung == 2:
        if not dsVeTau:
            print('Danh sách vé tàu trống.')
        else:
            for item in dsVeTau:
                item.display()
    elif lua_chon_nguoi_dung == 3:
        # Xem chi tiết vé tàu
        if not dsVeTau:
            print('Danh sách vé tàu trống.')
        else:
            ma_ve = input("Nhập mã vé cần xem chi tiết:")
            for item in dsVeTau:
                if item.ma_ve == ma_ve:
                    item.display()
                    break
            else:
                print('Không tìm thấy vé tàu có mã số này.')
    elif lua_chon_nguoi_dung == 4:
        # Cập nhật thông tin vé tàu
        if not dsVeTau:
            print('Danh sách vé tàu trống.')
        else:
            ma_ve = input("Nhập mã vé cần cập nhật:")
            for item in dsVeTau:
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
                    break
            else:
                print('Không tìm thấy vé tàu có mã số này.')
    elif lua_chon_nguoi_dung == 5:
        # Xóa vé tàu
        if not dsVeTau:
            print('Danh sách vé tàu trống.')
        else:
            ma_ve = input("Nhập mã vé cần xóa:")
            for item in dsVeTau:
                if item.ma_ve == ma_ve:
                    item.display()
                    tl = input('Bạn có chắc chắn muốn xóa vé tàu này không? (Y/N)')
                    if tl.upper() == 'Y':
                        dsVeTau.remove(item)
                        print('Xóa thành công!')
                        break
                    else:
                        print('Hủy bỏ xóa vé tàu.')
                        break
            else:
                print('Không tìm thấy vé tàu có mã số này.')
    elif lua_chon_nguoi_dung == 6:
        # Hiển thị tổng số vé tàu
        if not dsVeTau:
            print('Danh sách vé tàu trống.')
        else:
            tong_so_ve = len(dsVeTau)
            print(f'Tổng số vé tàu: {tong_so_ve}')
    elif lua_chon_nguoi_dung == 7:
        # Hiển thị tổng giá vé tàu
        if not dsVeTau:
            print('Danh sách vé tàu trống.')
        else:
            tong_gia_ve = sum(item.gia_ve for item in dsVeTau)
            print(f'Tổng giá vé tàu: {tong_gia_ve} VND')
    elif lua_chon_nguoi_dung == 8:
        # Thêm 1 phần tử vào danh sách
        ma_ve = input("Nhập mã vé: ")
        for item in dsVeTau:
            if item.ma_ve == ma_ve:
                print('Đã có vé tàu có mã số này.')
                break
        else:
            ten_hanh_khach = input("Nhập tên hành khách: ")
            tuoi_hanh_khach = int(input("Nhập tuổi hành khách: "))
            gia_ve = float(input("Nhập giá vé: "))
            ve_tau = Vetau(ma_ve, ten_hanh_khach, tuoi_hanh_khach, gia_ve)
            dsVeTau.append(ve_tau)
            print('Đã thêm mới vé tàu thành công.')
    elif lua_chon_nguoi_dung == 9:
        # Xuất danh sách các phần tử có trong danh sách
        if not dsVeTau:
            print('Danh sách vé tàu trống.')
        else:
            for item in dsVeTau:
                item.display()
    elif lua_chon_nguoi_dung == 10:
        # Tìm phần tử theo khóa chính
        ma_ve = input("Nhập mã vé cần tìm:")
        for item in dsVeTau:
            if item.ma_ve == ma_ve:
                item.display()
                break
        else:
            print('Không tìm thấy vé tàu có mã số này.')
    elif lua_chon_nguoi_dung == 11:
        # Sắp xếp danh sách theo khóa chính
        dsVeTau.sort(key=lambda x: x.ma_ve)
        print('Đã sắp xếp danh sách theo mã vé.')
    elif lua_chon_nguoi_dung == 12:
        # Xóa phần tử khỏi danh sách
        if not dsVeTau:
            print('Danh sách vé tàu trống.')
        else:
            xoa_cach = input("Nhập 'D' để xóa đầu, 'C' để xóa cuối, hoặc nhập mã vé để xóa:")
            if xoa_cach.upper() == 'D':
                dsVeTau.pop(0)
                print('Đã xóa phần tử đầu danh sách.')
            elif xoa_cach.upper() == 'C':
                dsVeTau.pop()
                print('Đã xóa phần tử cuối danh sách.')
            else:
                ma_ve = xoa_cach
                for item in dsVeTau:
                    if item.ma_ve == ma_ve:
                        dsVeTau.remove(item)
                        print('Đã xóa phần tử có mã vé', ma_ve)
                        break
                else:
                    print('Không tìm thấy vé tàu có mã số này.')
    elif lua_chon_nguoi_dung == 13:
        # Thống kê phần tử chia hết cho 2 bằng Queue
        if not dsVeTau:
            print('Danh sách vé tàu trống.')
        else:
            thong_ke_chia_het_cho_hai(dsVeTau)
    else:
        print('THOÁT CHƯƠNG TRÌNH')
        break
