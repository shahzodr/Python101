Animal_name = ['dog', 'goat',]
Human_name = ['John', 'David',]

num = min(len(Animal_name), len(Human_name))
result = [None]*(num*2)
result[::2] = Animal_name[:num]
result[1::2] = Human_name[:num]
result.extend(Animal_name[num:])
result.extend(Human_name[num:])
result





'''
mergeList = [mergeList(Animal_name), mergeList(Human_name)]
print mergeList(it.next() for it in itertools.cycle(iters))
'''

'''
mergeList = [None]*(len(Animal_name)+len(Human_name))

print(mergeList)
'''

'''
result[::2] = Animal_name
result[1::2] = Human_name
'''
