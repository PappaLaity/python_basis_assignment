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
