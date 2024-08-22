class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class DanhSachLienKetDon:
    def __init__(self):
        self.head = None

    def them_phan_tu(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def dem_so_phan_tu(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def tinh_tong(self):
        tong = 0
        current = self.head
        while current:
            tong += current.data
            current = current.next
        return tong

    def tim_max(self):
        if not self.head:
            return None
        max_val = self.head.data
        current = self.head.next
        while current:
            if current.data > max_val:
                max_val = current.data
            current = current.next
        return max_val

    def tim_min(self):
        if not self.head:
            return None
        min_val = self.head.data
        current = self.head.next
        while current:
            if current.data < min_val:
                min_val = current.data
            current = current.next
        return min_val

    def sap_xep(self):
        current = self.head
        values = []
        while current:
            values.append(current.data)
            current = current.next
        values.sort()
        sorted_list = DanhSachLienKetDon()
        for value in values:
            sorted_list.them_phan_tu(value)
        return sorted_list

# Hàm chính
if __name__ == "__main__":
    danh_sach = DanhSachLienKetDon()
    while True:
        try:
            data = input("Nhập số nguyên (để dừng nhập, nhấn Enter khi trống): ")
            if data == "":
                break
            data = int(data)
            danh_sach.them_phan_tu(data)
        except ValueError:
            print("Nhập không hợp lệ. Vui lòng nhập lại.")

    print("1. Số lượng các phần tử trong danh sách:", danh_sach.dem_so_phan_tu())
    print("2. Tổng giá trị của các số trong danh sách:", danh_sach.tinh_tong())
    print("3. Giá trị lớn nhất trong danh sách:", danh_sach.tim_max())
    print("4. Giá trị nhỏ nhất trong danh sách:", danh_sach.tim_min())
    danh_sach_sap_xep = danh_sach.sap_xep()
    print("5. Danh sách sau khi sắp xếp theo thứ tự tăng dần:")
    current = danh_sach_sap_xep.head
    while current:
        print(current.data, end=" ")
        current = current.next
