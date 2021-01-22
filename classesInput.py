class Classes:
    kind = 'python learner' #kind is universal
    def __init__(self, className, classGrade):
        self.name = className
        self.age = classGrade

while True:
    classCount = int(input(How many classes did you take this semester?: "))
                           
    d = Classes('Alex', 20)
    g = Classes('John', 22)

print (d.name)
print (g.name)
print (d.name+ " is a "+d.kind+" and so is "+g.name+".")

#check dognameinput.py
