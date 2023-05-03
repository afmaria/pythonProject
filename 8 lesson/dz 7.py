class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f'{self.a} + {self.b}i'

    def __add__(self, other):
        return f'{self.a + other.a} + {self.b}i'

    def __mul__(self, other):
        return f'{self.a * other.a - self.b * other.b} + {self.b * other.a + self.a * other.b}i'

number_1 = Complex(6, 4)
number_2 = Complex (4, 8)
print(number_1)
print(number_2)
print(number_2 * number_1)
print(number_2 + number_1)

