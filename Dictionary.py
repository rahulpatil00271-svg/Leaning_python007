#Dictionary
#_________________________________________________________________________________-
#In dictionary u can Enter Tuples and even Sets
#info is a variable to store dictionary
info = {
    "Subjects" : ["Python","C","C++","Java"],
    "Topics" : ("dict","tuple"),
    "Key" : "Value",
    "Name" : "Rahul",
     "Age" : 18,
     "Person" : True,
     122 : 92.3
}
#key can be a int or even a float
#int does'nt require ""

print(info)
print(info["Topics"])#you can also print it topicvise
print(info["Key"])

info["Name"] = "Raj" #u can change values
print(info["Name"])#sqr[] are must to write a Key


#_____________________________________________________________________________________-

#Nested Dictionary


#one list can have Multiple lists
Student = {
    "name " : "Rahul Patil",
    "subjects" : {
        "phy" : 89,
        "chem" : 98,
        "Maths " : 97
    }
}
print(Student)
# print(Student["subjects"]["chem"]) #To print specific key

print(Student.keys())#mentions outer Keys not Nested
print(len(Student))#len of only outer

#To store Dictionary in form of List
print(list(Student))

#key.get()
#print(Student["name2"]) #error _ After code doesnt Run
print(Student.get("name2")) #no error --> None _ after code Runs

#To update a new value

Student.update({"city" : "Pune"})
print(Student)
#Student.update({"name" : "RAM"}) To change the existing one








