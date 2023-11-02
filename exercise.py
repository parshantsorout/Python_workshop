# while True :
#     password = input("Enter your password : ")

#     if len(password) < 12 :
#         print("Password should be at least 12 characters long.")
#         continue
#     else:
#         has_uppercase = False
#         has_lowercase = False
#         has_special = False
#         has_digit = False

#         for char in password:
#             if ('a' <= char <= 'z') or ('A' <= char <= 'Z'):
#                 if char.isupper():
#                     has_uppercase = True
#                 elif char.islower():
#                     has_lowercase = True

#             elif '0' <= char <= '9':
#                 has_digit = True
#             elif char in "!@#$%^&*()+_;[]{}|,.<>?'/" :
#                 has_special = True

#         if has_uppercase and has_lowercase and has_digit and has_special:
#             print("This is a strong password")
#             break
#         else:
#             print("This is not a strong password . Please try again.")


# words =['Hello','Prashant']
# joined_text=','.join(words)
# print(joined_text)


# text="hello prashant,hello prashant how are you?"
# count=text.count("a")
# print(count)


# name="prashant"
# age=18
# message="my name is {} i am {} year old.".format(name,age)
# print(message)

# text="prashant is a student of btech honors"
# result=text[1::2]
# print(result)


# text="prashant is a student of btech honors"
# result=text[::4]
# print(result)



# txt="gla2023"
# print(txt.isalnum())

# txt1 ="12345678"
# print(txt1.isnumeric)




# txt2="prashant sorout"
# print(txt2.istitle())

# txt3="prashant you get some points of gertians"
# print(txt3.title())


# myData=["prashant","sorout","ramkhet"]
# print(myData)

# print(len(myData))

# print(type(myData))

# thislist=list(("abc","xyz","mno"))
# print(thislist)


# myList = ["GLA", "Sharda", "LPU", "Amity", "Delhi University", "Galgotias", "CU"]
# print (myList[1]) #The first item has index 0.

# print(myList[-1]) #-1 refers to the last item, -2 refers to the second last item etc.

# print(myList[2:5])

# print (myList[:4])

# print(myList[2:])

# print(myList[-4:-1])

# if "GLA" in myList:
#     print("Yes!")





# mydata=["cold milk","cold coffee","hot chai","ver hot coffee"]
# print(mydata)

# mydata[1]="black milk"
# print(mydata)

# mydata[1:3] =["black chai","hot coffee"]
# print(mydata)

# myList=[9,10,11]
# myList.append(12)
# print(myList)

# list1=["a","b","c"]
# list2=["m","n","o"]
# list1.extend(list2)
# print(list1)


# newlist=["kiwi","banana","apple"]
# finalist=newlist.copy()
# print(finalist)


# newlist=["kiwi","banana","apple"]
# newlist.extend(newlist)
# print(newlist)



# list3=list1+list2

# list1=["a","b","c"]
# list2=[4,5,6]

# for x in list2:
#     list1.append(x)

#     print(list1)
# list1=["a","b","c"]
# list2=[4,5,6]

# list1.extent(list2)
# print(list1)





# my_list = [1, 2, 3, 4, 5]
# print(my_list[3])  

# print(my_list[-1])

# sublist = my_list[1:5]
# print(sublist)

# my_list[2] = 10

# my_list.append(20)


# del my_list[0]

# my_list.insert(1, 5)

# print(my_list)

# Initialize an empty list
# my_list = []

# while True:
#     user_input = input("Enter user  to add(or 'complete' to finish): ")
    
#     if user_input.lower() == 'complete':
#         break
    
#     my_list.append(user_input)


# print("Final List:", my_list)



# input_word="hello"
# char_count={}
# for char in input_word:
#  if char in char_count:
#   char_count[char]+=1
#  else:
#   char_count[char]=1

#   for char,count in char_count.items():
#    print(f"{char}-{count}")




#    word="prashant"
#    char="a"
#    count=word.count(char)
#    print(count)

#    word="hello"
#    unique_char=[]

#    for char in word:
#     if char not in unique_char:
#      unique_char.append(char)

#      print(unique_char)
     


# squares= [x ** 2 for x in range(5)]
# print(squares)

# even_numbers=[x for x in range(10) if x% 2==0]
# print(even_numbers)

# results=['pass' if score >= 60 else 'fail' for score in [75,30,85,55]]
# print(results)

# names=['ramsingh','soorav','karan ahuja']
# name_length=[len(name) for name in names]
# print(names)


# num_elements=int(input("enter the no of elements"))
# original_list=[0]*num_elements
# print("original list:",original_list)

# for i in range(num_elements)


my_list=[]

no_of_items=int(input("enter the no of things you want to add"))
for i in range(no_of_items):
    item=input(f"no_of_items {i+1}:")
    my_list.append(item)

    print("final list:",my_list)


