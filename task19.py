class task2:
    def __init__(self,n=0,count=1):
        self.number = n
        self.count = count
       
    def inputn(self):
        self.n = int(input("Enter the value of n"))
       
    def printn(self):
        while(self.n>1):
            self.n = self.n - 1
            print("The values are",self.n)
           
x1 = task2()
x1.inputn()
x1.printn()
