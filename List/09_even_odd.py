marks = [1,51,77,100,90,7]

even = []
odd = []

for i in marks:
    if i % 2 ==0:
        even.append(i)
    else:
        odd.append(i)

print("Even numbers: ",even)
print("Odd numbers: ",odd)