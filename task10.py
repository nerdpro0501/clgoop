class task10:
    def __init__(self, p=0, r=0, t=0, ci=0):
        self.p = p
        self.rt = rt
        self.t = t
        self.ci = ci

    def compinterest(self):
        p = int(input("Enter the principal amount:"))
        r = int(input("Enter the rate of interest"))
        t = int(input("Enter the number of years"))
        ci = p*(1 + r)**3
        print("The simple interest is")
        print(ci)

x1 = task10()
x1.simpleinterest()