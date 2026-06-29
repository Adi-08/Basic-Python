# Check whether a person is eligible to vote.
# Conditions:
# Age ≥ 18
# Must be an Indian citizen

age = int(input("Enter the age: "))
citizen = input("Are you an Indian Citizen (yes/no):  ")

if age >= 18 and citizen.lower() == "yes":
    print("You are eligible to vote!!")
else:
    print("You are not eligible to vote")


# Check whether a number lies between 10 and 50.
a = int(input("Enter the number: "))
if a >= 10 and a<= 50:
    print("Number lies between 10 and 50")
else:
    print("Number does not lies between 10 and 50")