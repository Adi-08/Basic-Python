text = "programming"
count = 0
vowels = "aeiou"

for i in text:
    if i in vowels:
        count += 1

print("Number of vowels:", count)