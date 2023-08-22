# 13. Write a Python program to remove duplicates from Dictionary.

dict={1:1,2:2,3:2,4:3,5:4,6:4,7:1,8:8}
dict2={}

for i in range(1,len(dict)+1):
    if dict[i] not in dict2.values():
        dict2[i]=dict[i]

print(dict2)
