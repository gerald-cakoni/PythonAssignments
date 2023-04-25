class Pet:
    def __init__(self, name, type, trics, noise):
        self.name = name
        self.type = type
        self.trics = trics
        self.noise = noise
        self.health = 0
        self.energy = 0

    def sleep(self):
        self.energy += 25
    def eat(self):
        self.energy += 5
        self.health += 10
    def play(self):
        self.health += 5
    def noise1(self):
        print(f"The sound of: {self.name} is {self.noise}") 

class Ninja:
    def __init__(self, firstName, lastName, trats, petFood, pet):
        self.firstName = firstName
        self.lastName = lastName
        self.trats = trats
        self.petFood = petFood
        self.pet = pet

    def walk(self):
        self.pet.play()
        return self
    
    def feed(self):
        self.pet.eat()
        print(f"I just feed {self.pet.name}!")
        return self
    
    def bathe(self):
        self.pet.noise1()
        return self

#catName=input("Can you give your pet name please: ")

meri = Pet("Meri", "Cat", "Shake Hands", "Mjau Mjau")
bobi = Pet("Bobi", "Dog", "Shake Hands", "Ham Ham")
catName=input("Can you give your pet name please: ")

print(catName.name)
# guido = Ninja("Guido", "Smith", "trats", "food", catName)


#guido.feed();

