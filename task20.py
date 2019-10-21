class animal:
    def speak(self):
        print("Animal is speaking")
class Dog(animal):
    def bark(self):
        print("Dog is barking")
class Eat(Dog):
    def eating(self):
        print("Dog is eating")
d=Eat()
d.bark()
d.speak()
d.eating()
