mydict= {
"fast": "in a quick manner",
"saad": "A coder",
"marks":[1,2,5],
"anotherdict":{'saad': 'player'},
  1: 2
}

# dictionary method
print(list(mydict.keys()))  #Prints the keys of dictionary
print(mydict.values())  #Prints the keys of dictionary


print(mydict)
updatedict={
    "Amin Sir": "the Director",
    "Rameez Sir" : "Hardware",
    "Aman sir" : "Hardware",
    "Sai sir" : "Web Developer"
}
mydict.update(updatedict)  #update the dictionary by adding key-value pairs from (updatedict)
print(mydict)  


mydict.get("saad2")  #Return none as saad2 is not present in the dictionary
print(mydict)
print(mydict["saad2"]) #Return eror as saad2 is not present in the dictionary


