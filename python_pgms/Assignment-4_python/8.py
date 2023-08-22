# 8. Write a Python function that takes a list of words and returns the length of the longest one. 

list =["abc","abcdef","a"]

def longword(list):
    max =0
    for i in list:
        if len(i)>max:
            max=len(i)
    return max

print(longword(list))
