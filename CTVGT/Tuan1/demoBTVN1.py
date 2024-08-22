import matplotlib_inline as plt         
import Employee as emp        

menu_options = {
    1: 'Load data from file',
    2: 'Add new employee',
    3: 'Display list of employee',
    4: 'Show employee details',
    5: 'Update employee information',
    6: 'Delete employee',
    7: 'Increase salary of employee',
    8: 'Decrease salary of employee',
    9: 'Show total employee a month',
    10: 'Show total salary a month',
    11: 'Show average of salary a month',
    12: 'Show average of age',
    13: 'Show maximum age',
    14: 'Sort list of employee according to salary by ascending',
    15: 'Draw salary according to age',
    16: 'Draw average of salary chart by age group',
    17: 'Draw percentage of salary by age group',
    18: 'Draw percentage of total employee by age group',
    19: 'Store data to file',
    'Others': 'Exit program'
}

def print_menu():
    for key in menu_options.keys(): 
        print (key, '--', menu_options[key])
        
# Khai báo biển lưu trữ những nhân viên
dsNhanVien = []

while(True):
        print_menu()
        userChoice = ''
        try:
            userChoice = int(input('Input choice: '))
        except:
            print('Invalid input, try again')
            continue
        #Check what choice was entered and act accordingly
        if userChoice == 1:
            fr = open('dbemp_input.db',mode='r',encoding='utf-8')
            for line in fr:
                stripLine = line.strip('\n')
                ds = stripLine.split(',')
                maso = ds[0]
                ten = ds[1]
                tuoi = int(ds[2])
                luong = float (ds[3])
                nv = emp.Employee (maso, ten, tuoi, luong) 
                dsNhanVien.append(nv)
            fr.close()
        elif userChoice == 2:
            maso = input("Input code: ")
            ten = input("Input name: ")
            tuoi = int(input("Input age: "))
            luong = float(input("Input salary: "))
            nv = emp.Employee (maso, ten, tuoi, luong) 
            dsNhanVien.append(nv)
        elif userChoice == 3:
            if dsNhanVien.count==0: 
                print('Danh sach rong')
            else:
                for item in dsNhanVien:
                    item.display()
        elif userChoice == 4:
        #4:Show employee details
            if dsNhanVien.count==0: 
                print('Danh sach rong')
            else:
                ma = input("Input Code:")
                for item in dsNhanVien:
                    if(item.code ==ma): 
                        item.display()
        elif userChoice == 5:
        #5: Update employee information
            if dsNhanVien.count==0: 
                print('Danh sach rong')
            else:
                ma =input("Input Code for Update:")
                for item in dsNhanVien:
                    if(item.code ==ma):
                        item.display()
                        menu={
                            1: 'Update Name',
                            2: 'Update Age',
                            3: 'Update luong',
                            'Others': 'Thoat'
                        }
                        def Xuat_menu():
                            for key in menu.keys():
                                print(key, '--', menu[key])
                        while (True):
                            Xuat_menu()
                            traloi=''
                            try:
                                traloi =int(input('Nhap cac tuy chon:'))
                            except:
                                print('Nhap sai dinh dang, nhap lai:')
                                continue
                            if traloi==1:
                                ten = input("Input name: ")
                                item.name =ten
                                item.display()
                            elif traloi ==2:
                                tuoi = int(input("Input age: "))
                                item.age =tuoi
                                item.display()
                            elif traloi ==3:
                                luong = int(input("Input salary: "))
                                item.salary =luong
                                item.display()
                            else:
                                print('Ket thuc chinh sua')
                                break
                            
        elif userChoice == 6:
        #6: 'Delete employee'
            if dsNhanVien.count==0:
                print('Danh sach rong')
            else:
                ma = input("Input Code for Delete:")
                for item in dsNhanVien:
                    if(item.code ==ma):
                        item.display()
                        tl = input('Ban co chac chan xoa nhan vien nay khong Y/N?')
                        if tl =='Y':
                            #del item
                            dsNhanVien.remove(item)
            for item in dsNhanVien:
                    item.display()
        elif userChoice == 7:
        #7: Increase salary of employee
            if dsNhanVien.count==0:
                print('Danh sach rong')
            else:
                ma =input("Input Code for Increase:")
                for item in dsNhanVien:
                    if(item.code ==ma):
                        item.display()
                        luongtang = int(input('Nhap muc luong tang'))
                        item.salary = item.salary + luongtang
                        item.display()
        elif userChoice == 8:
        #8: Decrease salary of employee
            if dsNhanVien.count==0:
                print('Danh sach rong')
            else:
                ma =input("Input Code for Decrease:")
                for item in dsNhanVien:
                    if(item.code ==ma):
                        item.display()
                        luonggiam = int(input('Nhap muc luong giam'))
                        item.salary = item.salary -luonggiam
                        item.display()
        elif userChoice == 9:
        #9: 'Show total employee a month'
            if dsNhanVien.count==0:
                print('Danh sach rong')
            else:
                tongsnv=0
                for item in dsNhanVien:
                    tongsnv = tongsnv+1
                    item.display()
                print('Tong so nhan vien =', tongsnv)
        elif userChoice == 10:
            sumSalary = 0.0
            for item in dsNhanVien:
                sumSalary = sumSalary + item.salary
            print(f'Total salary: {sumSalary}')
        elif userChoice == 11:
            #11: 'Show average of salary a month'
            if dsNhanVien.count==0:
                print('Danh sach rong')
            else:
                tongsnv=0
                tongluong=0
                for item in dsNhanVien:
                    tongsnv = tongsnv+1
                    tongluong =tongluong +item.salary
                    item.display()
                luongtb = tongluong/tongsnv
                print(f'Luong trung binh nhan vien = {luongtb}')
        elif userChoice == 12:
            #12: 'Show average of age'
            if dsNhanVien.count==0:
                print('Danh sach rong')
            else:
                tongtuoi=0
                tongsnv=0
                for item in dsNhanVien:
                    tongsnv =tongsnv+1
                    tongtuoi = tongtuoi+item.age
                    item.display()
                tuoitb = tongtuoi/tongsnv
                print(f'Tuoi trung binh nhan vien = {tuoitb}') 
        elif userChoice == 13:
            #13: 'Show maximum age'
            if dsNhanVien.count==0:
                print('Danh sach rong')
            else:
                for item in dsNhanVien:
                    tuoimax=item.age
                    break
                for item in dsNhanVien:
                    if(item.age>tuoimax):
                        tuoimax = item.age
                print('Tuoi lon nhat =', tuoimax)
        elif userChoice == 14:
            #14: 'Sort list of employee according to salary by ascending'
            if dsNhanVien.count==0:
                print('Danh sach rong')
            else:
                tongsnv=0
                for item in dsNhanVien:
                    tongsnv = tongsnv+1
                    item.display()
                print('Tong so nhan vien = ',tongsnv)
        elif userChoice == 15:
            #Draw salary according to age
            arrTuoi = []
            arrLuong = []
            for item in dsNhanVien:
                arrTuoi.append(item.age)
                arrLuong.append(item.salary)
                
            # Vẽ đồ thị
            plt.figure(figsize=(15,5))
            
            plt.title("Age and salary chart")
            plt.xlabel("Ox: age")
            plt.ylabel("Oy: salary")
            
            plt.plot(arrTuoi, arrLuong, "go")
            plt.show()
        elif userChoice == 16:
            #16: 'Draw average of salary chart by age group',
            arrTuoi = []
            arrLuong = []
            for item in dsNhanVien:
                arrTuoi.append(item.age)
                arrLuong.append(item.salary)
            
            # Vẽ đồ thị
            plt.figure(figsize=(15,5))
            
            plt.title("Age and salary chart")
            plt.xlabel("Ox: age")
            plt.ylabel("Oy: salary")
            
            plt.plot(arrTuoi, arrLuong, "go")
            plt.show()
        elif userChoice == 17:
            #17: 'Draw percentage of salary by age group'
            arrTuoi = []
            arrLuong = []
            for item in dsNhanVien:
                arrTuoi.append(item.age)
                arrLuong.append(item.salary)
                
            # Vẽ đồ thị
            plt.figure(figsize=(15,5))
            
            plt.title("Age and salary chart")
            plt.xlabel("Ox: age")
            plt.ylabel("Oy: salary")
            
            plt.plot(arrTuoi, arrLuong, "go")
            plt.show()
        elif userChoice == 18:
            #18: 'Draw percentage of total employee by age group'
            arrTuoi = []
            arrLuong = []
            for item in dsNhanVien:
                arrTuoi.append(item.age)
                arrLuong.append(item.salary)
                
            # Vẽ đồ thị
            plt.figure(figsize=(15,5))
            
            plt.title("Age and salary chart")
            plt.xlabel("Ox: age")
            plt.ylabel("Oy: salary")
            
            plt.plot(arrTuoi, arrLuong, "go")
            plt.show()
        elif userChoice == 19:
            #19: 'Store data to file'
            arrTuoi = []
            arrLuong = []
            for item in dsNhanVien:
                for item in dsNhanVien:
                    arrTuoi.append(item.age)
                    arrLuong.append(item.salary)
                    
            # Vẽ đồ thị
            plt.figure(figsize=(15,5))
            
            plt.title("Age and salary chart")
            plt.xlabel("Ox: age")
            plt.ylabel("Oy: salary")
            
            plt.plot(arrTuoi, arrLuong, "go") 
            plt.show()
        else:
            print('BYE BYE')
            break
                                                                                