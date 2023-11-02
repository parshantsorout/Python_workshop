#encapsulation=protect the data (when we can use it)private the data
# class bankaccount:
#     def __init__(self,account_number,balance):
#         self.account_number =account_number
#         self.balance =balance
#     def getbalance(self):
#         return self.balance
        
# account1= bankaccount("1234", "1000")
# print(account1.account_number)
# print(account1.getbalance())

#inheritence
# class animal:
#     def __init__(self,name):
#         self.name=name

#     def speak(self):
#         pass
# class dog(animal):
#     def speak(self):
#         return "woof!"
# class cat(animal):
#     def speak(self):
#         return"meow!"
# dog1=dog("buddy")
# cat1=cat("whiskers")
# print(dog1.name,dog1.speak())
# print(cat1.name,cat1.speak())


# def my_function():
#     x=10
#     print(x)


# def my_function():
#     print(x)

#master is the main branch
#non-local scope  modify a global variable from within a function ,outside the function
x=10
def modify_global():
    global x
    x=20