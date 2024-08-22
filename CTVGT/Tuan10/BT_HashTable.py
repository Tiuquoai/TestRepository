class BangBam:
    #Định nghĩa bảng băm
    def __init__(self, kich_thuoc=10):
        self.danh_sach = [None for _ in range(kich_thuoc)]
        #Cho tất cả các phần tử trong danh sách đề là None
    #def
    #Chuyển bảng băm về chuỗi
    def __str__(self):
        kq = '['
        #Danh sách gồm 2 cấp
        stt1 =0
        for x in self.danh_sach:
            stt1 = stt1 + 1
            #Nếu không phải là phần tử đầu tiên
            if stt1 !=1:
                kq = kq +','
            #if
            if x is None:
                kq = kq +'[None]'
            else:
                #Không rỗng, không chứa con bên trong 
                kq = kq +'['
                stt2 = 0
                #Duyêt qua các phần tử con
                for e in x:
                    stt2 = stt2 + 1
                    #Không phải là phần tử đầu tiên, nối thêm vào
                    if stt2 !=1:
                        kq = kq +','
                    #if
                    kq = kq +str(e[0])+': '+str(e[1])
                #for
                kq = kq +']'
            #if
        kq = kq +']'
        return kq
    #def
    #Thực hiện trả về chuyển giá trị băm của khóa
    def bam(self,khoa):
        kich_thuoc = len(self.danh_sach)
        return hash(khoa) % kich_thuoc
    #def
    #Thực hiện thêm cặp (khóa, giá trị) vào bảng băm
    def them(self,khoa,gia_tri):
        chi_muc = self.bam(khoa)
        #Chưa có phần tử đưa vào vị trí này
        if self.danh_sach[chi_muc] is None:
            #Thêm mới
            self.danh_sach[chi_muc] = list() #Ví bảng băm chứa nhiều phần tử vào mỗi khe
            self.danh_sach[chi_muc].append([khoa,gia_tri])
        else:
            #Có rồi, cập nhật
            #Có 2 trường hợp: khe đã có, khe chưa có con
            #TH1: khoa mod 5 = thì khóa và giá trị sẽ được đưa vào khe = số dư
            #Nếu khe đó có giá trị khóa = với khóa đưa vào thì cập nhật lại giá trị của khóa đó
            #Nếu khe đó có giá trị khóa khoác với khóa đưa vào thì thêm vào cặp(khóa, giá trị) mới vào khe đó
            #Một khe có thể có nhiều phần tử
            cap_nhat = False
            for x in self.danh_sach[chi_muc]:
            #Xem có pt bằng nó không
                if x[0] == khoa: #Cập nhật giá trị của khóa đó
                    x[1] = gia_tri
                    cap_nhat = True
                    break
                #if
            #for
            if cap_nhat == False: #Không cập nhật phần tử con mà thêm vào
                self.danh_sach[chi_muc].append([khoa,gia_tri])
            #if
        #if
    #def
    #Lấy ra 1 giá trị từ bảng băm với khóa tương ứng
    def lay(self,khoa):
        chi_muc = self.bam(khoa)
        #Nếu giá trị này None
        if self.danh_sach[chi_muc] is None:
            return None
        else:
            for x in self.danh_sach[chi_muc]:
                if x[0] == khoa:
                    return x[1]
                #if
            #for
        #if
    #def
    #Thực hiện như phương thức thêm
    def __setitem__(self,khoa,gia_tri):
        self.them(khoa,gia_tri)
    #def
    #Thực hiện như phương thức lấy
    def __getitem__(self,khoa):
        return self.lay(khoa)
    #def
#class
#Tạo đối tượng bảng băm
#Thêm vào bảng băm các giá trị ngẫu nhiên [khóa, giá trị] vào bảng băm, xuất chuỗi mô tả bảng băm sau mỗi lần thêm
#Nhập vào 1 dãy khóa, lấy và xuấ ra giá trị tương ứng với khóa đó trong bảng băm
def main():
    bang_bam = BangBam(5)
    import random
    for _ in range(18):
        khoa = random.randint(0,10)
        gia_tri = random.randint(0,100)
        print(f'*Them khoa ={khoa}, gia tri ={gia_tri}')
        #bang_bam.them(khoa,giatri)
        bang_bam[khoa] = gia_tri
        print(bang_bam)
        print()
    #for
    khoa = int(input('Nhập vào 1 khóa: '))
    #gia_tri = bang_bam.lay(khoa)
    gia_tri = bang_bam[khoa]
    print(f'khoa ={khoa} có giá trị là {gia_tri}')
#def
if __name__=='__main__':
    main()
#if