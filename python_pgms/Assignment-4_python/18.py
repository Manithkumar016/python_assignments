
# 18. Write a Python program to swap comma and dot in a string.
# Sample string: "32.054,23"
# Expected Output: "32,054.23"

s="32.054,23"
t=list(s)
for i in range(len(t)):
    if t[i]=='.':
        t[i]=','
    elif t[i]==',':
        t[i]='.'

print(''.join(t))
