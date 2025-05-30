import string


def destroy_elements(elt1:list, elt2:list)->list:
    for item in elt2:
        elt1.remove(item)
    return elt1

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

def containsDuplicate(nums:list)->bool:
    n = len(nums)
    # result = True
    for number in nums:
        if(nums.count(number)>1):
            return True
    return False


def age_tuple(e:tuple)->int:
    return e[1]

def sort_person_list_by_age(l:list)->list:
    return l.sort(key=age_tuple)

def delete_all(nums:list,value:int)->list:
    new_list = []
    for elt in nums:
        if elt != value :
            new_list.append(elt)
    return new_list

def cleanup(words_list:list)->str:
    for words in words_list:
        if words == "" or words==" ":
            words_list.remove(words) 
    return " ".join(words_list)

def nested_sum(list_of_list:list)->int:
    sum = 0
    for sub_list in list_of_list:
        if len(sub_list) > 0:
            for elt in sub_list:
                sum+=elt
    return sum
def length_counts(string_list:str)->dict:
    dict_lenght = {}
    for elt in string_list:
        if len(elt) not in dict_lenght.keys():
            occur = 0
            for elt2 in string_list:
                if(len(elt) == len(elt2)):
                    occur +=1
        dict_lenght[len(elt)] = occur
    return dict_lenght

def doc_product(v1:list,v2:list)->int:
    if len(v1) != len(v2):
        return "Vectors should be equal"
    else:
        product=0
        for i in range(len(v1)):
            product+= v1[i]*v2[i]
        return product

def mat_mul(a:list, b:list):
    #  Return null if not m*n and n*p
    if(len(a[0])!=len(b)):
        return "Multiplication matricielle impossible\n"
    c = []
    for i in range(len(a)):
        c.append([0 for k in range(len(b[0]))])

    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                c[i][j] += a[i][k]*b[k][j]
    return c


def reverse(nums_list:list)->list:
    longueur = int(len(nums_list)/2)
    for i in range(longueur):
        a = nums_list[i]
        nums_list[i] = nums_list[-i-1]
        nums_list[-i-1] = a
    
    return nums_list

def four_id_list_generated():
    return [ f"{a}{b}{c:02d}" for a in string.ascii_lowercase for b in string.ascii_lowercase for c in range(100)]