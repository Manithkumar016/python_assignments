# 12. Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters.

s="ABcdefgh"
count=0
for i in range(0,4):
    if s[i].isupper():
        count+=1
if count>=2:
    print(s.upper())
else:
    print(s)
