#parrent class
class Animal:
    def speak(self):
        print("Animal is making a sound")

#chil class
class Dog(Animal):
    def speak(self):
        print("Dog is barking")

#Creating an Object of the child class
my_dog = Dog()
my_dog.speak()
