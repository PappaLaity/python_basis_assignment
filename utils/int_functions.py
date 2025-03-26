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
