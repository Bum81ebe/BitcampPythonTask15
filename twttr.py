#twitter

text = input("Please input your Text: ")
output = ""
for char in text:
    if char.upper() not in "AEIOU":
        output += char

print(output)