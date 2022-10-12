# list_data = [1, 2, 3, 4, 5]
# for number in list_data:
#     if number == 3:
#         print("found 3")
#     elif number > 3:
#         print("you have passed 3")
#     else:
#         print("too soon ")


# print(list_data)
# print(list_data[0])
# print(list_data[1])
# print(list_data[2])
# print(list_data[3])
# print(list_data[4])

#create a dictionary student_data
# iterate through the dict
# using control flow- if elif - else and for lopp print all the keys
# print all the values
# print key with matching value

student_1 = {
    "key": "values",
    "name": "Zakariya",
    "stream": "DevOps"


}
for key in student_1:
    print(key)
values = student_1.values()
print(values)
for key in student_1:
    if key in student_1:
        print(key, student_1[key])

