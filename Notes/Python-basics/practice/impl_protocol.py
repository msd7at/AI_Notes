from protocol import Animal
class Dog:
    def speak(self):
        return ("Bhau bhau")
    def eat(self):
        return("Kuch bhi omnivorus")
        # return 

class Cow:
    def speak(self):
        return "jai gow mata"
    def eats(self):
        return "grass"
    

def letsTest(animal : Animal):
    print(animal.speak())
    print(animal.eat())

letsTest(Dog())
letsTest(Cow())