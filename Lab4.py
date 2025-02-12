import math

def fibonacci(n):
    num1 = 0
    num2 = 1
    total =0
    x=0
    while x<n:
        total = num1 + num2
        num1 = num2
        num2 = total
        x +=1
    return total

def is_prime(num):
    if num <= 1:
        return False
    for x in range(2, int(math.sqrt(num)) + 1):
        if num % x == 0:
            return False
    return True

def print_prime_factors(num):
    if is_prime(num) == True:
        print(f"{num} = {num}")
        return
    original = num
    divisor = 2
    firstfactor = True
    print(f"{original} = ", end = "")
    while num>1:
        if num%divisor ==0 and is_prime(divisor):
            if not firstfactor:
                print(" * ", end = "")
            print(divisor, end = "")
            num /=divisor
            firstfactor = False
        else:
            divisor+=1
    print()

