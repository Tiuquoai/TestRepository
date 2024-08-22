from dslk import *
def main():
    ds =DSLienKet()
    ds.in_ds()
    print('1.Thêm------------------')
    so =int(input("Nhập số cần thêm"))
    print(f'Them {so}')
    ds.them(so)
    ds.ion_ds()
    
    so =int(input("Nhập số cần thêm"))
    print(f'Them {so}')
    ds.them(so)
    ds.ion_ds()
    
    print('1.Chèn------------------')
    ds.in_ds()
    so =int(input("Nhập số cần thêm"))
    
    vt = 0
    print(f'Chen {so} vao vi tri {vt}')
    ds.chen(vt, so)
    ds.in_ds()
    so =int(input("Nhập số cần thêm"))
    #so = 15
    vt = 1
    print(f'Chen {so} vao vi tri {vt}')
    ds.chen(vt, so)
    ds.in_ds()
    so =int(input("Nhập số cần thêm"))
    #so = 17
    vt =int(input("Nhập vị trí cần thêm"))
    #vt = 3
    print(f'Chen {so} vao vi tri {vt}')
    ds.chen(vt, so)
    ds.in_ds()
    
    #c.Tìm:
    print('3.Tìm------------------')
    ds.in_ds()
    so =int(input("Nhập số cần tìm"))
    #so = 99
    print(f'Tim {so}')
    vt = ds.tim(so)
    print(f'So {so} tai vi tri {vt}')
    
    ds.in_ds()
    so =int(input("Nhập số cần tìm"))
    #so = 15
    print(f'Tim {so}')
    vt = ds.tim(so)
    print(f'So {so} tai vi tri {vt}')