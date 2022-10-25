# a = 2
#
# b = 6
#
# print(a ** b) # square
# print(a / b)
# print(a // b) #floor division
# print(a % b) #mod - gives the remainder
#
# #BODMAS or BIDMAS
#
# print(3 + (4 * 3) / 4**6)
#
# mystr = "ant"
# print(hex(id(mystr)))

# myList  =   ["Dave", "Amy", "frank"]
# print(hex(id(myList)))
# myList.append("William")
# print(myList)
# print(hex(id(myList)))



#mynewList = list("bill", "dave")


# mylist = []
#
# print(mylist)
# mylist.append("ant")
# print(mylist)
# mylist.append("6")
# print(mylist)
#
# ant = ["ingegnere", 33, "Metalhead", True]
# print(ant)

# ************LISTS***************


# runners = []
#
# runner = []
# runner.append("bill")
# runner.append(56)
# runner.append(45)
# runner.append(29)
#
# runners.append(runner)
# runner = []
# runner.append("dave")
# runner.append(54)
# runner.append(67)
# runner.append(33)
# runners.append(runner)
#
# for runner in runners:
#     print(f"{runner[0]} lap1: {runner[1]} lap2: {runner[2]}"
#           f" lap3: {runner[3]}")
#
# cheese = ["edam", "brie"]
#
# print(cheese[-1])


# ******* TUPLES *******

# mytuple = ("bill", "dave")
# print(type(mytuple))
# print(mytuple)


# ****** DICTIONARIES *******

# caps = {
#     "england" : "London",
#     'France' : 'Paris',
#
# }
#
# search = input("enter your country").lower()
#
# print(caps[search])
#
# print(caps['France'])
#
# country = "Germany"
# caps[country] = 'Berlin'
# print(caps)

# ********* CONDITIONALS **********

# age = 88
#
# if age > 67:
#     print("Grab your pension")
# else:
#     print("Pay your NI")

# age = 16
#
# if age > 67:
#     print("Grab your pension")
#     print("You have worked long enough")
# elif age < 17:
#     print("You pay no NI")
# else:
#     print("Pay your NI")


#
# print(5 > 4) # TRUE
# print(5 < 4) # FALSE
#
# name = ""
#
# if name:
#     print("You entered date")
# else:
#     print("No Data entered")

# age = 56
# print(age < 4)
#
# name = input("Enter your name")
#
# if name == "bob":
#     print("Welcome Bob")
#     pw = input("Enter Password")
#     if pw == "LetMeIn":
#         print("You have access")
#     else:
#         print("Incorrect Password")
# else:
#     print("Who are you?")

# dist = 54
# cost = 67
#
# if dist < 50 and cost < 80:



#print(5 < 4 and 4 < 6)

list = [0,1,2,3]
#
# if list:
#     print("Data")
# else:
#     print("No Data")



# if all(list):
#     print("All True")
# else:
#     print("Not all true")
#
# if any(list):
#     print("There are some Trues")
#
#
# print(1) #boolean true
# print(0) #boolean false


# ******** CONDITIONAL LOOPS ******

#  *conditional While

# loops = 0
# while loops < 5:
#     print("this is a loop")
#     loops += 1
#
# print("End of Loop")
#
# lives = 3
# while lives > 0:
#     play()
#     if collision:
#         lives -=1
# print("Game Over")


# import random
# score = 0
# lives = 3
# while lives > 0:
#     print(f"you have {lives} lives ")
#     num1 = random.randint(0, 20)
#     num2 = random.randint(0, 20)
#     num3 = num1 + num2
#     print("what is", num1, "+", num2)
#     userans = int(input())
#     if userans == num3:
#         print("correct")
#         score += 1
#     else:
#         print("Incorrect")
#         lives -= 1
# print(f"you scored {score} points ")



# valid = "no"
# while valid == "no":
#     userin = input("Enter a Number")
#     if userin.isnumeric():
#         print("Thank you for a number")
#         valid = "yes"
#     else:
#         print("that was not a number")
#         valid = "no"
#
# print("Carry On")



# loops = 10
# while loops <= 20:
#     print(f"this is loops {loops}")
#     loops += 1


# loops = 1
# num = int(input("Enter a number"))
# while loops <= 12:
#     print(f"{num} * {loops} is {num*loops}")
#     loops += 1



valid = "no"
while valid == "no":
     userin = input("Enter a Number")
     if userin.isnumeric():
         print("Thank you for a number")
         valid = "yes"
     else:
         print("that was not a number")
         valid = "no"

intconv = int(userin)
userchoice = userin * 2
print("Carry On")

#  *unconditional For


