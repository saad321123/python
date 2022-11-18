# creating an empty set
a=set()
print(type(a))

#adding value in set
a.add (3)
a.add(4)
a.add(6)
a.add(6) #Adding a value repeatedly does not change a set
a.add((5,7,8))

#a.add({4:5}) #cannot add list and dictoinary in set

print(a)
print(len(a)) #prints the length of the set

a.remove(3)  #Remove 3 from the set
print(a)


