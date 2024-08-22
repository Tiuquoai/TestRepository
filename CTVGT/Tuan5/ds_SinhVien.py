class SinhVien:
    def __init__(self, masv, ten_sv, mon_hoc, diem):
        self.masv = masv
        self.ten_sv = ten_sv
        self.mon_hoc = mon_hoc
        self.diem = diem

class DanhSachSinhVien:
    def __init__(self):
        self.danh_sach = []

    def chen_hs_moi_cuoi(self, sv):
        self.danh_sach.append(sv)

    def sap_xep_theo_diem(self):
        self.danh_sach.sort(key=lambda x: x.diem)

    def chen_hs_moi_sau_sap_xep(self, sv):
        self.chen_hs_moi_cuoi(sv)
        self.sap_xep_theo_diem()

    def lay_danh_sach_diem_lon_hon_x(self, x):
        return [sv for sv in self.danh_sach if sv.diem > x]

    def tim_k_sv_diem_cao_nhat(self, k):
        return sorted(self.danh_sach, key=lambda x: x.diem, reverse=True)[:k]

    def loai_bo_sv_diem_nho_hon_x(self, x):
        self.danh_sach = [sv for sv in self.danh_sach if sv.diem >= x]

    def hop_nhat_danh_sach(self, danh_sach_moi):
        self.danh_sach.extend(danh_sach_moi)

    def in_danh_sach(self):
        for sv in self.danh_sach:
            print("Mã SV:", sv.masv, "- Tên SV:", sv.ten_sv, "- Môn học:", sv.mon_hoc, "- Điểm:", sv.diem)

    def ghi_danh_sach_ra_file(self, ten_file):
        with open(ten_file, "w") as file:
            for sv in self.danh_sach:
                file.write(f"{sv.masv},{sv.ten_sv},{sv.mon_hoc},{sv.diem}\n")

# Hàm main để thực hiện các thao tác từ menu
def main():
    danh_sach_sv = DanhSachSinhVien()
    while True:
        print("\nChọn chức năng:")
        print("1. Chèn một học sinh mới vào danh sách cuối cùng")
        print("2. Sắp xếp danh sách theo thứ tự tăng dần của Điểm")
        print("3. Chèn một học sinh mới vào danh sách đã sắp xếp")
        print("4. Lấy danh sách sinh viên có Điểm lớn hơn x")
        print("5. Tìm kiếm k sinh viên có Điểm cao nhất")
        print("6. Loại bỏ tất cả sinh viên có Điểm nhỏ hơn x")
        print("7. Hợp nhất vào danh sách sinh viên")
        print("8. In ra màn hình danh sách sinh viên")
        print("9. Ghi danh sách học sinh ra file txt")
        print("10. Kết thúc chương trình")

        choice = int(input("Nhập lựa chọn (1-10): "))

        if choice == 1:
            masv = input("Nhập Mã SV: ")
            ten_sv = input("Nhập Tên SV: ")
            mon_hoc = input("Nhập Môn học: ")
            diem = float(input("Nhập Điểm: "))
            sv_moi = SinhVien(masv, ten_sv, mon_hoc, diem)
            danh_sach_sv.chen_hs_moi_cuoi(sv_moi)
        elif choice == 2:
            danh_sach_sv.sap_xep_theo_diem()
        elif choice == 3:
            masv = input("Nhập Mã SV: ")
            ten_sv = input("Nhập Tên SV: ")
            mon_hoc = input("Nhập Môn học: ")
            diem = float(input("Nhập Điểm: "))
            sv_moi = SinhVien(masv, ten_sv, mon_hoc, diem)
            danh_sach_sv.chen_hs_moi_sau_sap_xep(sv_moi)
        elif choice == 4:
            x = float(input("Nhập x: "))
            danh_sach = danh_sach_sv.lay_danh_sach_diem_lon_hon_x(x)
            print("Danh sách sinh viên có Điểm lớn hơn", x)
            danh_sach_sv.in_danh_sach(danh_sach)
        elif choice == 5:
            k = int(input("Nhập k: "))
            danh_sach = danh_sach_sv.tim_k_sv_diem_cao_nhat(k)
            print(f"{k} sinh viên có Điểm cao nhất:")
            danh_sach_sv.in_danh_sach(danh_sach)
        elif choice == 6:
            x = float(input("Nhập x: "))
            danh_sach_sv.loai_bo_sv_diem_nho_hon_x(x)
        elif choice == 7:
            danh_sach_moi = DanhSachSinhVien()
            # Code để thêm sinh viên vào danh_sách mới
            danh_sach_sv.hop_nhat_danh_sach(danh_sach_moi)
        elif choice == 8:
            danh_sach_sv.in_danh_sach()
        elif choice == 9:
            ten_file = input("Nhập tên file: ")
            danh_sach_sv.ghi_danh_sach_ra_file(ten_file)
            print("Đã ghi danh sách sinh viên ra file", ten_file)
        elif choice == 10:
            print("Kết thúc chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Hãy nhập lại.")

if __name__ == "__main__":
    main()
