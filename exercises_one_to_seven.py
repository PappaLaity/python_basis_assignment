
# ************* Exercise 1 ************************

# destroy_elements([1, 2, 3], [4, 5]) => [1, 2, 3]
elt1,elt2 = [1,2,3,5],[1,2]
def destroy_elements(elt1:list, elt2:list)->list:
    result_list = []
    for item in elt1:
        # print(item)
        if (item not in elt2):
            result_list.append(item)
    return result_list

l = destroy_elements(elt1,elt2)
print(f"Destroy elements of {elt1} and {elt2}")
print(l)
# ************* End Ex 1   ************************

# ************* Exercise 2 ************************
nums  = [2,2,1,5,1,1,2,5,5,2,1,1,5,5,5,5,5,5]
def majority(nums:list)->int:
    n = len(nums)
    occur  = 1
    majority = -1
    for i in range(n):
        occur = 1
        for j in range(1,n):
            if ((nums[i] == nums[j]) and (i != j)):
                occur += 1
            if (occur >= int(n/2)):
                majority = nums[i]
                return majority
    
    return majority

print("Majority of List numbers")
x = majority(nums)
if (x != -1 ):
    print(x)
# ************* End Ex 2   ************************

# ************* Exercise 3 ************************

nums = [1,2,3,5,2]

def containsDuplicate(nums:list)->bool:
    n = len(nums)
    # result = True
    for number in nums:
        if(nums.count(number)>1):
            return True
    return False

print("Check if list contains duplicate value")

result = containsDuplicate(nums)
print(result)

# ************* End Ex 3  ************************

# ************* Exercise 4 ************************
def factors(number:int)->list:
    result = []
    for i in range(number):
        if(number%(i+1)==0):
            result.append(i+1)

    return result

y =64
x = factors(y)
print(f"factor de {y} donnera {x}")

# ************* End Ex 4   ************************

# ************* Exercise 5 ************************
def sum_square_up(number:int)->int:
    if(number <= 0 ):
        return "The input number should be positive"
    square_sum = 0
    for i in range(number):
        square_sum += (i+1)**2
    return square_sum

print("Sum of the squares of positive value up to x")
print(sum_square_up(4))
# ************* End Ex 5   ************************


# ************* Exercise 6 ************************
issa,abdou,laity = ("Issa",22),("Abdou",17),("Pappa",35)
persons = [issa,abdou,laity]

def age_tuple(e:tuple)->int:
    return e[1]

print(persons)
persons.sort(key=age_tuple)
print(persons)
# ************* End Ex 6   ************************

# ************* Exercise 7 ************************

text = "Write a function that takes a list of words and a minimum length, and returns a new list containing only words that are longer than the specified length."
words = text.split()
def words_list_with_min_len(words:list, k)->list:
    limitedword = []
    for word in words:
        if (len(word) > k):
            limitedword.append(word)
    return limitedword

words_new_list = words_list_with_min_len(words,5)
print(words_new_list)

# ************* End Exo 7   ************************

# ************* Exercise 8 ************************
nums = [1,3,5,2,1]
def delete_all(nums:list,value:int)->list:
    new_list = []
    for elt in nums:
        if elt != value :
            new_list.append(elt)
    return new_list

print("Delete all occurences functions")
num_list = delete_all(nums,1)
print(num_list)
# ************* End Exo 8 ************************



# ************* Exercise n ************************
# ************* End Ex n   ************************