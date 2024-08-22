import hinhchunhat as rect

menu_options = {
    1: 'thêm mới hình chữu nhật',
    2: 'hiển thị danh sách hình chữ nhật',
    3: 'tính tổng diện tích các hình chữ nhật',
    4: 'hiển thị cá hình chữu nhật có chu vi nhỏ nhất',
    'Others': 'thoát khỏi chương trình' 
}

def print_menu():
    for key in menu_options.key(): 
        print (key, '--', menu_options[key])        
        
dsHCN = []     

while(True):    
        print_menu()
        userChoice = ''
        try:   
            userChoice = int(input('nhap tuy chon: '))
        except:   
            print('nhap sai dinh dang, hay nhap lai ...')
            continue      
        
        if userChoice == 1:      
            cr = float(input("nhap chieu rong: "))
            cd = float(input("nhap chieu dai: "))
            
            hcn = rect.hinhchunhat(cr, cd)
            dsHCN.append(hcn)
        elif userChoice == 2:   
            for item in dsHCN:    
                item.display()
        elif userChoice == 3:       
            dientich = 0.0
            for item in dsHCN:
                dientich = dientich + item.area()
            print(f'tong dien tich la: {dientich}')
        elif userChoice == 4:    
            if dsHCN.count == 0:     
                print('danh sach rong')
            else:    
                chuvinn = dsHCN[0].perimeter()
                for item in dsHCN:    
                    if chuvinn > item.perimeter():   
                        chuvinn = item.perimeter()
                for item in dsHCN:    
                    if item.perimeter() == chuvinn:   
                        item.display()
        else:    
            print('thoat chuong trinh BYE BYE')
            break