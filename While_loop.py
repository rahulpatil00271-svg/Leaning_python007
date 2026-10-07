# #Used to Write code once and use it multiple times

# #Infinite Loop

# # while True:
# #     print("Hello")

# #non-Infinite
# #Prints Hello n digits from 1 to 5  
# count = 1 #count is a variable
# while count <= 5 :
#     print("Helllo", count)# To print 
#     count += 1 #increment by 1

# #prints Hello n digits in Reverse order
# Count = 6 
# while Count >= 1 : # From 6 to 1
#     print("Hello", Count)
#     Count -=1 #Decrement by 1

# #Questions
# #1
# # i = 1
# # while i <= 100 :
# #     print("hey", i)
# #     i +=1 

# #2
# a = 100
# while a >= 1 :
#     print("hey", a)
#     a -=1 

# #3
# x = 1
# while x<= 10 :
#     print(x*x)
#     x += 1

# #4- Table
# n = int(input("Enter Variable" )) #Table to print
# t = 1 #counter from 1
# while t <= 10 : # Ends at 10 
#     print(n*t) 
#     t += 1 #increment


#  #5 - List 
# nums = [1,4,9,16,25,36,49,64,81,100]

# l=1
# while 1 <= len(nums):
#     print(nums[l])
#     l+=1

#6 - Tuple Find a value

Num = (1,4,9,16,25,36,49,64,81,100,36)
T = 36

i = 0
while i < len(Num) :
    if Num[i] == T:
        print("Found at idx ", i)
    i += 1


