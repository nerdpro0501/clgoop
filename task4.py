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