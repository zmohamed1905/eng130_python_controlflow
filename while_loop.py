

# data = 0
#
# while data < 10:
#     print(f"it's working - >{data}")
#     if data == 5:
#         break # key word - continue also a key word
#     data += 1

def calculate_age():
    user_prompt = True
    age = 0
    while user_prompt:
        age = input("please enter your age")
        if age.isdigit():
            user_prompt = False
        else:
            print("Please enter your age in digits only")
        print(f"your age is {age}")
    # calculate their age- year of birth etc.

    year= 2022 - int(age)

    year= str(year)

    print("and you were born in {}".format(year))

calculate_age()