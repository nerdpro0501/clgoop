class task1:
    def __init__(self, a=0):
        self.a = a

    def input(self):
        a = int(input("Enter the value of a"))
        print(a)

x = task1()
x.input()

class task4:
    def __init__(self, x=0, y=0, dif=0):
        self.x = x
        self.y = y
        self.dif = dif

    def input(self):
        x = int(input("Enter the value of x"))
        print(x)
        y = int(input("Enter the value of y"))
        print(y)
        dif = x - y
        print("The difference is")
        print(dif)

x1 = task2()
x1.input()


class task8:
    def __init__(self, a=0, b=0, c=0, d=0, exp=0):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.exp = exp

    def expression(self):
        a = int(input("Enter the value of a"))
        b = int(input("Enter the value of b"))
        c = int(input("Enter the value of c"))
        d = int(input("Enter the value of d"))
        exp = (a/b) + (c/d)
        print("The answer is:")
        print(exp)


x1 = task8()
x1.expression() 