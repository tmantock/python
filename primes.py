import math

def primelist(limit):
    primes = []

    for x in range(limit):
        prime = True

        if(x < 2):
            continue
        #An integer is prime if it is not divisible by any prime less than or equal to its square root
        sqrt = math.floor(math.sqrt(x))

        for i in range(2, sqrt + 1):
            if(x % i == 0):
                prime = False

        if(prime == True):
            primes.append(x)

    return primes


def isPrime(num):
    if(num < 2):
        return False
    
    sqrt = math.floor(math.sqrt(num))

    for i in range(2, sqrt + 1):
        if(num % i == 0):
            return False
        
    return True


print(primelist(100))
print(isPrime(22))
