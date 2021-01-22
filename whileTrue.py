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
    d = Dog('Fideo', 10) #name and weight are unique for every dog
    g = Dog('Fifi', 2)

    print (d.name+':', d.bark(3))
    print (g.name+':', g.bark(6))
    print (d.name+ " is a "+d.kind+" and so is "+g.name+".")

Done = input("Are you done?" + '(Yes/No)')
if 'Yes' in QuitAssure:
    exit()
else:
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
    d = Dog('Fideo', 10) #name and weight are unique for every dog
    g = Dog('Fifi', 2)

    print (d.name+':', d.bark(3))
    print (g.name+':', g.bark(6))
    print (d.name+ " is a "+d.kind+" and so is "+g.name+".")
Done = input("Are you done?" + '(Yes/No)')
if 'Yes' in QuitAssure:
    exit()
