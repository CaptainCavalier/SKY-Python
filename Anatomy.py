#Example script

import sys
argc = len(sys.argv)

if argc > 1:
    print("Too many Args")
    print("How did that Happen?!")
else:
    print("Hello World")

print("goodbye from", sys.argv[0])


