var = input("Please enter a value: ")

print(var.upper())
print(len(var))
print(var.isdecimal())

pw = input("Check Password")

for char  in pw:
    if char.islower():
        print("That's a lower case")



