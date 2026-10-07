veggies = ["Poato", "BRinjal","Flower","Cucumber"]
#syntax:- for variable in rage
for val in veggies :
    print(val)

#

tup = (1,2,3,4,5)

for num in tup:
    print(num)

#
# str = "Yoooo its Rahul" #Prints each letter 1 by 1(as its String)

# for char in str:
#     print(char)


#
str = "The Warriors "
for char in str:
    print(char)
    if(char == 'a'): #cheacks if the next letter is a or no
        print("found a ") #When it reaches a it says found a
        break


print("End")

#Question
#1

nums = [1,4,9,16,25,49,64,81,100]
x  = 49

idx=0
for i in nums:
    if(i == x):
        print("Number found at idx ", idx)
    idx +=1


#Questions
#1
for z in range(101):
    print(z)
    