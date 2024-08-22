# Định nghĩa lớp DSLK mô tả 1 dslk gồm các phương thức:
# __init__(self): khởi tạo
# __str(self)__: đổi sang kiẻue chuỗi
# them_dau(self, gia_tri): them phan tu vao dau ds
# them_duoi(self, gia_tri): them phan tu vao cuoi ds
# lay_Dau(self): lấy giá trị phần tử đầu ds
# xoa_dau(self): xóa phần tử đầu ds

class Nut:
    def __init__(self, gia_tri):
        self.gia_tri = gia_tri
        self.nut_ke_tiep = None
        #def
    #class
    
    class DSLienKetHD:
        def __init__(self):
            self.dau = None
            self.duoi = None
        #def
        #doi ve chuoi
        def __str__(self):
            kq =''
            stt = 0
            hien_tai = self.dau
            while hien_tai != None:
                stt = stt+1
                if stt == 1:#phan tu dau tien
                    kq = kq + str(hien_tai.gia_tri)
            else:
                kq = kq + '->' + str[hien_tai.gia_tri]
            #if
            hien_tai = hien_tai.nut_ke_tiep
            #while
            return kq
    #def
                
                
                
                
    #them dau
    def them_dau(self, gia_tri):
        nut = Nut(gia_tri)
        if self.dau == None:
            self.dau = nut
            self.duoi = nut
        else:
            nut.nut_ke_tiep = self.dau
            self.dau = nut
        #if
    #def
    #them duoi
    def them_duoi(self,gia_tri):
        nut = Nut(gia_tri)
        if self.dau == None: #nut dau tien
            self.dau = nut
            self.duoi = nut
        else: #khong la nut dau tien
            self.duoi.nut_ke_tiep = nut
            self.duoi = nut
        #if
    #def
    #lay gia tri phan tu dau tien
    def lay_dau(self):
        if self.dau == None:
            return None
        else:
            return  self.dau.gia_tri
        #if
    #def
    #xoa dau
    def xoa_dau(self):
        tam = self.dau
        if self.dau ==self.duoi:
            self.dau = None
            self.duoi = None
        else:
            self.dau = self.dau_nut_ke_tiep
        #if
        del tam
    #def
#class

    
            
            
            
            