class NUV:
    def __init__(self,name):
        self.name=name
    def intro(self):
        print("Hi,I am student of " + self.name)
class SET(NUV):
    pass
class CSE(SET):
    pass
X=NUV("Navrachna University")
Y=SET("School of Engineering & Technolodgy")
Z=CSE("Computer Science & Engineering")

X.intro()
Y.intro()
Z.intro()
