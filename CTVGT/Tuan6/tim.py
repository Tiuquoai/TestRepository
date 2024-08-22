import turtle
import random
import math

# Thiết lập màn hình
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("sky blue")

# Tạo đối tượng Turtle cho trái tim
heart = turtle.Turtle()
heart.hideturtle()  # Ẩn Turtle
heart.speed(1)  # Tốc độ nhanh hơn

# Màu sắc
heart_color = "red"
text_color = "white"
bubble_colors = ["cyan", "blue", "purple", "pink", "orange", "yellow"]  # Danh sách màu sắc bong bóng

# Vẽ hình trái tim
def draw_heart():
    heart.penup()
    heart.goto(0, -250)
    heart.pendown()
    heart.begin_fill()
    heart.fillcolor(heart_color)
    heart.left(140)
    heart.forward(224)  # Đoạn này được điều chỉnh
    for _ in range(200):
        heart.right(1)
        heart.forward(2)
    heart.left(120)
    for _ in range(200):
        heart.right(1)
        heart.forward(2)
    heart.forward(224)  # Đoạn này được điều chỉnh
    heart.end_fill()

# Thêm văn bản vào bên trong trái tim
def add_text():
    heart.penup()
    heart.goto(0, -180)
    heart.pendown()
    heart.color(text_color)
    heart.write("Love", align="center", font=("Arial", 20, "bold"))

# Tạo danh sách chứa bong bóng
bubbles = []

# Hàm tạo bong bóng
def create_bubble():
    bubble = turtle.Turtle()
    bubble.hideturtle()  # Ẩn Turtle
    bubble.speed(10)  # Tốc độ nhanh hơn
    bubble.penup()
    x = random.randint(-300, 300)
    y = random.randint(-100, 250)
    color = random.choice(bubble_colors)  # Chọn màu sắc ngẫu nhiên từ danh sách màu sắc
    bubble.color(color)
    bubble.goto(x, y)
    bubble.dot(20)  # Kích thước bong bóng
    bubbles.append((bubble, x, y))

# Tạo số lượng bong bóng
for _ in range(20):
    create_bubble()

# Hàm chuyển động bong bóng
def move_bubbles():
    for bubble_info in bubbles:
        bubble, x, y = bubble_info
        x += math.sin(bubble.heading() * math.pi / 180) * 2
        y += math.cos(bubble.heading() * math.pi / 180) * 2
        if x < -400 or x > 400 or y < -300 or y > 300:
            x = random.randint(-300, 300)
            y = random.randint(-100, 250)
        bubble_info = (bubble, x, y)
        bubble.goto(x, y)

# Vẽ trái tim và bong bóng
draw_heart()
add_text()

# Thực hiện chuyển động và hiển thị
while True:
    move_bubbles()
    screen.update()
