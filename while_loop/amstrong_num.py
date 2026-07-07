num = 123

original = num
armstrong = 0
while num >0:
    digit = num % 10
    armstrong = armstrong + digit **3  
    num //= 10

if armstrong == original:
    print("This is the armstrong number")
else:
    print("This is not a amstrong number")