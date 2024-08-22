class Node:
    def __init__(self, char):
        self.char = char
        self.count = 1
        self.left = None
        self.right = None

class CayTanSoKyTu:
    def __init__(self):
        self.root = None

    def chen(self, char):
        if self.root is None:
            self.root = Node(char)
        else:
            self._chen(char, self.root)

    def _chen(self, char, node):
        if char == node.char:
            node.count += 1
        elif char < node.char:
            if node.left is None:
                node.left = Node(char)
            else:
                self._chen(char, node.left)
        else:
            if node.right is None:
                node.right = Node(char)
            else:
                self._chen(char, node.right)

    def xay_dung_cay_tu_van_ban(self, van_ban):
        for char in van_ban:
            if char.isalpha():
                self.chen(char.lower())  

    def dem_so_lan_xuat_hien(self, char):
        return self._dem_so_lan_xuat_hien(char, self.root) if self.root else 0

    def _dem_so_lan_xuat_hien(self, char, node):
        if node is None:
            return 0
        elif char == node.char:
            return node.count
        elif char < node.char:
            return self._dem_so_lan_xuat_hien(char, node.left)
        else:
            return self._dem_so_lan_xuat_hien(char, node.right)

def main():
    van_ban = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
    cay_tan_so_ky_tu = CayTanSoKyTu()
    cay_tan_so_ky_tu.xay_dung_cay_tu_van_ban(van_ban)

    print("Thống kê số lần xuất hiện của mỗi ký tự:")
    for char in "abcdefghijklmnopqrstuvwxyz":
        count = cay_tan_so_ky_tu.dem_so_lan_xuat_hien(char)
        if count > 0:
            print(f"'{char}': {count}")

    while True:
        input_char = input("Nhập ký tự để kiểm tra số lần xuất hiện (Nhập 'q' để thoát): ").lower()
        if input_char == 'q':
            break
        elif not input_char.isalpha():
            print("Vui lòng chỉ nhập ký tự chữ cái!")
            continue
        count = cay_tan_so_ky_tu.dem_so_lan_xuat_hien(input_char)
        print(f"Ký tự '{input_char}' xuất hiện {count} lần trong văn bản.")

if __name__ == "__main__":
    main()
