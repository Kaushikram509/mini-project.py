class calculator:
    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y
    def add(self):
        c = self.x+self.y
        return f"Sum of {self.x} and {self.y} is: {c}"
    def sub(self):
        a = self.x-self.y
        return f"sub of {self.x} and {self.y} is: {a}"
    def div(self):
        if self.y == 0:
            return "Division by zero is not allowed"
        b = self.x / self.y
        return f"Div of {self.x} and {self.y} is: {b}"

    def mul(self):
        d = self.x*self.y
        return f"mul if {self.x} and {self.y} is: {d}"
c1 = calculator(10,0)
c2 = calculator(2,3)
print(c1.add())
print(c2.add())
print(c1.sub())
print(c1.div())
print(c1.mul())
