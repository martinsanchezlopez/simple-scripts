from math import *
import sys



def facto(n):
    x = n
    i=2
    message = ""
    while x > 1:
        if x%i == 0:
            x = x/i
            message += "*" + str(i) #TODO: add power for reccuring multiples
        else:
            i+=1
    print("\n " + str(n) + " = " + message[1:])


if len(sys.argv) > 1:
    x = int(sys.argv[1])
    facto(x)


while True:
    nb = int(input("\n Enter a natural number : "))
    facto(nb)
