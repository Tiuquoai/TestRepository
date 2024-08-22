class Sach:
    def __init__(self, ten_sach, tac_gia, nha_xuat_ban, nam_xuat_ban, gia):
        self.ten_sach = ten_sach
        self.tac_gia = tac_gia
        self.nha_xuat_ban = nha_xuat_ban
        self.nam_xuat_ban = nam_xuat_ban
        self.gia = gia
        self.next = None

class DanhSachSach:
    def __init__(self):
        self.head = None

    def them_sach_vao_cuoi(self, sach):
        if not self.head:
            self.head = sach
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = sach

    def them_sach_vao_dau(self, sach):
        sach.next = self.head
        self.head = sach

    def xuat_danh_sach(self):
        current = self.head
        while current:
            print("Tên sách:", current.ten_sach)
            print("Tác giả:", current.tac_gia)
            print("Nhà xuất bản:", current.nha_xuat_ban)
            print("Năm xuất bản:", current.nam_xuat_ban)
            print("Giá:", current.gia)
            print("--------------------")
            current = current.next

    def dem_sach_theo_tac_gia(self, tac_gia):
        count = 0
        current = self.head
        while current:
            if tac_gia in current.tac_gia:
                count += 1
            current = current.next
        return count

    def sach_phat_hanh_trong_nam_cua_nxb(self, nam, nha_xuat_ban):
        danh_sach_sach = []
        current = self.head
        while current:
            if current.nam_xuat_ban == nam and current.nha_xuat_ban == nha_xuat_ban:
                danh_sach_sach.append(current)
            current = current.next
        return danh_sach_sach

    def tim_sach_theo_ten(self, ten_sach):
        current = self.head
        while current:
            if current.ten_sach.lower() == ten_sach.lower():
                return current
            current = current.next
        return None

    def them_sach_moi(self, sach):
        ten_sach = sach.ten_sach
        if self.tim_sach_theo_ten(ten_sach):
            print("Sách đã tồn tại trong danh sách. Vui lòng nhập tên sách khác.")
        else:
            self.them_sach_vao_cuoi(sach)

    def xoa_sach_theo_ten(self, ten_sach):
        if not self.head:
            print("Danh sách rỗng.")
            return
        if self.head.ten_sach.lower() == ten_sach.lower():
            self.head = self.head.next
            print("Đã xóa sách có tên", ten_sach)
            return
        current = self.head
        while current.next:
            if current.next.ten_sach.lower() == ten_sach.lower():
                current.next = current.next.next
                print("Đã xóa sách có tên", ten_sach)
                return
            current = current.next
        print("Không tìm thấy sách có tên", ten_sach)

# Hàm main để thực hiện các thao tác từ menu
def main():
    danh_sach_sach = DanhSachSach()
    while True:
        print("\nChọn chức năng:")
        print("1. Thêm một sách mới vào cuối danh sách")
        print("2. Thêm một sách mới vào đầu danh sách")
        print("3. Xuất danh sách các sách")
        print("4. Đếm số lượng sách của một tác giả")
        print("5. Liệt kê các sách phát hành trong năm của một nhà xuất bản")
        print("6. Tìm kiếm và thêm sách mới")
        print("7. Xóa sách khỏi danh sách")
        print("8. Kết thúc chương trình")

        choice = int(input("Nhập lựa chọn (1-8): "))

        if choice == 1:
            ten_sach = input("Nhập tên sách: ")
            tac_gia = input("Nhập tác giả: ")
            nha_xuat_ban = input("Nhập nhà xuất bản: ")
            nam_xuat_ban = int(input("Nhập năm xuất bản: "))
            gia = int(input("Nhập giá: "))
            sach_moi = Sach(ten_sach, tac_gia, nha_xuat_ban, nam_xuat_ban, gia)
            danh_sach_sach.them_sach_vao_cuoi(sach_moi)
        elif choice == 2:
            ten_sach = input("Nhập tên sách: ")
            tac_gia = input("Nhập tác giả: ")
            nha_xuat_ban = input("Nhập nhà xuất bản: ")
            nam_xuat_ban = int(input("Nhập năm xuất bản: "))
            gia = int(input("Nhập giá: "))
            sach_moi = Sach(ten_sach, tac_gia, nha_xuat_ban, nam_xuat_ban, gia)
            danh_sach_sach.them_sach_vao_dau(sach_moi)
        elif choice == 3:
            print("Danh sách các sách:")
            danh_sach_sach.xuat_danh_sach()
        elif choice == 4:
            tac_gia = input("Nhập tên tác giả: ")
            count = danh_sach_sach.dem_sach_theo_tac_gia(tac_gia)
            print(f"Số lượng sách của tác giả {tac_gia}: {count}")
        elif choice == 5:
            nam_xuat_ban = int(input("Nhập năm xuất bản: "))
            nha_xuat_ban = input("Nhập tên nhà xuất bản: ")
            sach_phat_hanh = danh_sach_sach.sach_phat_hanh_trong_nam_cua_nxb(nam_xuat_ban, nha_xuat_ban)
            print(f"Các sách phát hành trong năm {nam_xuat_ban} của nhà xuất bản {nha_xuat_ban}:")
            for sach in sach_phat_hanh:
                print(sach.ten_sach)
        elif choice == 6:
            ten_sach = input("Nhập tên sách: ")
            sach_tim_thay = danh_sach_sach.tim_sach_theo_ten(ten_sach)
            if sach_tim_thay:
                print("Sách đã tồn tại trong danh sách. Bạn có muốn cập nhật thông tin không?")
                lua_chon = input("Nhập 'y' nếu muốn cập nhật, 'n' nếu không: ")
                if lua_chon.lower() == 'y':
                    tac_gia = input("Nhập tác giả mới: ")
                    nha_xuat_ban = input("Nhập nhà xuất bản mới: ")
                    nam_xuat_ban = int(input("Nhập năm xuất bản mới: "))
                    gia = int(input("Nhập giá mới: "))
                    sach_moi = Sach(ten_sach, tac_gia, nha_xuat_ban, nam_xuat_ban, gia)
                    danh_sach_sach.them_sach_moi(sach_moi)
            else:
                tac_gia = input("Nhập tác giả: ")
                nha_xuat_ban = input("Nhập nhà xuất bản: ")
                nam_xuat_ban = int(input("Nhập năm xuất bản: "))
                gia = int(input("Nhập giá: "))
                sach_moi = Sach(ten_sach, tac_gia, nha_xuat_ban, nam_xuat_ban, gia)
                danh_sach_sach.them_sach_vao_cuoi(sach_moi)
        elif choice == 7:
            ten_sach = input("Nhập tên sách cần xóa: ")
            danh_sach_sach.xoa_sach_theo_ten(ten_sach)
        elif choice == 8:
            print("Kết thúc chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn từ 1 đến 8.")

if __name__ == "__main__":
    main()
