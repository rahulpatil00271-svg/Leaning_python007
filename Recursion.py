###########Recursionnnnnnnnnnnn#############

#loops and recursion are similar

#But a recursion calls itself repeatedly

#Ex. 
# def show(n):
#     print(n)
# show(5) #Just prints 5 when called

#U can use recursion instead of loop

def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)
    print("End ")
show(5)


#_____________________________________________________________________________________

#Recursion in Factorial Functionttt
def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)#Here factorial for n! is (n-1)*n Factorial

print(factorial(5))
print(factorial(4))
print(factorial(6))

####################Questions!!!!!!!!!!!!!!!!!!################

#To calculate sum of n values
def cal_sum(x):
    if(x==0):
        return 0
   
    return cal_sum(x-1) + x

print(cal_sum(9))


#Recursion in List
def print_list(list, idx =0):
    if idx == len(list): #if index value = len (i.e last value) it's 
        return #returns <stops> 
    print(list[idx]) #print value at idx 0 (As idx != len)
    print_list(list,idx+1) #goes to Next index value

fruits = ["Mango", "Apple", "Chikoooo","carrot"]
print_list(fruits)#goes to def
