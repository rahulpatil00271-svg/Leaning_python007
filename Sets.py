# #Sets
# #Set does'nt print duplicate Values

# Num = {14,12,13,13,16,17,18}#set is keyword Set is not a keyword
# print(Num)

# #__________________________________________________________________________________________________________
# #Empty Set
# # collection = set()
# # print(type(collection))
# # #To add value to empty set
# # collection.add(23)
# # print(collection)

# #__________________________________________________________________________________________________________
# #Empty Dictionary
# # collec = {}
# # print(type(collec))

# #__________________________________________________________________________________________________________

# #note- In sets only immutable values can be added 
# #Ex. Lists can,t be added to Sets 

# #__________________________________________________________________________________________________________
# #Pop-Gives Random Value from set

# Collection_pop = {"Helllo", "Hi", "Heyyyyyy Budyyyyy"}

# print(Collection_pop.pop())

# #__________________________________________________________________________________________________________
# #set.union(set2) Combines Both set values n Returns new

# set_1 = {1,2,3,5,7}
# set_2 = {1,3,6,8,9}
# print(set_1.union(set_2))
# #output : {1,2,3,5,6,7,8,9}#no repeted values
# print(set_1.intersection(set_2))#prints common values
# #__________________________________________________________________________________________________________

# #Questions!!!!!!
# #1
# dictionary_1 = {
#     "cat" : "a small Animal",
#     "Table" : {
#         "a piece of furniture"," Facts of Figure"
#     }

# }
# print(dictionary_1)

# #2
# #set of Subjets each set for each Classroom, find no. of classrooms required

# Sub = {
#     "Python", "Java","C","C++","Javascript","Java","Python","Java","C++","C"
# }
# print(len(Sub))

# #3
# #To Enter Marks of 3 Subjects

# Marks = {}

# x = int(input("Enter phy  : "))

# Marks.update({"phy ": x})

# x = int(input("Enter Maths : "))
# Marks.update({"Maths ": x})

# x = int(input("Enter Chem  : "))
# Marks.update({"Chem ": x})

# print(Marks)


#print 9 and 9.0
#case 1
values = {
    9, 9.0}
print(values)
#Output = 9

#case 2
Values = { 9, "9.0"}
print(Values)
#Output-9,9.0 #here 9.0 is String 

# Case 3
Value = { ("float", 9.0),
         ("int", 9)
}
print(Value)
#Output_ 'float',9.0 'int', 9
