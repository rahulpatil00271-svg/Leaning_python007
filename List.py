#List - [Mutable]
#________________________________________________________________________-
# marks = [12,13,15,19]
# marks.append(4) #to add value in last
# marks.sort()#to sort in ascending(also works with strings)
# print(marks)

# marks.reverse()
# print(marks)

# marks.insert(2,3)#inserts value 3 at index 2
# print(marks)
#__________________________________________________________________________-

#To comment Entire Para - ctrl+/
#Question 
#enter 3 movies and store them in a list form
#___________________________________________________________________________
#(M1)
# movies =[]

# mov1 = input("Enter Movie1")
# mov2 = input("Enter Movie2")
# mov3 = input("Enter Movie3")

# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)

# print(movies)


#___________________________________________________________________________

# method 2
# movies =[]

# mov = input("Enter Movie1")
# movies.append(mov)

# mov = input("Enter Movie2")
# movies.append(mov)

# mov = input("Enter Movie3")
# movies.append(mov)

# print(movies)


# ___________________________________________________________________________

# Method3
# movies =[]

# movies.append(input("Enter Movie1"))
# movies.append(input("Enter Movie2"))
# movies.append(input("Enter Movie3"))

# print(movies)


#___________________________________________________________________________
#To check is a list Palindrome or no(hint: Use copy)
#(Same from start n End)
#__________________________________________________________________________

# list1 = [1,2,3,3,2,1]

# copy_list1 = list1.copy()#U have to make a copy before reversing it, As reverse changes og list itself
# copy_list1.reverse()

# if copy_list1 == list1:
#     print("It's a pallindrome ")
# else:
#     print("Not a pallindrome")

#___________________________________________________________________________

# list2 = ["a","b","c"]

# copy_list2 = list2.copy()
# copy_list2.reverse()


# if copy_list2 == list2:
#     print("It's a pallindrome ")
# else:
#     print("Not a pallindrome")

#______________________________________________________________________
#Taking Input
list3 = []
list3.append(input("Enter a char"))
list3.append(input("Enter a char"))
list3.append(input("Enter a char"))


copy_list3 = list3.copy()
copy_list3.reverse()


if copy_list3 == list3:
    print("It's a pallindrome ")
else:
    print("Not a pallindrome")
