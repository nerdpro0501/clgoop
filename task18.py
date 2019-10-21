class task1:
    def __init__(self,n=0,count=1):
        self.number = n
        self.count = count
       
    def inputn(self):
        self.n = int(input("Enter the value of n"))
       
    def printn(self):
        while(self.count<self.n):
            self.count = self.count + 1
            print("The values are",self.count)
           
x1 = task1()
x1.inputn()
x1.printn()