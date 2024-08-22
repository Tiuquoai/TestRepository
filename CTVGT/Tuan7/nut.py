class Nut:
#định nghĩa lớp nút
    def __init__(self, khoa=None):
        self.khoa = khoa
        self.trai = None
        self.phai = None
    #def
    def chen(self,khoa):
        if self is None:
            nut = Nut(khoa)
            self = nut
            return
        #if nut chua duoc khoi tao
        #nut da khoi tao roi, nut khac None
        if khoa<self.khoa:
            if self.trai == None:
                self.trai = Nut(khoa) #nut chua co gia tri
            else: #nut trai da co gia tri
                self.trai.chen(khoa)
                #if
        elif khoa > self.khoa:
            if self.phai == None:
                self.phai = Nut(khoa)
            else:
                #co nut ben phai roi
                self.phai.chen(khoa)
                #if
        else:
            #khong lon hon hay khong nho hon, bi trung khoa
                print (f'bi trung khoa {khoa}')
            #if
        #def
#class Nut
#dinh nghia lop cay nhi phan tim kiem
class CayNhiPhanTimKiem:
    def __init__(self,khoa = None):
        if khoa == None: #khong truyen vao tham so
            self.goc = None
        else:
            self.goc = Nut(khoa)
        #if
    #def
    #chen vao 1 gia tri khoa
    def chen(self, khoa):
        if self.goc == None:
            self.goc = Nut(khoa)
        else: #co nut roi
            self.goc.chen(khoa)
        #if
    #def chen 1 nut vao cay
    #xoa 1 nut
    def xoa(self,khoa):
        nut_cha = None
        cha_con = None
        nut_ht = self.goc
        #tim nut xoa
        #cac truong hop xoa nut la, xoa nut co 1 con trai, xoa nut co 1 con phai
        #xoa nut co ca 2 con, xoa nut goc
        while nut_ht != None:
            if nut_ht.khoa > khoa: #khoa xoa nho hon
                nut_cha = nut_ht
                nut_ht = nut_ht.trai #tim nhanh ben trai
                cha_con = 'trai'
            elif nut_ht.khoa < khoa:
                nut_cha = nut_ht
                nut_ht = nut_ht.phai
                cha_con = 'phai'
            else: #bang, tim thay nghia la xoa nut nay
                if nut_cha == None: #nut goc
                    #xoa nut goc
                    #neu nut goc khong co 2 con
                    if nut_ht.trai == None and nut_ht.phai == None:
                        #xoa nut goc ma khong co con
                        self.goc = None
                    #if
                    elif nut_ht.trai == None:
                        #nut trai khong co con, xoa nut goc chi co 1 nut con ben phai
                        self.goc = nut_ht.phai
                    elif nut_ht.phai == None:
                        #xoa nut chi co 1 con ben trai
                        self.goc = nut_ht.trai
                    else:
                        #xoa nut goc co du 2 con
                        #xoay trai
                        self.goc = nut_ht.phai
                        tam = self.goc
                        while tam.trai !=None:
                        #truy tim den cuc trai de gan nhanh trai xuong ben trai cua nut cuc trai
                            tam = tam.trai
                        #while
                        tam.trai = nut_ht.trai
                    #if
                elif nut_ht.trai == None and nut_ht.phai == None:
                    #khong phai nut goc. Xoa nut la, khong co con trai va phai
                    if cha_con == 'trai':
                        nut_cha.trai = None
                    else:
                        nut_cha.trai = None
                    #if
                elif nut_ht.trai == None:
                    #khong phai nut la ma la nut giua
                    #xoa nut chi co 1 con ben phai
                    if cha_con == 'trai':
                        nut_cha.trai = nut_ht.phai
                    else:
                        nut_cha.phai = nut_ht.phai
                    #if
                elif nut_ht.phai == None:
                    #xoa nut giua chi co 1 con ben trai
                    if cha_con == 'trai':
                        nut_cha.trai = nut_ht.trai
                    else: 
                        nut_cha.phai = nut_ht.trai
                else:
                    #xoa nut co du 2 con
                    #xoay trai
                    if cha_con == 'trai':
                        nut_cha.trai = nut_ht.phai
                    else:
                        nut_cha.phai = nut_ht.phai
                    #if
                    if nut_ht.phai.trai == None:
                        nut_ht.phai.trai = nut_ht.trai
                    else: #nut chua la none, truy tim nut tan cung ben trai
                        tam = nut_ht.phai
                        while tam.trai != None:
                            tam = tam.trai
                        #while
                        tam.trai = nut_ht.trai
                    #if
                #if
                del nut_ht
                break
                #if
        #while
    #def        
    def duyet_trai_nut_phai(self,goc=0):
        #duyet theo LNR
        nut_ht = goc
        if goc == 0:
            nut_ht = self.goc
        #if
        #kiem tra nut hien tai co bang None khong
        if nut_ht == None:
            return[]
        else: #cay co gia tri
            kq = []
            kq_trai = self.duyet_trai_nut_phai(nut_ht.trai)
            for x in kq_trai:
                kq.append(x)
            #for duyet trai
            kq.append(nut_ht.khoa)
            #duyet phai
            kq_phai = self.duyet_trai_nut_phai(nut_ht.phai)
            for x in kq_phai:
                kq.append(x)
            #for
            return kq
        #if
    #def
    #duyet NLR
    def duyet_nut_trai_phai(self,goc = 0):
        #duyet theo NLR
        nut_ht = goc
        if goc == 0:
            nut_ht = self.goc
        #if
        #kiemtra nut hien tai co bang none khong
        if nut_ht == None:
            return []
        else: #cay co gia tri
            kq = []
            kq.append(nut_ht.khoa)
            kq_trai = self.duyet_nut_trai_phai(nut_ht.trai)
            for x in kq_trai:
                kq.append(x)
            #for duyet trai
            
            #duyet phai
            kq_phai = self.duyet_nut_trai_phai(nut_ht.phai)
            for x in kq_phai:
                kq.append(x)
            
            #for
            return kq
        #if
    #def
    def duyet_trai_phai_nut(self,goc=0):
        #duyet theo LRN
        nut_ht = goc
        if goc == 0:
            nut_ht = self.goc
        #if
        #kiemtra nut hien tai co bang none khong
        if nut_ht == None:
            return[]
        else: #cay co gia tri
            kq = []
            kq_trai = self.duyet_trai_phai_nut(nut_ht.phai)
            for x in kq_trai:
                kq.append(x)
            #for duyet trai
            
            #duyet phai
            kq_phai = self.duyet_trai_phai_nut(nut_ht.phai)
            for x in kq_phai:
                kq.append(x)
            #not
            kq.append(nut_ht.khoa)
            #for
            return kq
        #if
    #def
    #tim
    def tim(self,khoa):
        if self.goc == None:
        #cay rong
            return
        #if
        nut_ht = self.goc
        kq =''
        while (nut_ht != None and nut_ht.khoa !=khoa):
            kq = kq + f'{nut_ht.khoa} -> '
            if khoa <=nut_ht.khoa:
                nut_ht = nut_ht.trai
            else:
                nut_ht = nut_ht.phai
            
            #if
        #while
        if nut_ht == None: #tim khong thay
            return None
        else: #tim thay
            kq =kq +f'{nut_ht.khoa}'
            return kq
        #if
    #def
