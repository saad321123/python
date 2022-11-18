# write a program to create a dictionary of hindi words with values as there English traslation. Provide user with an option to look it up

mydict={
    "Pankha" : "Fan" ,
    "Dabba" : "Box" ,
    "Vastu" : "Element"
}
print("option are",mydict.keys())
a=input("enter the hindi word\n")
# print("The meaning of word is:",mydict[a])

# Below line will not throw an error
print("The meaning of word is:",mydict.get(a))

