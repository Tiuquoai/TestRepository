import time
import random

def generate_random_array(size):
    return [random.randint(0, 50) for _ in range(size)] #thay số 1000 nhỏ hơn để chạy nhanh hơn

def save_array_to_file(arr, filename):
    with open(filename, 'w') as file:
        for num in arr:
            file.write(f"{num}\n")

def bubble_sort(arr):
    compare = 0
    swap = 0
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            compare += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap += 1
    return compare, swap


def insertion_sort(arr):
    compare = 0
    swap = 0
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            compare += 1
            arr[j + 1] = arr[j]
            j -= 1
            swap += 1
        arr[j + 1] = key
    return compare, swap

def merge_sort(arr):
    compare = 0
    swap = 0
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            compare += 1
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
                swap += 1
            else:
                arr[k] = R[j]
                j += 1
                swap += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return compare, swap

def partition(arr, left, right):
    compare = 0
    swap = 0
    i = left - 1
    pivot = arr[right]
    for j in range(left, right):
        compare += 1
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            swap += 1
    arr[i+1], arr[right] = arr[right], arr[i+1]
    swap += 1
    return i+1, swap, compare

def quick_sort(arr, left, right):
    swap = 0
    compare = 0
    if left < right:
        pi, swap1, compare1 = partition(arr, left, right)
        swap += swap1
        compare += compare1
        swap_left, compare_left = quick_sort(arr, left, pi-1)
        swap_right, compare_right = quick_sort(arr, pi+1, right)
        swap += swap_left + swap_right
        compare += compare_left + compare_right
    return swap, compare
        
        
        

def selection_sort(arr):
    swaps = 0
    compare = 0
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            compare += 1
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            swaps += 1
    return swaps, compare

def heapify(arr, n, i, compare):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n:
        compare += 1
        if arr[l] > arr[largest]:
            largest = l

    if r < n:
        compare += 1
        if arr[r] > arr[largest]:
            largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        return heapify(arr, n, largest, compare + 1)
    
    return compare

def heap_sort(arr):
    n = len(arr)
    compare = 0
    swap = 0
    
    for i in range(n // 2 - 1, -1, -1):
        compare = heapify(arr, n, i, compare)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        swap += 1
        compare = heapify(arr, i, 0, compare)

    return swap, compare


def counting_sort(arr):
    max_val = max(arr)
    min_val = min(arr)
    range_of_elements = max_val - min_val + 1

    count_arr = [0 for _ in range(range_of_elements)]
    output_arr = [0 for _ in range(len(arr))]

    for i in range(len(arr)):
        count_arr[arr[i] - min_val] += 1

    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i - 1]

    for i in range(len(arr) - 1, -1, -1):
        output_arr[count_arr[arr[i] - min_val] - 1] = arr[i]
        count_arr[arr[i] - min_val] -= 1

    for i in range(len(arr)):
        arr[i] = output_arr[i]

def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    compare = 0
    swap = 0
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                compare += 1
                arr[j] = arr[j - gap]
                j -= gap
                swap += 1
            arr[j] = temp
        gap //= 2
    return compare, swap

def interchange_sort(arr):
    n = len(arr)
    compare = 0
    swap = 0
    for i in range(n):
        for j in range(i + 1, n):
            compare += 1
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                swap += 1
    return compare, swap


array_size = 100#thay 100 để chạy nhanh hơn

# Tạo mảng ngẫu nhiên
arr = generate_random_array(array_size)

# Lưu mảng vào file mang1.int
#save_array_to_file(arr, 'mang1.int')

# Bubble Sort
start_time = time.time()
n = bubble_sort(arr.copy())
end_time = time.time()
print("Bubble Sort Time:", end_time - start_time)
print("So lan so sanh va so lan hoan vi: ", n)
print('\n')

# Insertion Sort
start_time = time.time()
n = insertion_sort(arr.copy())
end_time = time.time()
print("Insertion Sort Time:", end_time - start_time)
print("So lan so sanh va so lan hoan vi: ", n)
print('\n')

# Merge Sort
start_time = time.time()
n = merge_sort(arr.copy())
end_time = time.time()
print("Merge Sort Time:", end_time - start_time)
print("So lan so sanh va so lan hoan vi: ", n)
print('\n')

# Quick Sort
start_time = time.time()
a = arr.copy()
n = quick_sort(a, 0, len(a)-1)
end_time = time.time()
print("Quick Sort Time:", end_time - start_time)
print("So lan so sanh va so lan hoan vi: ", n)
print('\n')

# Selection Sort
start_time = time.time()
n = selection_sort(arr.copy())
end_time = time.time()
print("Selection Sort Time:", end_time - start_time)
print("So lan so sanh va so lan hoan vi: ", n)
print('\n')

# Heap Sort
start_time = time.time()
n = heap_sort(arr.copy())
end_time = time.time()
print("Heap Sort Time:", end_time - start_time)
print("So lan so sanh va so lan hoan vi: ", n)
print('\n')

# Counting Sort
#start_time = time.time()
#counting_sort(arr.copy())
#end_time = time.time()
#print("Counting Sort Time:", end_time - start_time)

# Shell Sort
start_time = time.time()
n = shell_sort(arr.copy())
end_time = time.time()
print("Shell Sort Time:", end_time - start_time)
print("So lan so sanh va so lan hoan vi: ", n)
print('\n')

# Interchange Sort
start_time = time.time()
interchange_sort(arr.copy())
end_time = time.time()
print("Interchange Sort Time:", end_time - start_time)
print("So lan so sanh va so lan hoan vi: ", n)
print('\n')
