#tạo đối tượng bảng băm
#thêm vào bảng băm các giá trị ngẫu nhiên [khóa, giá trị] vào bảng băm, xuất chuỗi mô tả bảng băm sau mỗi lần thêm
#nhập vào 1 dãy khóa, lấy và xuất ra giá trị tương ứng với khóa đó trong bảng băm
def main():
    bang_bam = dict() 
    import random
    for i in range (18):
        khoa = random.randint(0,10)
        gia_tri = random.randint(0,100)
        print(f'them khoa = {khoa}, gia tri = {gia_tri}')
        bang_bam[khoa] = gia_tri
        print(bang_bam)
        print()

    new_khoa = int(input('Nhap vao mot khoa: '))
    gia_tri = bang_bam[khoa]
    print(f"Gia tri cua khoa {khoa} la {gia_tri}")
if __name__== "__main__":
    main()
