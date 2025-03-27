from utils.dict_functions import dict_persons
from utils.list_functions import cleanup, containsDuplicate, delete_all, destroy_elements, length_counts, majority, nested_sum, sort_person_list_by_age
from utils.int_functions import factors, sum_square_up
from utils.str_functions import encoded_text, isomorphic_string, strongest_password_verify, words_lengths, words_list_with_min_len
from utils.tuple_functions import sum_of_even_and_odds


elt1,elt2,nums = [1,2,3,5],[1,2],[2,2,1,5,1,1,2,5,5,2,1,1,5,5,5,5,5,5]

# Exercise 1

print(f"Destroy element form {elt2} in {elt1}:")
l = destroy_elements(elt1,elt2)
print(f"Destroy elements of {elt1} and {elt2} will be: {l} \n\n")

# Exercise 2

print("Majority of List numbers")
x = majority(nums)
print(f"Majority element of list {nums} is equal to: {x}\n\n")

# Exercise 3

print(f"Check if list {elt1} contains duplicate value")

    # result = containsDuplicate(nums)
result = containsDuplicate(elt1)
print(result,"\n\n")

x,y = 4,64

# Exercise 4

fact = factors(y)
print(f"factor of {y} will give {fact}\n\n")

# Exercise 5

print(f"Sum of the squares of positive value up to {x}: {sum_square_up(x)} \n\n")

issa,abdou,laity = ("Issa",22),("Abdou",17),("Pappa",35)
persons = [issa,abdou,laity]

# Exercise 6

print(f"Persons List: {persons} \n")
sort_person_list_by_age(persons)
print(f"Sorted list by age give: {persons}\n\n")

text = "Write a function that takes a list of words and a minimum length, and returns a new list containing only words that are longer than the specified length."
words = text.split()

# Exercise 7

k = 5
print(text)
print(f"list of words which the len > {k}:")
words_new_list = words_list_with_min_len(words,k)
print(words_new_list)

# Exercise 8

lnums = [1,3,5,2,1]
print(lnums)
print("Delete all occurences functions for 1")
num_list = delete_all(lnums,1)
print(num_list)

# Exercise 9
textcode = "afghjrwgh"

print(textcode)
encode_result = encoded_text(textcode)
print(f"Encoding of text <{textcode}> give <{encode_result}>")

# Exercise 10

textstr = "Sorted list by age give"
print(f"words length of <{textstr}> will give: {words_lengths(textstr)}")

# Exercise 11
    
    # list_to_clean = ["cat", "er", "pillar"]
list_to_clean = ["cat", " ", "er", "", "pillar"]
print(f"function clean list of {list_to_clean} give: {cleanup(list_to_clean)}") 

# Exercise 12

    # nested_list =[[1, 2, 3], [4, 5]]
nested_list =[[1, 2, 3], [], [], [4], [5]]
sum = nested_sum(nested_list)
print(f"Sum of the list {nested_list} give: {sum}")

# Exercise 13
# Uncomment the code below to execute the function
# dict_persons()

# Exercise 14

# Exercise 15

# password = "AMMIPython@2025"
password = "AMMIPython2025"
strength_password = strongest_password_verify(password)
# print(strength_password)
if(strength_password):
    print(f"password {password} is strong")
else:
    print(f"password {password} is not strong")

# Exercise 16

# tuple_list = (1,2,3,4)
tuple_list = (1,3,5)
print(f"Sum of even and odd numbers of tuple {tuple_list} give: {sum_of_even_and_odds(tuple_list)}\n")


# Exercise 17
sa_countries = ["Brazil", "Venezuela", "Argentina", "Ecuador", "Bolivia", "Peru"]
sa_countries_result = length_counts(sa_countries)
print(sa_countries_result)
# Exercise 18
s = "eggg"
t = "addd"
# s = "foo"
# t = "bar"
print(isomorphic_string(s,t))
# Exercise 19
# Exercise 20
# Exercise 21
# Exercise 22
# Exercise 23
# Exercise 24
# Exercise 25
# Exercise 26