

# data = 0
#
# while data < 10:
#     print(f"it's working - >{data}")
#     if data == 5:
#         break # key word - continue also a key word
#     data += 1

user_prompt = True

while user_prompt:
    age = input("please enter your age")
    if age.isdigit():
        user_prompt = False
    else:
        print("Please enter your age in digits only")
    print(f"your age is {age}")
# calculate their age- year of birth etc.
