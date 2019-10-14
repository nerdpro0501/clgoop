class task3:
    def __init__(self, x=0, y=0, sum=0):
        self.x = x
        self.y = y
        self.sum = sum

    def input(self):
        x = int(input("Enter the value of x"))
        print(x)
        y = int(input("Enter the value of y"))
        print(y)
        sum = x+ y
        print("The sum is")
        print(sum)

x1 = task2()
x1.input()