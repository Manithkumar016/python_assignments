
# 20. Write a Python program to remove all consecutive duplicates of a given string.

s="aabbbcdcef"
i=0
while(i<len(s)-1):
    # print(i)
    if s[i]==s[i+1]:
        s=s[0:i]+s[i+1:]
        
    else:
        i=i+1

print(s)

