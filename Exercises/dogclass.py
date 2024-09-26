# Creating a dog class
class dog:
# Class attribute species "canis familiaris"
    species = "canis familiaris"
# Each Dog should have a name and age
    def __init__(self, name, age):
        self.name = name
        self.age = age
# Should print nicely
    def __str__(self):
        return f"{self.name} is {self.age} years old"
# Should be able to speak a sound (argument)

    def speak(self, sound):
        return f"{self.name} says {sound}"

ollie = dog("Ollie",900)   
#print(ollie)
print(ollie.speak("Wau"))
