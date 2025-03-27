def sum_of_even_and_odds(input:tuple)->tuple:
    even,odd = 0,0
    for elt in input:
        if (elt%2 == 0): # even number
            even+=elt
        else:
            odd+=elt
    return even,odd