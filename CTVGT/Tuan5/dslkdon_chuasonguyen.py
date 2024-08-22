class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class DSLK:
    def __init__(self):
        self.head = None

    def them_cuoi(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def them_truoc(self, data, prev_data):
        new_node = Node(data)
        if not self.head:
            print("Danh sách rỗng. Không thể thêm trước.")
            return
        if self.head.data == prev_data:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        while current.next:
            if current.next.data == prev_data:
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        print("Không tìm thấy giá trị", prev_data, "trong danh sách.")

    def in_ds(self):
        current = self.head
        if not current:
            print("Danh sách rỗng.")
            return
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def in_ds_nguoc(self, node):
        if not node:
            return
        self.in_ds_nguoc(node.next)
        print(node.data, end=" ")

    def tim_gtln_gttn(self):
        if not self.head:
            print("Danh sách rỗng.")
            return
        max_val = self.head.data
        min_val = self.head.data
        current = self.head.next
        while current:
            if current.data > max_val:
                max_val = current.data
            if current.data < min_val:
                min_val = current.data
            current = current.next
        print("Giá trị lớn nhất trong danh sách:", max_val)
        print("Giá trị nhỏ nhất trong danh sách:", min_val)

    def tinh_tong_am_duong(self):
        if not self.head:
            print("Danh sách rỗng.")
            return
        sum_positive = 0
        sum_negative = 0
        current = self.head
        while current:
            if current.data > 0:
                sum_positive += current.data
            elif current.data < 0:
                sum_negative += current.data
            current = current.next
        print("Tổng số dương trong danh sách:", sum_positive)
        print("Tổng số âm trong danh sách:", sum_negative)

    def tinh_tich(self):
        if not self.head:
            print("Danh sách rỗng.")
            return
        product = 1
        current = self.head
        while current:
            product *= current.data
            current = current.next
        print("Tích các số trong danh sách:", product)

    def tinh_tong_binh_phuong(self):
        if not self.head:
            print("Danh sách rỗng.")
            return
        sum_square = 0
        current = self.head
        while current:
            sum_square += current.data ** 2
            current = current.next
        print("Tổng bình phương các số trong danh sách:", sum_square)

    def la_so_nguyen_to(self, x):
        if not self.head:
            print("Danh sách rỗng.")
            return
        current = self.head
        print("Các số nguyên tố của", x, "trong danh sách là:")
        while current:
            if self.kiem_tra_so_nguyen_to(current.data):
                print(current.data, end=" ")
            current = current.next
        print()

    def uoc_so(self, x):
        if not self.head:
            print("Danh sách rỗng.")
            return
        current = self.head
        print("Các ước số của", x, "trong danh sách là:")
        while current:
            if x % current.data == 0:
                print(current.data, end=" ")
            current = current.next
        print()

    def tim_gt_dau_tien_lon_hon_x(self, x):
        if not self.head:
            print("Danh sách rỗng.")
            return
        current = self.head
        while current:
            if current.data > x:
                print("Giá trị đầu tiên lớn hơn", x, "trong danh sách là:", current.data)
                return
            current = current.next
        print("Không có giá trị nào trong danh sách lớn hơn", x)

    def so_nguyen_to_cuoi_cung(self):
        if not self.head:
            print("Danh sách rỗng.")
            return
        last_prime = None
        current = self.head
        while current:
            if self.kiem_tra_so_nguyen_to(current.data):
                last_prime = current.data
            current = current.next
        if last_prime:
            print("Số nguyên tố cuối cùng trong danh sách:", last_prime)
        else:
            print("Trong danh sách không có số nguyên tố.")

    def dem_so_nguyen_to(self):
        if not self.head:
            print("Danh sách rỗng.")
            return
        count = 0
        current = self.head
        while current:
            if self.kiem_tra_so_nguyen_to(current.data):
                count += 1
            current = current.next
        print("Số lượng số nguyên tố trong danh sách là:", count)

    def kiem_tra_sap_tang(self):
        if not self.head:
            print("Danh sách rỗng.")
            return True
        current = self.head
        while current.next:
            if current.data > current.next.data:
                return False
            current = current.next
        return True

    def kiem_tra_doi_xung(self):
        if not self.head:
            print("Danh sách rỗng.")
            return False
        current = self.head
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        return elements == elements[::-1]

    def xoa_cuoi(self):
        if not self.head:
            print("Danh sách rỗng, không có phần tử để xóa.")
            return
        if not self.head.next:
            self.head = None
            return
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None

    def xoa_dau(self):
        if not self.head:
            print("Danh sách rỗng, không có phần tử để xóa.")
            return
        self.head = self.head.next

    def huy_danh_sach(self):
        self.head = None

    def kiem_tra_so_nguyen_to(self, num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

# Hàm main để thực hiện các thao tác từ menu
def main():
    danh_sach = DSLK()
    while True:
        print("\nChọn chức năng:")
        print("1. Thêm một số vào cuối danh sách")
        print("2. Thêm một số vào trước một số khác")
        print("3. In danh sách")
        print("4. In danh sách theo thứ tự ngược")
        print("5. Tìm giá trị lớn nhất và nhỏ nhất trong danh sách")
        print("6. Tính tổng số âm và số dương trong danh sách")
        print("7. Tính tích các số trong danh sách")
        print("8. Tính tổng bình phương các số trong danh sách")
        print("9. Nhập x, xuất các số là số nguyên tố của x")
        print("10. Nhập x, xuất các số là ước số của x")
        print("11. Nhập x, tìm giá trị đầu tiên trong danh sách lớn hơn x")
        print("12. Xuất số nguyên tố cuối cùng trong danh sách")
        print("13. Đếm số lượng số nguyên tố trong danh sách")
        print("14. Kiểm tra xem danh sách có được sắp tăng không")
        print("15. Kiểm tra xem danh sách có các phần tử đối xứng hay không")
        print("16. Xóa phần tử cuối cùng")
        print("17. Xóa phần tử đầu tiên")
        print("18. Hủy toàn bộ danh sách")
        print("19. Kết thúc chương trình")

        choice = int(input("Nhập lựa chọn (1-19): "))

        if choice == 1:
            num = int(input("Nhập số cần thêm vào cuối danh sách: "))
            danh_sach.them_cuoi(num)
        elif choice == 2:
            num = int(input("Nhập số cần thêm vào danh sách: "))
            prev_num = int(input("Nhập số trước đó trong danh sách: "))
            danh_sach.them_truoc(num, prev_num)
        elif choice == 3:
            print("Danh sách:")
            danh_sach.in_ds()
        elif choice == 4:
            print("Danh sách theo thứ tự ngược:")
            danh_sach.in_ds_nguoc(danh_sach.head)
            print()
        elif choice == 5:
            danh_sach.tim_gtln_gttn()
        elif choice == 6:
            danh_sach.tinh_tong_am_duong()
        elif choice == 7:
            danh_sach.tinh_tich()
        elif choice == 8:
            danh_sach.tinh_tong_binh_phuong()
        elif choice == 9:
            x = int(input("Nhập x: "))
            danh_sach.la_so_nguyen_to(x)
        elif choice == 10:
            x = int(input("Nhập x: "))
            danh_sach.uoc_so(x)
        elif choice == 11:
            x = int(input("Nhập x: "))
            danh_sach.tim_gt_dau_tien_lon_hon_x(x)
        elif choice == 12:
            danh_sach.so_nguyen_to_cuoi_cung()
        elif choice == 13:
            danh_sach.dem_so_nguyen_to()
        elif choice == 14:
            if danh_sach.kiem_tra_sap_tang():
                print("Danh sách đã được sắp tăng.")
            else:
                print("Danh sách chưa được sắp tăng.")
        elif choice == 15:
            if danh_sach.kiem_tra_doi_xung():
                print("Danh sách có các phần tử đối xứng.")
            else:
                print("Danh sách không có các phần tử đối xứng.")
        elif choice == 16:
            danh_sach.xoa_cuoi()
            print("Đã xóa phần tử cuối cùng khỏi danh sách.")
        elif choice == 17:
            danh_sach.xoa_dau()
            print("Đã xóa phần tử đầu tiên khỏi danh sách.")
        elif choice == 18:
            danh_sach.huy_danh_sach()
            print("Đã hủy toàn bộ danh sách.")
        elif choice == 19:
            print("Kết thúc chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Hãy nhập lại.")

if __name__ == "__main__":
    main()
