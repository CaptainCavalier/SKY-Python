grade = int(input("Put your score here"))
if grade > 100 or grade < 0:
    print("Invalid Number")
else:
    if grade > 90:
        print("A*")
    elif grade > 80:
        print("A")
    elif grade > 70:
        print("B")
    elif grade > 60:
        print("C")
    elif grade > 50:
        print("D")
    elif grade > 40:
        print("E")
    else:
        print("You Have Failed")
        print("UNLUCKY")



