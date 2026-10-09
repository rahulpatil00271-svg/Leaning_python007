#Functions.........................
def calc_sum(a,b): #To define function def is used
    sum = a+b                                   
    print(sum)
    return(sum)  #It hands u the value of sum to use to again somewhere else
calc_sum(3,4)
calc_sum(4,9)
#Here calc_sum is used multiple Times


#Average of 3 Numbers

def calc_avg(a, b, c):
    sum = a+b+c 
    avg  = sum/3
    print(avg)
    return avg
calc_avg(2,5,3) #can be printed whenever called
#####################Types of Functions####################
#1 Built in function

#ex. print function
#sep = after a , it keeps a space
#end = new print starts on next line 

#2 User Defined function

##############Default Parametersssssss##########
#If no values passed it gives erro

# def cal_(x,y):
#     print(x+y)
#     return(x+y)
# cal_()

#No error

def cal_(x=1,y=4):#Even at the end value is not defined it returns default values
    print(x+y)
    return(x+y)
cal_()

############Questions>>>>>>>>>>>>>########
#using F print length of list
heros = [" Superman","Shaktiman","Ironman","Flash"]#list is formed
games = ["FF","BGMI","FF max"]
def print_len(list):#Defined so any length of  list can be Printed when its called
    print(len(list))

print_len(heros)# Prints len of heros as its called
print_len(games)# Prints len of games as its called

#without F
cities =["Delhi","gurgoan","Pune", "Mumbai"]

print(len(cities))

#________________________________________________________________________________________________________________________________________________---

#Without using F print !(Factorial)

# n = int(input("Enter No. : "))
# fact = 1 #counter from 1 
# for i in range(1,n+1):#when multiplied or added stores value in i to use it again
#     fact *= i #shorter way of fact = fact*i #Multiplies till last value of i
# print(fact)

#__________________________________________________________________________-

#Using Function print !(Factorial)

def cal_fact(n):
    fact = 1 #counter from 1 
    for i in range(1,n+1):#when multiplied or added stores value in i to use it again
        fact *= i #shorter way of fact = fact*i #Multiplies till last value of i
    print(fact) #End value will be stored in fact

cal_fact(7)
cal_fact(9)
cal_fact(3)


#________________________________________________________________________________________________-
# Using Function convert USD to INR
def converter(x):
    rup = x*83
    print(rup," INR = ",x," USD ")
    return(rup)
converter(3)
converter(6)

#____________________________________________________________________________________________________

#Whether Even or Odd Using Functions
def eve_odd(o):
    if o%2==0:
        print("Even")
    else:
        print("odd ")

eve_odd(33)
eve_odd(198)


    