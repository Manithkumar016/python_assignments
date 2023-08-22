# 15. Write a Python program to count repeated characters in a string.
# Sample string: 'thequickbrownfoxjumpsoverthelazydog'
# Expected output :
# o 4
# e 3
# u 2
# h 2
# r 2
# t 2

s= 'thequickbrownfoxjumpsoverthelazydog'
k={}
for i in s:
    if i in k.keys():
        k[i]+=1
    else:
        k[i]=1

for key,value in k.items():
    if k[key]>=2:
        print(key,value)

