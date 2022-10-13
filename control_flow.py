# pseudo coding


# weather = "time"
#
# # if it's cold:
# if weather == "cold": # True or False
#     print("wear a jacket")
# #     take jacket
# elif weather == "sunny":
#     print("let's go to the beach")
#
# # if its raining:
# else:
#     print("no match better luck next time")
#     rain coat
# if it's sunny: boolean value true- next line if false goes to else or elif
#     let's go to the beach
# else

# age restriction for movie tickets
# create a condition for 18 & above
# 16 & above
# universal
# pg
# 12a
# 15 & above
# if nothing matches inform the user to enter their age again
# user must not be allowed to enter age over 117 years

print("Hello!, Welcome to Sparta Cinema")
age = int(input("Enter your age: "))

# Updated DEF Movie Rating
def movie_rating(age):
    if age > 117:
        print("Your age must be under 117, please try again ")
    elif age >= 18:
        print("Enjoy the  18 plus movie!")
    elif age >= 16:
        print("Enjoy the 16 plus movie!")
    elif age >= 15:
        print("Enjoy the 15 plus movie!")
    elif age >= 12:
        print("Enjoy the 12 plus movie!")
    else:
        print("Error, please try again :( ")

    return f"Your age is {age}"
print(movie_rating(age))