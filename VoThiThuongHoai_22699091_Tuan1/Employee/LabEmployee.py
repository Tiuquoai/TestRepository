import Employee as emp

import matplotlib.pyplot as plt

menu_options = {
    1: 'Tải dữ liệu từ tệp',
    2: 'Thêm nhân viên mới',
    3: 'Hiển thị danh sách nhân viên',
    4: 'Hiển thị chi tiết nhân viên',
    5: 'Cập nhật thông tin nhân viên',
    6: 'Xóa nhân viên',
    7: 'Tăng lương cho nhân viên',
    8: 'Giảm lương cho nhân viên',
    9: 'Hiển thị tổng số nhân viên',
    10: 'Hiển thị tổng lương',
    11: 'Hiển thị lương trung bình',
    12: 'Hiển thị tuổi trung bình',
    13: 'Hiển thị tuổi cao nhất',
    14: 'Sắp xếp nhân viên theo lương',
    15: 'Vẽ biểu đồ lương theo tuổi',
    16: 'Vẽ biểu đồ lương trung bình theo nhóm tuổi',
    17: 'Vẽ biểu đồ phần trăm lương theo nhóm tuổi',
    18: 'Vẽ biểu đồ phần trăm tổng số nhân viên theo nhóm tuổi',
    19: 'Lưu dữ liệu vào tệp',
    'Others': 'Thoát chương trình'
}

def print_menu():
    for key, value in menu_options.items():
        print(key, '--', value)

# Khai báo một danh sách để lưu trữ nhân viên
dsNhanVien = []

