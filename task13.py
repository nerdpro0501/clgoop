class Task:
    def __init__(self, indate = 0):
        self.indate = indate
   
    def inputdate(self):
        self.indate = int(input("Enter the number of days :"))
       
    def printmessage(self):
        if self.indate == 30:
            print("The months having",self.indate,"days are April, June, September, November")
        elif self.indate == 31:
            print("The months having",self.indate,"days are January, March, May, July, August, October, December")
        elif self.indate == 28:
            print("The month having",self.indate," days is February")
        elif self.indate == 29:
            print("The year is a leap year and the month is February")
        else:
            print("Invalid input")
           
x1 = Task()
x1.inputdate()
x1.printmessage()