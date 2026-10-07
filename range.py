# #Range
# #Note: In range 10 not included
# for i in range(10): #10 is a stoping condition
#     print(i)


# for x in range(1,11):#Range(start,Stop)
#     print(x)


# for a in range(1,21,3):#Range(start,Stop, increment)
#     print(a)


# #Questions
# #1
# for z in range(101):
#     print(z)

# #3 (Reverse)
# for q in range(101,0,-1):
#     print(q)

# #Table

# T= int(input("Enter Num "))#Input value from User

# for n in range(1,11): #from 1 to 10
#     print(T*n)#to print Table of T


# #Sum of  first S natural Nums

# S = 132 #no. of elements

# sum = 0 #Starting value and Sum to store sum of S nums
# for c in range(1,S+1):
#     sum += c
# print(sum)

#Sum of  first w natural Nums Using While Loop

w = 133
add = 0
l = 1
while l <= w:
    add += l
    l += 1

print("Total ", add)


#Factorial ! of N natural nums
N = 5
fact = 1 # alsways 1 not 0
i=1
while i<= N:
    fact *= i
    i += 1
print("Factorial = ", fact)
