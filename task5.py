class task5:
    def __init__(self, x=0, y=0, prod=0):
        self.x = x
        self.y = y
        self.prod = prod

    def input(self):
        x = int(input("Enter the value of x"))
        print(x)
        y = int(input("Enter the value of y"))
        print(y)
        prod = x*y
        print("The product is")
        print(prod)

x1 = task2()
x1.input()