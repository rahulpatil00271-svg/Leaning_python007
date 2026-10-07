# #Note: Continue basically Skips a no. 
# #Case-1
# i = 0
# while i <= 5: 
#     if(i == 3):#when i = 3, it stops
#         continue
#     print(i) #Executed when i != 3
#     i += 1

#Case-2
a = 0
while a <=5:
    if(a == 3):
        a += 1 #Executed when a = 3
        continue  #Executed when a = 3
    print(a) #when a!=3
    a += 1

#Case 3 To print odd
x = 1
while x <= 10: #step 1 checks less then 10 or not
    if(x%2 == 0): #checks even or no.. if not then print(x) if yes then increatmeant n continue(skip even)
        x += 1
        continue #Skips Even 
    print(x)
    x += 1



    