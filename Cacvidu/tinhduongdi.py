import itertools
import math

# Hàm tính khoảng cách giữa hai điểm
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Hàm tính tổng độ dài của hành trình
def total_distance(route, distance_matrix):
    return sum(distance_matrix[route[i]][route[i + 1]] for i in range(len(route) - 1))

# Hàm tìm đường đi ngắn nhất sử dụng thuật toán Nearest Neighbor và cải thiện bằng 2-opt
def tsp_nearest_neighbor(cities):
    # Tạo ma trận khoảng cách
    distance_matrix = [
        [distance(cities[i], cities[j]) for j in range(len(cities))]
        for i in range(len(cities))
    ]

    # Bắt đầu từ thành phố đầu tiên
    current_city = 0
    path = [current_city]
    unvisited = set(range(1, len(cities)))

    # Thuật toán Nearest Neighbor
    while unvisited:
        next_city = min(unvisited, key=lambda city: distance_matrix[current_city][city])
        unvisited.remove(next_city)
        path.append(next_city)
        current_city = next_city

    path.append(0)  # Quay lại điểm xuất phát

    # Cải thiện bằng thuật toán 2-opt
    def two_opt(route):
        best = route
        improved = True
        while improved:
            improved = False
            for i in range(1, len(route) - 2):
                for j in range(i + 1, len(route)):
                    if j - i == 1: continue
                    new_route = route[:i] + route[i:j][::-1] + route[j:]
                    if total_distance(new_route, distance_matrix) < total_distance(best, distance_matrix):
                        best = new_route
                        improved = True
            route = best
        return best

    optimized_path = two_opt(path)
    return optimized_path, total_distance(optimized_path, distance_matrix)

# Danh sách các thành phố (tọa độ x, y)
cities = [
    (0, 0), (1, 3), (4, 3), (6, 1),
    (3, 0), (5, 2), (7, 3), (2, 4)
]

# Giải bài toán TSP
path, dist = tsp_nearest_neighbor(cities)
print("Đường đi tối ưu:", path)
print("Tổng khoảng cách:", dist)
