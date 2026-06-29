# Program: Voting Eligibility

age = int(input("Enter your age: "))
citizen = input("Are you an Indian citizen (yes/no): ")

if age >= 18 and citizen.lower() == "yes":
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")


print("-" * 40)

# Program: Check Number Between 10 and 50

num = int(input("Enter a number: "))

if 10 <= num <= 50:
    print("The number lies between 10 and 50.")
else:
    print("The number does not lie between 10 and 50.")