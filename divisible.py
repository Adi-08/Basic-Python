# Check if a number is divisible by either 2 or 7.

num = int(input("Enter the number: "))

if num % 2 == 0 and num % 7 ==0:
    print("It is divisible by both 2 and 7")
elif num % 2==0:
    print("Number is divisible by 2")
elif num % 7 ==0:
    print("Number is divisible by 7")
else:
    print("Number is not divisible by 2 or 7")