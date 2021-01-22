'''
OOP: Object Oriented Programming
Top-down design.
Decompose program in seperate tasks and it must work together.

if "You and your friend fix dinner"
then objects: you, friend, dinner
Add 'you' and 'friend' into [class]
class must have attributes: name, eye color...

Ex. Dog
- Name
- Weight
- Able to bark (method)
method is universal attribute to class
'''

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

d = Dog('Fideo', 10)
g = Dog('Fifi', 2)

print (d.name+':', d.bark(3))
print (g.name+':', g.bark(6))
print (d.name+ " is a "+d.kind+" and so is "+g.name+".")
