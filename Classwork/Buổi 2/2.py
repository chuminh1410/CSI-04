class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width
    def nhap(self):
        self.height = int(input("Input height: "))
        self.width = int(input("Input width: "))
    def dientich(self):
        return self.height * self.width
    def chuvi(self):
        return (self.height + self.width) * 2

rectangle1 = Rectangle(height=0, width=0)

rectangle1.nhap()

area = rectangle1.dientich()
perimeter = rectangle1.chuvi()

print(f"Diện tích: {area}")
print(f"Chu vi: {perimeter}")
