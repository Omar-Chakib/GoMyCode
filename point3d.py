class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def Area(self):
        return self.length * self.width

    def Perimeter(self):
        return 2 * (self.length + self.width)

class Circle:
    def __init__(self, center_x, center_y, radius):
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius

    def Area(self):
        return 3.14159 * self.radius ** 2

    def Perimeter(self):
        return 2 * 3.14159 * self.radius

    def is_inside(self, x, y):
        distance = ((x - self.center_x) ** 2 + (y - self.center_y) ** 2) ** 0.5
        return distance <= self.radius

class Bank:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return self.balance
        else:
            return "Insufficient funds"


my_point = Point3D(1, 2, 3)
print("Point3D:", my_point)


my_rectangle = Rectangle(4, 3)
print("the area of the rectangle:", my_rectangle.area())
print("the perimeter of the rectangle:", my_rectangle.perimeter())


my_circle = Circle(0, 0, 5)
print("the area of the cirlce:", my_circle.area())
print("the perimeter of the circle:", my_circle.perimeter())
print(" Inside Circle:", my_circle.is_inside(3, 4))


my_account = Bank(1000)
print("Balance after you deposit:", my_account.deposit(500))
print("Balance after you withdrawal:", my_account.withdraw(300))
