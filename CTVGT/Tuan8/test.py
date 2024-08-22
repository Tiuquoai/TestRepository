def cong(a, b):
    return a + b

def tru(a, b):
    return a - b

def nhan(a, b):
    return a * b

def chia(a, b):
    return a / b

# Ví dụ sử dụng các phép toán
x = 5
y = 3

tong = cong(x, y)
hieu = tru(x, y)
tich = nhan(x, y)
thuong = chia(x, y)

print("Tổng:", tong)
print("Hiệu:", hieu)
print("Tích:", tich)
print("Thương:", thuong)