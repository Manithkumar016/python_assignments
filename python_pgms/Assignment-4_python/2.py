# 2. Write a Python program to count the number of characters (character frequency) in a string. 
# Sample String : google.com'
# Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}

s="google.com"
k={}
for i in s:
    if i in k.keys():
        k[i]+=1
    else:
        k[i]=1

print(k)
