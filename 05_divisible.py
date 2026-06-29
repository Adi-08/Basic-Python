# Program: Check Divisibility by 2 or 7

num = int(input("Enter a number: "))

if num % 2 == 0 and num % 7 == 0:
    print("The number is divisible by both 2 and 7.")
elif num % 2 == 0:
    print("The number is divisible by 2.")
elif num % 7 == 0:
    print("The number is divisible by 7.")
else:
    print("The number is not divisible by 2 or 7.")