bignum = 0
while bignum <= 10:
    userin = input("Please enter a number greater than 10:  ")
    if userin.isnumeric():
        bignum = int(userin)
        if bignum < 10:
            print("Thats not higher then 10 idiot")
        else:
            print("Thanks for playing")
    else:
        print("Not a valid input FOOL!")


