import random
import time

# Phương pháp Đổi chỗ trực tiếp (Interchange sort)
def interchange_sort(arr):
    comparisons = 0
    swaps = 0
    n = len(arr)
    for i in range(n - 1):
        for j in range(i + 1, n):
            comparisons += 1
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                swaps += 1
    return comparisons, swaps

# Phương pháp Nổi bọt (Bubble sort)
def bubble_sort(arr):
    comparisons = 0
    swaps = 0
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
    return comparisons, swaps

# Phương pháp Chèn trực tiếp (Insertion sort)
def insertion_sort(arr):
    comparisons = 0
    swaps = 0
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        comparisons += 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            swaps += 1
            comparisons += 1
        arr[j + 1] = key
    return comparisons, swaps

# Phương pháp Chọn trực tiếp (Selection sort)
def selection_sort(arr):
    comparisons = 0
    swaps = 0
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        swaps += 1
    return comparisons, swaps

# Phương pháp dựa trên phân hoạch (Quick sort)
def quick_sort(arr):
    comparisons = 0
    swaps = 0
    
    def partition(arr, low, high):
        nonlocal comparisons, swaps
        i = low - 1
        pivot = arr[high]
        for j in range(low, high):
            comparisons += 1
            if arr[j] <= pivot:
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]
                swaps += 1
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        swaps += 1
        return i + 1
    
    def quick_sort_recursive(arr, low, high):
        nonlocal comparisons, swaps
        if low < high:
            pi = partition(arr, low, high)
            quick_sort_recursive(arr, low, pi - 1)
            quick_sort_recursive(arr, pi + 1, high)
    
    n = len(arr)
    quick_sort_recursive(arr, 0, n - 1)
    return comparisons, swaps


# Phát sinh mảng số nguyên
array = [random.randint(1, 1000) for _ in range(50000)] #thay số nhỏ để chạy 

# Lưu mảng vào tập tin mang1.int
with open('mang1.int', 'w') as file:
    file.write('\n'.join(str(num) for num in array))

# Đo thời gian chạy và số lần so sánh, hoán vị cho từng thuật toán sắp xếp
start_time = time.time()
interchange_comparisons, interchange_swaps = interchange_sort(array.copy())
interchange_time = time.time() - start_time

start_time = time.time()
bubble_comparisons, bubble_swaps = bubble_sort(array.copy())
bubble_time = time.time() - start_time

start_time = time.time()
insertion_comparisons, insertion_swaps = insertion_sort(array.copy())
insertion_time = time.time() - start_time

start_time = time.time()
selection_comparisons, selection_swaps = selection_sort(array.copy())
selection_time = time.time() - start_time

start_time = time.time()
quick_comparisons, quick_swaps = quick_sort(array.copy())
quick_time = time.time() - start_time

# In kết quả
print("Độ phức tạp của các thuật toán sắp xếp")
print()
print("Phương pháp sắp xếp")
print("1. Phương pháp Đổi chỗ trực tiếp (Interchange sort)")
print("Thời gian chạy (mili giây):", interchange_time * 1000)
print("Số lần so sánh (lệnh if):", interchange_comparisons)
print("Số lần hoán vị:", interchange_swaps)
print()
print("2. Phương pháp Nổi bọt (Bubble sort)")
print("Thời gian chạy (mili giây):", bubble_time * 1000)
print("Số lần so sánh (lệnh if):", bubble_comparisons)
print("Số lần hoán vị:", bubble_swaps)
print()
print("3. Phương pháp Chèn trực tiếp (Insertion sort)")
print("Thời gian chạy (mili giây):", insertion_time * 1000)
print("Số lần so sánh (lệnh if):", insertion_comparisons)
print("Số lần hoán vị:", insertion_swaps)
print()
print("4. Phương pháp Chọn trực tiếp (Selection sort)")
print("Thời gian chạy (mili giây):", selection_time * 1000)
print("Số lần so sánh (lệnh if):", selection_comparisons)
print("Số lần hoán vị:", selection_swaps)
print()
print("5. Phương pháp dựa trên phân hoạch (Quick sort)")
print("Thời gian chạy (mili giây):", quick_time * 1000)
print("Số lần so sánh (lệnh if):", quick_comparisons)
print("Số lần hoán vị:", quick_swaps)