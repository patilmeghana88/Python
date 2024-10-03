class Bird:
    def fly(self):
        print("Bird is flying.")

class Airplane:
    def fly(self):
        print("Airplane is flying.")

#polymorphism in action
def make_it_fly (flying_object):
    flying_object.fly()

#creating objects
sparrow = Bird()
boeing = Airplane()

make_it_fly(sparrow)
make_it_fly(boeing)
