class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def kiem_tra_cay_rong(root):
    return root is None

def la_node(root):
    return root.left is None and root.right is None

def la_node_co_gia_tri(root, value):
    if root is None:
        return False
    if root.data == value and la_node(root):
        return True
    return False

def la_node_cha(root, node):
    if root is None:
        return False
    if (root.left == node or root.right == node):
        return True
    return False

def chieu_cao_cay(root):
    if root is None:
        return 0
    else:
        left_height = chieu_cao_cay(root.left)
        right_height = chieu_cao_cay(root.right)
        return max(left_height, right_height) + 1

def dem_so_nut(root):
    if root is None:
        return 0
    else:
        return 1 + dem_so_nut(root.left) + dem_so_nut(root.right)

def duyet_tien_tu(root):
    if root:
        print(root.data, end=" ")
        duyet_tien_tu(root.left)
        duyet_tien_tu(root.right)

def duyet_trung_tu(root):
    if root:
        duyet_trung_tu(root.left)
        print(root.data, end=" ")
        duyet_trung_tu(root.right)

def duyet_hau_tu(root):
    if root:
        duyet_hau_tu(root.left)
        duyet_hau_tu(root.right)
        print(root.data, end=" ")

def dem_so_nut_la(root):
    if root is None:
        return 0
    elif root.left is None and root.right is None:
        return 1
    else:
        return dem_so_nut_la(root.left) + dem_so_nut_la(root.right)

def dem_so_nut_trung_gian(root):
    if root is None:
        return 0
    elif root.left is not None or root.right is not None:
        return 1 + dem_so_nut_trung_gian(root.left) + dem_so_nut_trung_gian(root.right)
    else:
        return 0

def tim_gia_tri_lon_nhat(root):
    if root is None:
        return float('-inf')
    max_left = tim_gia_tri_lon_nhat(root.left)
    max_right = tim_gia_tri_lon_nhat(root.right)
    return max(root.data, max_left, max_right)

def tim_gia_tri_nho_nhat(root):
    if root is None:
        return float('inf')
    min_left = tim_gia_tri_nho_nhat(root.left)
    min_right = tim_gia_tri_nho_nhat(root.right)
    return min(root.data, min_left, min_right)

def tong_gia_tri_cac_nut(root):
    if root is None:
        return 0
    return root.data + tong_gia_tri_cac_nut(root.left) + tong_gia_tri_cac_nut(root.right)

def trung_binh_gia_tri_cac_nut(root):
    count = dem_so_nut(root)
    if count == 0:
        return 0
    return tong_gia_tri_cac_nut(root) / count
def main():
    # Tạo cây nhị phân
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    root.left.left = Node(3)
    root.left.right = Node(7)
    root.right.right = Node(20)

    print("Cây nhị phân:")
    duyet_tien_tu(root)
    print("\n")

    # Kiểm tra cây rỗng
    if kiem_tra_cay_rong(root):
        print("Cây nhị phân rỗng.")
    else:
        print("Cây nhị phân không rỗng.")

    # Kiểm tra nút lá
    node = root.left.left
    if la_node(node):
        print(f"Node {node.data} là nút lá.")
    else:
        print(f"Node {node.data} không phải là nút lá.")

    # Kiểm tra nút cha
    node_n = root.left
    node_m = root.left.left
    if la_node_cha(node_n, node_m):
        print(f"Node {node_n.data} là nút cha của node {node_m.data}.")
    else:
        print(f"Node {node_n.data} không phải là nút cha của node {node_m.data}.")

    # Tính chiều cao của cây
    height = chieu_cao_cay(root)
    print(f"Chiều cao của cây: {height}")

    # Tính số nút của cây
    num_nodes = dem_so_nut(root)
    print(f"Số nút của cây: {num_nodes}")

    # Duyệt các loại
    print("Duyệt tiền tự:")
    duyet_tien_tu(root)
    print("\nDuyệt trung tự:")
    duyet_trung_tu(root)
    print("\nDuyệt hậu tự:")
    duyet_hau_tu(root)
    print("\n")

    # Đếm số nút lá
    leaf_count = dem_so_nut_la(root)
    print(f"Số nút lá của cây: {leaf_count}")

    # Đếm số nút trung gian
    intermediate_count = dem_so_nut_trung_gian(root)
    print(f"Số nút trung gian của cây: {intermediate_count}")

    # Tìm giá trị lớn nhất
    max_value = tim_gia_tri_lon_nhat(root)
    print(f"Giá trị lớn nhất của cây: {max_value}")

    # Tìm giá trị nhỏ nhất
    min_value = tim_gia_tri_nho_nhat(root)
    print(f"Giá trị nhỏ nhất của cây: {min_value}")

    # Tính tổng giá trị các nút
    sum_value = tong_gia_tri_cac_nut(root)
    print(f"Tổng giá trị các nút của cây: {sum_value}")

    # Tính trung bình giá trị các nút
    average_value = trung_binh_gia_tri_cac_nut(root)
    print(f"Trung bình giá trị các nút của cây: {average_value}")

if __name__ == "__main__":
    main()
