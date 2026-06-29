# WAP to reverse the string
text = "Python"
# print(text[::-1])

reverse = ""

for char in text:
    reverse = char + reverse

print("Reversed string:", reverse)