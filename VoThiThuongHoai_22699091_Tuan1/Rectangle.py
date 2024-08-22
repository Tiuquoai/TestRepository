class Rectangle: 
 
    def __init__(self,width,length): 
        self.width = width 
        self.length = length 
 
    def area(self): 
        result = self.width * self.length 
        return result 
    def perimeter(self): 
        result = 2*(self.width + self.length) 
        return result 
    def display(self): 
        print(f'rong: {self.width}, dai: {self.length}, chu vi: {self.perimeter():.2f}, dien tich: {self.area():.2f}\n')