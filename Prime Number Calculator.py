from math import sqrt
def Primemısöyle(number):
    if number == 2: # 2 is the only even prime number
        return True
    elif number < 2 or number % 2 == 0: # 1 is not a prime number
        return False
    else:
        i = 3
        while i <= sqrt(number):
            if number % i == 0:
                return False
            i += 2
            
        return True
number = int(input("Enter a number: "))
if Primemısöyle(number):
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")
