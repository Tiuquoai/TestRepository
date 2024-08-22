class IdValue:
    def __init__(self, id, value):
        self.id = id
        self.value = value

class IdValueNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class DanhSachSinhVien:
    def __init__(self):
        self.head = None
        self.tail = None

    def rong(self):
        return self.head is None

    def trung_lap(self, id):
        current = self.head
        while current:
            if current.data.id == id:
                return True
            current = current.next
        return False

    def them_cuoi(self, newdata):
        new_node = IdValueNode(newdata)
        if self.rong():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def them_dau(self, newdata):
        new_node = IdValueNode(newdata)
        if self.rong():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def xuat_danh_sach(self):
        current = self.head
        while current:
            print(f"ID: {current.data.id}, Value: {current.data.value}")
            current = current.next

    def so_luong_tac_gia(self, tac_gia):
        count = 0
        current = self.head
        while current:
            if tac_gia in current.data.value:
                count += 1
            current = current.next
        return count

    def sach_nxb_trong_nam(self, nxb, nam):
        sach = []
        current = self.head
        while current:
            if current.data.value == nxb and current.data.nam_xuat_ban == nam:
                sach.append(current.data)
            current = current.next
        return sach

    def tim_sach_theo_ten(self, ten_sach):
        current = self.head
        while current:
            if current.data.value.lower() == ten_sach.lower():
                return current.data
            current = current.next
        return None

    def xoa_dau(self):
        if self.rong():
            return "Danh sách rỗng, không thể xóa."
        else:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next

    def xoa_cuoi(self):
        if self.rong():
            return "Danh sách rỗng, không thể xóa."
        else:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                current = self.head
                while current.next != self.tail:
                    current = current.next
                current.next = None
                self.tail = current

    def xoa_theo_ten(self, ten_sach):
        if self.rong():
            return "Danh sách rỗng, không thể xóa."
        else:
            if self.head.data.value.lower() == ten_sach.lower():
                return self.xoa_dau()
            else:
                prev = None
                current = self.head
                while current:
                    if current.data.value.lower() == ten_sach.lower():
                        if current == self.tail:
                            return self.xoa_cuoi()
                        else:
                            prev.next = current.next
                            return f"Sách '{ten_sach}' đã được xóa khỏi danh sách."
                    prev = current
                    current = current.next
                return f"Sách '{ten_sach}' không tồn tại trong danh sách."

# Test code
if __name__ == "__main__":
    # Tạo một danh sách sinh viên
    danh_sach_sv = DanhSachSinhVien()

    # Thêm một số sinh viên vào danh sách
    sv1 = IdValue("SV001", "Nguyen Van A")
    sv2 = IdValue("SV002", "Tran Thi B")
    sv3 = IdValue("SV003", "Le Van C")

    danh_sach_sv.them_cuoi(sv1)
    danh_sach_sv.them_cuoi(sv2)
    danh_sach_sv.them_cuoi(sv3)

    # In danh sách sinh viên
    print("Danh sách sinh viên:")
    danh_sach_sv.xuat_danh_sach()

    # Kiểm tra trùng lặp
    print("Có trùng lặp với ID 'SV002':", danh_sach_sv.trung_lap("SV002"))  # Kết quả: True
    print("Có trùng lặp với ID 'SV004':", danh_sach_sv.trung_lap("SV004"))  # Kết quả: False
