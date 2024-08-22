from dslk_queue import DSLienKetHD

class HangDoi:
    #Queue
    def __init__(self):
        self.danh_sach = DSLienKetHD()
    #def       
    def __str__(self):
        kq = 'Hang Doi ['
        kq = kq + str(self.danh_sach)
        kq = kq + ']'
        return kq
    
    def la_rong(self):
        return self.danh_sach.dau == None
    
    def xep_hang(self,gia_tri):
        self.danh_sach.them_duoi(gia_tri)
        
    def ra_hang(self):
        if self.la_rong():
            return None
        else:
            kq = self.danh_sach.lay_dau()
            self.danh_sach.xoa_dau()
            return kq
        
if __name__ =='__main__':
    hang_doi = HangDoi()
    print(hang_doi)
    
    print('--------xep hang-------')
    for x in range (1,6):
        print (f'xep hang {x}')
        hang_doi.xep_hang(x)
        print(hang_doi)
        
    print('-------------ra hang-----------')
    while not hang_doi.la_rong():
        gt = hang_doi.ra_hang()
        print(f'ra hang ->{gt}')
        print(hang_doi)