#class
#ham main
def main():
    SO_PHAN_TU = 10
    cay = CayNhiPhanTimKiem()
    print('******chen vao cay *******')
    tap_gia_tri = set()
    from random import randint
    while len(tap_gia_tri) < SO_PHAN_TU:
        gt = randint (1,100) #lay 10 phan tu khong trung nhau nen dung tap hop
        tap_gia_tri.add(gt)
    
    #while
    #tap_gia_tri = list(tap_gia_tri) #phat sin danh sach ngau nhien
    tap_gia_tri = [66,46,84,11,84,99,36,77,83,87,100,86,85] 
    print('chen lan luot', tap_gia_tri)
    for x in tap_gia_tri:
        cay.chen(x)
    kq = cay.duyet_trai_nut_phai()
    print('*******duyet cay theo Trai - Nut - Phai (LNR):',kq)
    
    kq = cay.duyet_nut_trai_phai()
    print('*******duyet cay theo Nut - Trai - Phai (LNR):',kq)
    
    kq = cay.duyet_trai_phai_nut()
    print('*******duyet cay theo Trai - Phai - Nut (LNR):',kq)
    print('*****xoa 1 phan tu co trong cay:')
    gt = int(input('nhap vao gia tri can xoa'))
    print(f'xoa {gt}')
    cay.xoa(gt)
    kq = cay.duyet_trai_nut_phai()
    print('*******duyet cay theo Trai - Nut - Phai (LNR):',kq)
    
    kq = cay.duyet_nut_trai_phai()
    print('*******duyet cay theo Nut - Trai - Phai (LNR):',kq)
    
    kq = cay.duyet_trai_phai_nut()
    print('*******duyet cay theo Trai - Phai - Nut (LNR):',kq)
    #tim
    while True:
        nhap = input('nhap vao khoa can tim ')
        if nhap == '':
            break
        #if
        gt = int(nhap)
        kq = cay.tim(gt)
        if kq == None:
            print(f'khong tim thay {gt}')
        else: #tim thay
            print(f'tim thay {gt}:{kq}')
        #if
    #while
#def
if __name__=='__main__':
    main()
#if    
             
            
        
    
    