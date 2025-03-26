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