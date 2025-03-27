def factors(number:int)->list:
    result = []
    for i in range(number):
        if(number%(i+1)==0):
            result.append(i+1)

    return result

def sum_square_up(number:int)->int:
    if(number <= 0 ):
        return "The input number should be positive"
    square_sum = 0
    for i in range(number):
        square_sum += (i+1)**2
    return square_sum

def factoriel(n:int)->int:
    fact = 1
    for i in range(1,n+1):
        fact*=i
    return fact

def fibonacci(n:int)->int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    return n + fibonacci(n-1)

def prime_number(start:int,stop:int)->list:
    prime_list = []
    for i in range(start,stop+1):
        prime_test = 1
        for j in range(2,i):
            if i%j==0:
                prime_test = 0
        if prime_test == 1:
            prime_list.append(i)
    return prime_list


