nameList = []
while True:
    names = str(input("Enter your name: "))
    if names in nameList:
        print ("The name is already in the list")
        continue
    else:
        nameList.append(names)
        print (nameList)
