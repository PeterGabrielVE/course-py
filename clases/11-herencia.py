class Addition:
    a = 10
    b = 20
    def add(self):
        sum = self.a + self.b
        print("Sum of a and b is:",sum)

class Subtraction(Addition):
    def sub(self):
        sub = self.b - self.a
        print("Subtraction of a and b is:",sub)

class Multiplication(Subtraction):
    def multi(self):
        multi = self.a * self.b
        print("Multiplication of a and b is:",multi)

ob = Multiplication()
ob.add()
ob.sub()
ob.multi()