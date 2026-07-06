num = int(input("Enter the number: "))
original = num
reverse = 0

while num>0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10
print(reverse)

if reverse == original:
    print("Palindrome")
else:
    print("Not Palindrome")

