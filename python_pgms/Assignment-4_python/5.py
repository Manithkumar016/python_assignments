# 5. Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
# Sample String : 'abc', 'xyz' 
# Expected Result : 'xyc abz'

s="abc"
t="xyz"
print(t[0:2]+s[2:]+" "+s[0:2]+t[2:])
