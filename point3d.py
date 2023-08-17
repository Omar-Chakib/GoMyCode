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

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

class Circle:
    def __init__(self, center_x, center_y, radius):
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

    def perimeter(self):
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

# Point3D example
my_point = Point3D(1, 2, 3)
print("Point3D:", my_point)

# Rectangle example
my_rectangle = Rectangle(4, 3)
print("Rectangle Area:", my_rectangle.area())
print("Rectangle Perimeter:", my_rectangle.perimeter())

# Circle example
my_circle = Circle(0, 0, 5)
print("Circle Area:", my_circle.area())
print("Circle Perimeter:", my_circle.perimeter())
print("Is Inside Circle:", my_circle.is_inside(3, 4))

# Bank Account example
my_account = Bank(1000)
print("Balance after deposit:", my_account.deposit(500))
print("Balance after withdrawal:", my_account.withdraw(300))