while True:
    print_menu()
    userChoice = input('Nhập lựa chọn: ')
    
    try:
        userChoice = int(userChoice)
    except ValueError:
        print('Nhập không hợp lệ, vui lòng thử lại')
        continue
    
    # Kiểm tra lựa chọn và thực hiện hành động tương ứng
    if userChoice == 1:
        fr = open('dbemp_input.db', mode='r', encoding='utf-8')
        for line in fr:
            stripLine = line.strip('\n')
            ds = stripLine.split(',')
            maso = ds[0]
            ten = ds[1]
            tuoi = int(ds[2])
            luong = float(ds[3])
            nv = emp.Employee(maso, ten, tuoi, luong)
            dsNhanVien.append(nv)
        fr.close()
    elif userChoice == 2:
        maso = input("Nhập mã số: ")
        ten = input("Nhập tên: ")
        tuoi = int(input("Nhập tuổi: "))
        luong = float(input("Nhập lương: "))
        nv = emp.Employee(maso, ten, tuoi, luong)
        dsNhanVien.append(nv)
    elif userChoice == 3:
        if len(dsNhanVien) == 0:
            print('Danh sách rỗng')
        else:
            for item in dsNhanVien:
                item.display()
    elif userChoice == 4:
        if len(dsNhanVien) == 0:
            print('Danh sách rỗng')
        else:
            ma = input("Nhập mã: ")
            for item in dsNhanVien:
                if item.code == ma:
                    item.display()
    elif userChoice == 5:
        if len(dsNhanVien) == 0:
            print('Danh sách rỗng')
        else:
            ma = input("Nhập mã để cập nhật: ")
            for item in dsNhanVien:
                if item.code == ma:
                    item.display()
                    menu = {
                        1: 'Cập nhật tên',
                        2: 'Cập nhật tuổi',
                        3: 'Cập nhật lương',
                        'Others': 'Thoát'
                    }
                    def print_update_menu():
                        for key, value in menu.items():
                            print(key, '--', value)
                    while True:
                        print_update_menu()
                        traloi = input('Nhập các tùy chọn: ')
                        try:
                            traloi = int(traloi)
                        except ValueError:
                            print('Nhập sai định dạng, vui lòng nhập lại:')
                            continue
                        if traloi == 1:
                            ten = input("Nhập tên: ")
                            item.name = ten
                            item.display()
                        elif traloi == 2:
                            tuoi = int(input("Nhập tuổi: "))
                            item.age = tuoi
                            item.display()
                        elif traloi == 3:
                            luong = float(input("Nhập lương: "))
                            item.salary = luong
                            item.display()
                        else:
                            print('Kết thúc chỉnh sửa')
                            break
    elif userChoice == 6:
        if len(dsNhanVien) == 0:
            print('Danh sách rỗng')
        else:
            ma = input("Nhập mã để xóa: ")
            for item in dsNhanVien:
                if item.code == ma:
                    item.display()
                    tl = input('Bạn có chắc chắn xóa nhân viên này không Y/N?')
                    if tl == 'Y':
                        dsNhanVien.remove(item)
            for item in dsNhanVien:
                item.display()
    elif userChoice == 7:
        if len(dsNhanVien) == 0:
            print('Danh sách rỗng')
        else:
            ma = input("Nhập mã để cập nhật: ")
            for item in dsNhanVien:
                if item.code == ma:
                    item.display()
                    luongtang = int(input('Nhập mức lương tăng: '))
                    item.salary += luongtang
                    item.display()
    elif userChoice == 8:
        if len(dsNhanVien) == 0:
            print('Danh sách rỗng')
        else:
            ma = input("Nhập mã để cập nhật: ")
            for item in dsNhanVien:
                if item.code == ma:
                    item.display()
                    luonggiam = int(input('Nhập mức lương giảm: '))
                    item.salary -= luonggiam
                    item.display()
    elif userChoice == 9:
        if len(dsNhanVien) == 0:
            print('Danh sách rỗng')
        else:
            tongsnv = len(dsNhanVien)
            for item in dsNhanVien:
                item.display()
            print('Tổng số nhân viên =', tongsnv)
    elif userChoice == 10:
        sumSalary = sum(item.salary for item in dsNhanVien)
        print(f'Tổng lương: {sumSalary}')
    elif userChoice == 11:
        if len(dsNhanVien) == 0:
            print('Danh sách rỗng')
        else:
            tongsnv = len(dsNhanVien)
            tongluong = sum(item.salary for item in dsNhanVien)
            for item in dsNhanVien:
                item.display()
            luongtb = tongluong / tongsnv
            print(f'Lương trung bình nhân viên = {luongtb}')
    elif userChoice == 12:
        if len(dsNhanVien) == 0:
            print('Danh sách rỗng')
        else:
            tongtuoi = sum(item.age for item in dsNhanVien)
            tongsnv = len(dsNhanVien)
            for item in dsNhanVien:
                item.display()
            tuoitb = tongtuoi / tongsnv
            print(f'Tuổi trung bình nhân viên = {tuoitb}')
    elif userChoice == 13:
        if len(dsNhanVien) == 0:
            print('Danh sách rỗng')
        else:
            tuoimax = max(item.age for item in dsNhanVien)
            print('Tuổi cao nhất =', tuoimax)
    elif userChoice == 14:
        if len(dsNhanVien) == 0:
            print('Danh sách rỗng')
        else:
            tongsnv = len(dsNhanVien)
            for item in dsNhanVien:
                item.display()
            print('Tổng số nhân viên =', tongsnv)
    elif userChoice == 15:
        arrTuoi = [item.age for item in dsNhanVien]
        arrLuong = [item.salary for item in dsNhanVien]
        plt.figure(figsize=(15, 5))
        plt.title("Biểu đồ tuổi và lương")
        plt.xlabel("Ox: tuổi")
        plt.ylabel("Oy: lương")
        plt.plot(arrTuoi, arrLuong, "go")
        plt.show()
    elif userChoice == 16:
        arrTuoi = [item.age for item in dsNhanVien]
        arrLuong = [item.salary for item in dsNhanVien]
        plt.figure(figsize=(15, 5))
        plt.title("Biểu đồ tuổi và lương")
        plt.xlabel("Ox: tuổi")
        plt.ylabel("Oy: lương")
        plt.plot(arrTuoi, arrLuong, "go")
        plt.show()
    elif userChoice == 17:
        arrTuoi = [item.age for item in dsNhanVien]
        arrLuong = [item.salary for item in dsNhanVien]
        plt.figure(figsize=(15, 5))
        plt.title("Biểu đồ tuổi và lương")
        plt.xlabel("Ox: tuổi")
        plt.ylabel("Oy: lương")
        plt.plot(arrTuoi, arrLuong, "go")
        plt.show()
    elif userChoice == 18:
        arrTuoi = [item.age for item in dsNhanVien]
        arrLuong = [item.salary for item in dsNhanVien]
        plt.figure(figsize=(15, 5))
        plt.title("Biểu đồ tuổi và lương")
        plt.xlabel("Ox: tuổi")
        plt.ylabel("Oy: lương")
        plt.plot(arrTuoi, arrLuong, "go")
        plt.show()
    elif userChoice == 19:
        arrTuoi = [item.age for item in dsNhanVien]
        arrLuong = [item.salary for item in dsNhanVien]
        plt.figure(figsize=(15, 5))
        plt.title("Biểu đồ tuổi và lương")
        plt.xlabel("Ox: tuổi")
        plt.ylabel("Oy: lương")
        plt.plot(arrTuoi, arrLuong, "go")
        plt.show()
    else:
        print('TẠM BIỆT')
        break
