# Strings
name = "Pramod"
# Str
print(type(name))
print(name.upper())
print(name.lower())
print(len(name))    #Length starts from 1


a = "90"
age = 90
print(type(a))
print(type(age))


name = "This is a Big Line"
print(type(name))
name = name + str(1)
print(name)

first_name = "Pramod"
last_name = "Dutta"
full_name = first_name + last_name    #CONCAT
print(full_name)

how_many_planes_i_have = None
print(type(how_many_planes_i_have)) #<class 'NoneType'>
# null not present in python

val = 0 # This is int

#id
age = 10
age2 = 10
print(id(age))  #memory location : 1965582215760
print(id(age))  #memory location : 1965582215760