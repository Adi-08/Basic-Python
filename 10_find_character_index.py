
# Program: Find Character Index

txt = "Python"
find = "o"

for i in range(len(txt)):
    if txt[i]== find:
        print(i)


# We can used pre-defined method
target =txt.find("o")
print(target)