from utils.dict_functions import dict_persons
from utils.file_functions import copy_file
from utils.list_functions import cleanup, containsDuplicate, delete_all, destroy_elements, doc_product, four_id_list_generated, length_counts, majority, mat_mul, nested_sum, reverse, sort_person_list_by_age
from utils.int_functions import factoriel, factors, fibonacci, prime_number, sum_square_up
from utils.str_functions import encoded_text, isomorphic_string, palindrom, strongest_password_verify, words_lengths, words_list_with_min_len
from utils.tuple_functions import sum_of_even_and_odds


elt1,elt2,nums = [1,2,3,5],[1,2],[2,2,1,5,1,1,2,5,5,2,1,1,5,5,5,5,5,5]

# Exercise 1

print("\n ********** Exercise 1 ************\n")

print(f"Destroy element form {elt2} in {elt1}:")
l = destroy_elements(elt1,elt2)
print(f"Destroy elements of {elt1} and {elt2} will be: {l} \n\n")

# Exercise 2
print("\n ********** Exercise 2 ************\n")

print("Majority of List numbers")
x = majority(nums)
print(f"Majority element of list {nums} is equal to: {x}\n\n")

# Exercise 3
print("\n ********** Exercise 3 ************\n")

print(f"Check if list {elt1} contains duplicate value")

# result = containsDuplicate(nums)
result = containsDuplicate(elt1)
print(result,"\n\n")

x,y = 4,64

# Exercise 4
print("\n ********** Exercise 4 ************\n")

fact = factors(y)
print(f"factor of {y} will give {fact}\n\n")

# Exercise 5
print("\n ********** Exercise 5 ************\n")

print(f"Sum of the squares of positive value up to {x}: {sum_square_up(x)} \n\n")

issa,abdou,laity = ("Issa",22),("Abdou",17),("Pappa",35)
persons = [issa,abdou,laity]

# Exercise 6
print("\n ********** Exercise 6 ************\n")

print(f"Persons List: {persons} \n")
sort_person_list_by_age(persons)
print(f"Sorted list by age give: {persons}\n\n")

text = "Write a function that takes a list of words and a minimum length, and returns a new list containing only words that are longer than the specified length."
words = text.split()

# Exercise 7
print("\n ********** Exercise 7 ************\n")

k = 5
print(text)
print(f"list of words which the len > {k}:")
words_new_list = words_list_with_min_len(words,k)
print(words_new_list)

# Exercise 8
print("\n ********** Exercise 8 ************\n")

lnums = [1,3,5,2,1]
print(lnums)
print("Delete all occurences functions for 1")
num_list = delete_all(lnums,1)
print(num_list)

# Exercise 9
print("\n ********** Exercise 9 ************\n")

textcode = "afghjrwgh"

print(textcode)
encode_result = encoded_text(textcode)
print(f"Encoding of text <{textcode}> give <{encode_result}>")

# Exercise 10
print("\n ********** Exercise 10 ************\n")

textstr = "Sorted list by age give"
print(f"words length of <{textstr}> will give: {words_lengths(textstr)}")

# Exercise 11
print("\n ********** Exercise 11 ************\n")

# list_to_clean = ["cat", "er", "pillar"]
list_to_clean = ["cat", " ", "er", "", "pillar"]
print(f"function clean list of {list_to_clean} give: {cleanup(list_to_clean)}") 

# Exercise 12
print("\n ********** Exercise 12 ************\n")

# nested_list =[[1, 2, 3], [4, 5]]
nested_list =[[1, 2, 3], [], [], [4], [5]]
sum = nested_sum(nested_list)
print(f"Sum of the list {nested_list} give: {sum}")

# Exercise 13
print("\n ********** Exercise 13 ************\n")

print("Uncomment the code below (line 114) to execute the function")

# dict_persons()

# Exercise 14

print("\n ********** Exercise 14 ************\n")

uids = four_id_list_generated()
print(uids[:15])

# Exercise 15

print("\n ********** Exercise 15 ************\n")

# password = "AMMIPython@2025"
password = "AMMIPython2025"

strength_password = strongest_password_verify(password)

if(strength_password):
    print(f"password {password} is strong")
else:
    print(f"password {password} is not strong")

# Exercise 16
print("\n ********** Exercise 16 ************\n")

# tuple_list = (1,2,3,4)
tuple_list = (1,3,5)
print(f"Sum of even and odd numbers of tuple {tuple_list} give: {sum_of_even_and_odds(tuple_list)}\n")


# Exercise 17
print("\n ********** Exercise 17 ************\n")

sa_countries = ["Brazil", "Venezuela", "Argentina", "Ecuador", "Bolivia", "Peru"]
sa_countries_result = length_counts(sa_countries)
print(sa_countries_result)

# Exercise 18
print("\n ********** Exercise 18 ************\n")


s = "eggg"
t = "addd"
# s = "foo"
# t = "bar"

print(isomorphic_string(s,t))

# Exercise 19

print("\n ********** Exercise 19 ************\n")


v1 = [1,2,3,4]
v2 = [3,2,1,0]

print(f"Dot product of {v1} and {v2} give: {doc_product(v1,v2)}\n")

# Exercise 20
print("\n ********** Exercise 20 ************\n")

A = [ [1,2,3],[4,5,6] ]
# A = [ [1,2],[4,5] ] # Multiplication matricielle impossible
B = [ [4,5], [1,2], [0, 1] ]

C = mat_mul(A,B)
print(C,"\n")

# Exercise 21
print("\n ********** Exercise 21 ************\n")


Ex = [1,2,3,4,5]
print (f" The list before reversed is {Ex}\n")
Ex = reverse(Ex)
print (f" The list after reversed is {Ex}\n")

# Exercise 22
print("\n ********** Exercise 22 ************\n")

s = "abas"
result = palindrom(s)
if(result):
    print(f"{s} is a palindrom")
else:
    print(f"{s} is not a palindrom")

# Exercise 23
print("\n ********** Exercise 23 ************\n")

k = 4
print(f"Factoriel of {k} will give : {factoriel(k)}")

# Exercise 24
print("\n ********** Exercise 24 ************\n")

k = 10
print(f"Fibonacci of {k} will give : {fibonacci(k)}")

# Exercise 25
print("\n ********** Exercise 25 ************\n")

start,stop = 19,31
prime_list = prime_number(start,stop)
print(f"List of prime number between {start} and {stop} is {prime_list}")

# Exercise 26
print("\n ********** Exercise 26 ************\n")
print("Uncomment the code below ")

## copy file

input_txt= "input.txt"
output_txt= "output.txt"

# result = copy_file(input_txt,output_txt)
# if (result):
#     print("File successfully copied!")
# else:
#     print(f"Error: {input_txt} dosn't exist make sure you give the right path")