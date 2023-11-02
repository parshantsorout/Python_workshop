# float_num=3.75
# integer_num=15
# string_num="25"
# string_float="7.5"

# convert_int=int(float_num)
# converted_str=str(integer_num)
# converted_str_to_int=int(string_num)
# converted_str_to_float=float(string_float)

# print("converted float to int",convert_int)
# print("converted int to str",converted_str)
# print("converyed str to int",converted_str_to_int)



# score = 65
# if score >= 65:
#     print("65 more")
# elif score >= 80:
#     print()
# else:
#     print()







# Largest of two numbers

# num1=int(input("enter your 1st number\n"))
# num2=int(input("enter your 2nd number\n"))
# if num1<=0 or num2<=0 or num1<=0 and num2<=0:
#    print("these are invalid")

# elif num1==num2:
#    print("both are same")
# elif num1>num2:
#    print(f"{num1} is greater and num2 is {lesser}")  
# elif num2>num1:
#    print(f"{num2} is greater and num1 is {lesser}")


# Fast food menu selection

# foodtype=(input("you are veg or non-veg: "))
# budget=int(input("what is your budget: "))
# time=int(input("enter time: "))
# if foodtype =="veg" and budget=="100"and time==("15"):
#   print("1.Burger ")
#   print("2.Pizza")

 
# elif foodtype=="non-veg" and budget=="100"and time==("15"):
#   print("1. non-veg Burger ")
#   print("2. chicken Pizza")


# Usename and Password Validation




# for num in range(1,11):
#     if num ==11:
#         break
#     print(num)

# input1=input("enter name of your university:- ")
# for x in input1:
#      print(x)


# i=1
# while i<6:
#     i==1
#     if i==3:
#         continue
#     print(i)

   

# start=int(input("enter the start range:"))
# end=int(input("enter the end range:"))
        
# sum_even=0
# sum_odd=0

# for num in range(start,end+1):
#     if num%2==0:
#         sum_even+=num
#     else:
#         sum_odd+=num

# print(f"sum of even numbers between {start} and{end}: {sum_even}")
# print(f"sum of odd numbers between {start} and{end}: {sum_odd}")




#factorial calculator
# n=int(input("enter a number"))
# factorial=1
# for i in range (1,n+1):
#     factorial*=1
#     print(f"the factorial of {n} is: {factorial}")


#fibonacci sequence

# limit=1000
# finonacci_sequence=[0,1]

# while True:
#     next_number=finonacci_sequence[-1]+finonacci_sequence[-2]
#     if next_number>limit:
#         break
#     finonacci_sequence += [next_number]
# print("Finonacci sequence")
# print("finonacci_sequence")






# print("HELLO","WORLD", sep="-")
# print("HELLO - WORLD")


# str="hello"
# str[:2]
# print(str)


# print(2+4.00, 2**4.0)

# name=input("enter your name:")
# print("hello,"+name+"! ")








# k=4
# for k in range(k+1,0,-1):
#     print("*"*k)



#reverse number
# poi=int(input("enter the numbers"))
# reversed_number=0
# while number >0:
#     digit =number


#leap year checker
start_range=int(input("enter the starting range: "))
end_range=int(input("enter the ending range: "))

for i in range(start_range , end_range+1):
    if i %4==0 and(i%100!=0 or i %400==0):
        print("print leap year are this",i)


