class VeMayBay:
    def __init__(self, ma_ve, ten_hanh_khach, so_hieu_chuyen_bay, ngay_khoi_hanh, so_ghe, gia_ve):
        self.ma_ve = ma_ve
        self.ten_hanh_khach = ten_hanh_khach
        self.so_hieu_chuyen_bay = so_hieu_chuyen_bay
        self.ngay_khoi_hanh = ngay_khoi_hanh
        self.so_ghe = so_ghe
        self.gia_ve = gia_ve

    def hien_thi(self):
        print(f'Mã vé: {self.ma_ve}')
        print(f'Tên hành khách: {self.ten_hanh_khach}')
        print(f'Số hiệu chuyến bay: {self.so_hieu_chuyen_bay}')
        print(f'Ngày khởi hành: {self.ngay_khoi_hanh}')
        print(f'Số ghế: {self.so_ghe}')
        print(f'Giá vé: {self.gia_ve}')

    def tinh_gia_ve_sau_giam_gia(self, ty_le_giam_gia):
        gia_ve_sau_giam_gia = self.gia_ve - (self.gia_ve * ty_le_giam_gia)
        return max(gia_ve_sau_giam_gia, 0)  # Đảm bảo giá vé không âm

    def lay_thong_tin_ve(self):
        return f'{self.ten_hanh_khach} - Chuyến bay {self.so_hieu_chuyen_bay} - Ghế {self.so_ghe}'

    def lay_thong_tin_chuyen_bay(self):
        return f'Chuyến bay {self.so_hieu_chuyen_bay} - Ngày khởi hành: {self.ngay_khoi_hanh}'
