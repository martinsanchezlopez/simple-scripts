from math import *
import sys


#return a boolean for a given number
def checkPrime(nb):
    nb_root = int(sqrt(nb)) + 1
    for i in range(2, nb_root):
        if (nb%i==0):
            print("\n -divisible by " + str(i))
            return False
        
    return True


def printOutput(b, nb):
    
    #---- are for visibility
    message = "\n -- The number " + str(nb)
    if b:
        message += " is a prime number"
    else:
        message += " is NOT a prime number"
    print(message)

if len(sys.argv) > 1:
    x = int(sys.argv[1])
    printOutput(checkPrime(x), x)


while True:
    nb = int(input("\n Enter a natural number : "))
    printOutput(checkPrime(nb), nb)
