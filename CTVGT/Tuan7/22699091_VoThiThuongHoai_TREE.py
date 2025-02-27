class Nut:
    #định ngĩa lớp nút
    def __init__(self, khoa=None):
        self.khoa = khoa
        self.trai = None
        self.phai = None
    #def
    def chen(self, khoa):
        if self is None:
            nut = Nut(khoa)
            self = nut
            return
        #if Nút chưa được khởi tạo
        #nút đã khởi tạo rồi, Nút khác None
        if khoa<self.khoa:
            if self.trai == None:
                self.trai = Nut(khoa) #nút trái chưa có giá trị
            else: #nút trái đã có giá trị
                self.trai.chen(khoa)
            #if
        elif khoa > self.khoa:
            if self.phai == None:
                self.phai = Nut(khoa)
            else:
            #có nút bên phải rồi
                self.phai.chen(khoa)
            #if
        else:
        #Không lớn hơn hay không nhỏ hơn, bị trùng khóa
            print (f'Bị trùng khóa {khoa}')
        #if
    #def
#class Nut
#định nghĩa lớp cây nhị phân tìm kiếm
class CayNhiPhanTimKiem:
    def __init__(self,khoa = None):
        if khoa == None:#không truyền vào tham số
            self.goc = None
        else:
            self.goc = Nut(khoa)
        #if
    #def
    #chèn vào 1 giá trị khóa
    def chen(self, khoa):
        if self.goc == None:
            self.goc = Nut(khoa)
        else:#có nút rồi
            self.goc.chen(khoa)
        #if
    #def chèn 1 nút vào cây
    #xóa 1 nút
    def xoa(self,khoa):
        nut_cha = None
        cha_con = None
        nut_ht = self.goc
        #tìm nút xóa
        #các trường hợp xóa nút lá, xóa nút có 1 con trái, xóa nút có 1 con phải,
        #xóa nút có cả 2 con, xóa nút gốc
        while nut_ht != None:
            if nut_ht.khoa > khoa:#khóa xóa nhỏ hơn
                nut_cha =nut_ht
                nut_ht = nut_ht.trai #tìm nhánh bên trái
                cha_con ='trai'
            elif nut_ht.khoa < khoa:
                nut_cha = nut_ht
                nut_ht = nut_ht.phai
                cha_con = 'phai'
            else:#bằng, tìm thấy nghĩa là xóa nút này
                if nut_cha == None: #nút gốc
                    #xóa nút gốc
                    #nếu nút gốc không có 2 con
                    if nut_ht.trai == None and nut_ht.phai == None:
                        #xóa nút gốc mà không có con
                        self.goc = None
                    #if
                    elif nut_ht.trai == None:
                        #Nút trái không có con, xóa nút gốc chỉ có nút con bên phải
                        self.goc = nut_ht.phai
                    elif nut_ht.phai == None:
                        #xóa nút chỉ có 1 con bên trái
                        self.goc = nut_ht.trai
                    else:
                        #xóa  nút gốc có đủ 2 con
                        #xoay trái
                        self.goc = nut_ht.phai
                        tam = self.goc  
                        while tam.trai !=None:
                        #truy tìm đến cực trái để gắn nhánh trái xuống bên trái của nút cực trái
                            tam = tam.trai 
                        #while
                        tam.trai = nut_ht.trai
                    #if
                elif nut_ht.trai == None and nut_ht.phai == None:
                    #không phải nút gốc. Xóa nút lá, không có con trái và phải
                    if cha_con == 'trai':
                        nut_cha.trai = None
                    else:
                        nut_cha.phai = None
                    #if
                elif nut_ht.trai == None:
                    #không phải là nút mà là nút giữa
                    #xóa nút chỉ có 1 con bên phải
                    if cha_con == 'trai':
                        nut_cha.trai = nut_ht.phai 
                    else:
                        nut_cha.phai = nut_ht.phai 
                    #if
                elif nut_ht.phai == None:
                    #xóa nút giữa chỉ có 1 con bên trái
                    if cha_con == 'trai':
                        nut_cha.trai = nut_ht.trai 
                    else:
                        nut_cha.phai = nut_ht.trai 
                else:
                    #xóa nút có đủ 2 con
                    #xoay trái
                    if cha_con == 'trai':
                        nut_cha.trai = nut_ht.phai 
                    else:
                        nut_cha.phai = nut_ht.phai 
                    #if
                    if nut_ht.phai.trai == None:
                        nut_ht.phai.trai = nut_ht.trai 
                    else: #nút chưa là None, truy tìm nút tận cùng bên trái
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
        #duyệt theo LNR
        nut_ht = goc
        if goc == 0:
            nut_ht = self.goc
        #if
        #kiểm tra nút hiện tại có bằng None không
        if nut_ht == None:
            return []
        else: #cây có giá trị
            kq = []
            kq_trai = self.duyet_trai_nut_phai(nut_ht.trai)
            for x in kq_trai:
                kq.append(x)
            #for duyệt trái
            kq.append(nut_ht.khoa)
            #duyệt phải
            kq_phai = self.duyet_trai_nut_phai(nut_ht.phai)
            for x in kq_phai:
                kq.append(x)
            #for
            return kq
        #if
    #def
    def duyet_nut_trai_phai(self,goc=0):
        #duyệt theo NLR
        nut_ht = goc
        if goc == 0:
            nut_ht = self.goc 
        #if
        #kiểm tra nút hiện tại có bằng None không
        if nut_ht == None:
            return []
        else: #cây có giá trị
            kq = []
            kq.append(nut_ht.khoa)
            kq_trai = self.duyet_nut_trai_phai(nut_ht.trai)
            for x in kq_trai:
                kq.append(x)
            #for duyệt trái
            
            #duyệt phải
            kq_phai = self.duyet_nut_trai_phai(nut_ht.phai)
            for x in kq_phai:
                kq.append(x)
            #for
            return kq
        #if
    #def
    def duyet_trai_phai_nut(self,goc=0):
        #duyệt theo LRN
        nut_ht = goc
        if goc == 0:
            nut_ht = self.goc 
        #if
        #kiểm tra nút hiện tại có bằng None không
        if nut_ht == None:
            return []
        else: #cây có giá trị
            kq = []
            kq_trai = self.duyet_trai_nut_phai(nut_ht.trai)
            for x in kq_trai:
                kq.append(x)
            #for duyệt trái
            
            #duyệt phải
            kq_phai = self.duyet_trai_phai_nut(nut_ht.phai)
            for x in kq_phai:
                kq.append(x)
            #not
            kq.append(nut_ht.khoa)
            #for
            return kq
        #if
    #def
    #tìm
    def tim(self, khoa):
        if self.goc == None:
        #cây rỗng
            return
        #if
        nut_ht = self.goc 
        kq = ''
        while (nut_ht != None and nut_ht.khoa !=khoa):
            kq = kq + f'"{nut_ht.khoa} -> '
            if khoa <= nut_ht.khoa:
                nut_ht = nut_ht.trai 
            else:
                nut_ht = nut_ht.phai 
            #if
        #while
        if nut_ht == None: #tìm không thấy
            return None
        else: #tìm thấy
            kq = kq + f'{nut_ht.khoa}'
            return kq
        #if
    #def
