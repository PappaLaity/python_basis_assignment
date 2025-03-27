def words_list_with_min_len(words:list, k)->list:
    limitedword = []
    for word in words:
        if (len(word) > k):
            limitedword.append(word)
    return limitedword

def encoded_text(text:str)->str:
    textList = list(text)
    for i in range(len(textList)):
        textList[i] = chr(ord(textList[i])+2)
    return "".join(textList)

def words_lengths(text:str)->list:
    words_list  = text.split()
    nums_list = []
    for elt in words_list:
        nums_list.append(len(elt))
    return nums_list

def is_special_char(chaine:str)->bool:
    for c in chaine:
        if not ( (c.isalpha()) or c.isdigit() or c == " "):
            return True
    return False


def strongest_password_verify(password:str)->str:
    digit = any(char.isdigit() for char in password)
    upper = any(char.isupper() for char in password)
    lower = any(char.islower() for char in password)
    special = is_special_char(password)
    return (digit and upper and lower and special) 

def isomorphic_string(s:str,t:str)->bool:
    result = True
    if(len(s) != len(t)):
        return False
    for i in range(len(s)):
        for j in range(len(t)):
            if s[i] == s[j] and i!=j :
                result *= (t[i] == t[j])
    return bool(result)