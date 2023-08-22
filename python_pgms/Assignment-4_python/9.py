# 9. Write a Python program to remove the nth index character from a nonempty string.

s="abcdefghi"
n=3
def remove_n(n,s):
    return s[0:n]+s[n+1:]

print(remove_n(n,s))
