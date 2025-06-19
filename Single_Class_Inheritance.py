class Animal:
    def  __init__(self,name):
        self.name = name
        print({self.name},"the name of Animal")

    # Method
    def speak(self):
        print("A Generic sound which an Animal makes")

class Dog(Animal):
    def __init__(self,name, breed, color):
        super().__init__(name)
        self.breed = breed
        self.color = color

    # Behaviours of Dog
    def Make_Sound(self):
        print("Dog Barks!!")

Dog1= Dog("Leo", "Labra", "Baby-Pink")

# Calling/Initiating Method from Parent Class
Dog1.speak()