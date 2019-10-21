class task11:
    def __init__(self, r=0, cir=0, ar=0):
        self.r = r
        self.cir = cir
        self.ar = ar

    def area(self):
        r = int(input("Enter the input of r"))
        area = 3.14 * r * r
        print(area)

    def circumference(self):
        r = int(input("Enter the input of r"))
        cir = 2*3.14*r
        print(cir)

x1 = task11()
x1.area()
x1.circumference()