#password checker using regEx to search each character in string
import re


pw = input("Please Enter a Password: ")
x = True
while x:
    if not re.search("[a-z]", pw):
        print("Password must contain a lowercase character")
        break
    elif not re.search("[A-Z]", pw):
        print("Password must contain an uppercase character")
        break
    elif not re.search("[0-9]", pw):
        print("Password must contain a number")
        break
    elif not re.search("[$#@]", pw):
        print("Password must contain a special character")
        break
    else:
        print("Valid Password Entered")
        x = False
        break

if x:
    print("Not a Valid Password")




