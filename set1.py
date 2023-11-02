# my_dict={}

# student={
#     "name":"alice",
#     "age":25,
#     "grade":"a"
#  }
# print(student)
# print(student.get("name"))


# name=student["name"]
# age=student["age"]

# student["age"]=23
# student["city"]="nyop"


# for key,  value in student.items():
#     print(f"{key}: {value}")

# if "age" in student:
#     print("age exist in dictionary")

# squares = {num:num**2 for num in range(1,5)}
# cubes = {num:num**3 for num in range(1,5)}
# print(squares)    
# print(cubes)    



# dict{
#     0:10,
#     1:20,
#     }
# print(dict)


# dic1={1:10 , 2:20}
# dic2={3:30 , 3:40}
# dic3={5:50 , 6:60}
# dic1.update(dic2)
# dic1.update(dic3)
# print(dic1)


# d={
#     "x":10,
#     "y":20,
#     "z":30
# }
# for dict_key, dict_value in d.items():
#     print(dict_key'->')




# color_dict={

# }
#key=color_dict.keys():
# print(sorted(keys))




#square question
# squares = {num:num**2 for num in range(1,16)}
# print(squares)

# mydict={
#     "data1":100,
#     "data2":-54,
#     "data3":247,


# }



d={
    1: 10,
    2: 20,
    3: 30,
    4: 40,
    5: 50,
    6: 60,
}
n=int(input("enter your no. to check:"))
if n in d.keys():
    print("exist")
else:
    print("not exist")