class Node:
    def __init__(self, key):
        self.key = key
        self.count = 1
        self.left = None
        self.right = None

def chen_vao_cay(root, key):
    if root is None:
        return Node(key)
    
    if key < root.key:
        root.left = chen_vao_cay(root.left, key)
    elif key > root.key:
        root.right = chen_vao_cay(root.right, key)
    else:
        root.count += 1
    
    return root

def xay_dung_cay(van_ban):
    root = None
    for char in van_ban:
        if char.isalpha():
            char = char.lower()
            root = chen_vao_cay(root, char)
    return root

def dem_ky_tu(root, kytu):
    if root is None:
        return 0
    
    if kytu < root.key:
        return dem_ky_tu(root.left, kytu)
    elif kytu > root.key:
        return dem_ky_tu(root.right, kytu)
    else:
        return root.count

def dem_gia_tri_doc_lap(arr):
    root = None
    for num in arr:
        root = chen_vao_cay(root, num)
    
    return dem_dinh(root)

def dem_dinh(root):
    if root is None:
        return 0
    return 1 + dem_dinh(root.left) + dem_dinh(root.right)

def dem_phan_tu(root, key):
    if root is None:
        return 0
    
    if key < root.key:
        return dem_phan_tu(root.left, key)
    elif key > root.key:
        return dem_phan_tu(root.right, key)
    else:
        return root.count

if __name__ == "__main__":
    van_ban = input("Nhap vao van ban: ")
    cay = xay_dung_cay(van_ban)
    kytu_can_kiem_tra = input("Nhap ky tu can kiem tra: ").lower()
    print(f"So lan xuat hien cua ky tu '{kytu_can_kiem_tra}' trong van ban: {dem_ky_tu(cay, kytu_can_kiem_tra)}")

    chuoi_so = input("Nhap day so, cach nhau bang khoang trang: ").split()
    chuoi_so = [int(num) for num in chuoi_so]
    cay = xay_dung_cay(chuoi_so)
    print("So gia tri phan biet trong day so:", dem_gia_tri_doc_lap(chuoi_so))
    print("So luong phan tu cua moi gia tri phan biet:")
    for num in chuoi_so:
        if dem_phan_tu(cay, num) == 1:
            print(f"{num}: {dem_phan_tu(cay, num)} lan")