#class
#Hàm main
def main():
    SO_PHAN_TU = 10
    cay = CayNhiPhanTimKiem()
    print('*******Chèn vào cây*******')
    tap_gia_tri = set()
    from random import randint
    while len(tap_gia_tri) < SO_PHAN_TU:
        gt = randint (1,100) #Lấy 10 phần tử không trùng nhau nên dùng tập hợp
        tap_gia_tri.add(gt)
    #while
    #tap_gia_tri = list(tap_gia_tri) #phát sinh danh sách ngẫu nhiên
    tap_gia_tri = [66,46,84,11,81, 99,36,77,83, 87,100, 86, 85]
    print('Chèn lần lượt', tap_gia_tri)
    for x in tap_gia_tri:
        cay.chen(x)
    kq = cay.duyet_trai_nut_phai()
    print('*******Duyệt cây theo Trai - Nut - Phai (LNR):', kq)
    
    kq = cay.duyet_nut_trai_phai()
    print('*******Duyệt cây theo Nut - Trai - Phai (NLR):', kq)
    
    kq = cay.duyet_trai_phai_nut()
    print('*******Duyệt cây theo Trai - Phai - Nut (LRN):', kq)
    print('*******Xóa 1 phần tử có trong cây: ')
    gt = int(input('Nhập vào giá trị cần xóa'))
    print(f'Xoa {gt}')
    cay.xoa(gt)
    kq = cay.duyet_trai_nut_phai()
    print('*******Duyệt cây theo Trai - Nut - Phai (LNR):', kq)
    
    kq = cay.duyet_nut_trai_phai()
    print('*******Duyệt cây theo Nut - Trai - Phai (NLR):', kq)
    
    kq = cay.duyet_trai_phai_nut()
    print('*******Duyệt cây theo Trai - Phai - Nut (LRN):', kq)
    #tìm
    while True:
        nhap = input('Nhập vào khóa cần tìm')
        if nhap == '':
            break
        #if
        gt = int(nhap)
        kq = cay.tim(gt)
        if kq == None:
            print(f'Không tìm thấy {gt}')
        else: #tìm thấy
            print(f'Tìm thấy {gt}:{kq}')
        #if
    #while
#def
if __name__=='__main__':
    main()
    #if                        