while True:
    class Dog:
        kind = 'canine' #kind is universal, all carnivores are universally canine.
        def __init__(self, name, weight):
            self.name = name
            self.weight = weight
        def bark(self,num):
            if (self.weight < 4):
                sound = 'yip ' * num
            else:
                sound = 'ruff ' * num
            return (sound)

dogName = str(input("Enter your dog's name: "))
dogWeight = float(input("Enter your dog's weight: "))
dogName2 = str(input("Enter your second dog's name: "))
dogWeight2 = float(input("Enter your second dog's weight: "))

d = Dog(dogName, dogWeight)
g = Dog(dogName2, dogWeight2)

dogBark = int(input("How many times should " + dogName + " bark: "))
dogBark2 = int(input("How many times should " + dogName2 + " bark: "))

print (d.name+':', d.bark(dogBark))
print (g.name+':', d.bark(dogBark2))
print (d.name+ " is a "+d.kind+" and so is "+g.name+".")

Quit
