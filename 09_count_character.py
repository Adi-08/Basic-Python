# Program: Count Character Occurrences

text = "pythono"
find = "o"

count = 0

for char in text:
    if char == find:
        count += 1

if count > 0:
    print(f"'{find}' is present {count} time(s).")
else:
    print(f"'{find}' is not present.")