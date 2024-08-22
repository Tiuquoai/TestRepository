import Rectangle as rect

menu_options = { 
    1: 'Thêm mới hình chữ nhật', 
    2: 'Hiển thị danh sách hình chữ nhật', 
    3: 'Tính tổng diện tích các hình chữ nhật', 
    4: 'Hiển thị các hình chữ nhật có chu vi nhỏ nhất',
    'Others': 'Thoát chương trình' 
} 

def print_menu(): 
    for key, value in menu_options.items(): 
        print(key, '--', value) 
 
dsHCN = [] 
 
while True: 
    print_menu() 
    userChoice = input('Nhập tùy chọn: ')
    
    try: 
        userChoice = int(userChoice) 
    except ValueError: 
        print('Nhập sai định dạng, hãy nhập lại.....') 
        continue
    
    if userChoice == 1: 
        cr = float(input("Nhập chiều rộng: ")) 
        cd = float(input("Nhập chiều dài: "))
        hcn = rect.Rectangle(cr, cd) 
        dsHCN.append(hcn) 
    elif userChoice == 2: 
        for item in dsHCN: 
            item.display() 
    elif userChoice == 3: 
        dientich = sum(item.area() for item in dsHCN) 
        print(f'Tổng diện tích là: {dientich}')  
    elif userChoice == 4: 
        if len(dsHCN) == 0: 
            print('Danh sách rỗng') 
        else: 
            chuvinn = dsHCN[0].perimeter() 
            for item in dsHCN: 
                if chuvinn > item.perimeter(): 
                    chuvinn = item.perimeter() 
            for item in dsHCN: 
                if item.perimeter() == chuvinn: 
                    item.display() 
    else: 
        print('Thoát chương trình BYE BYE') 
        break
