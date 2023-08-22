
# 7. Write a Python program that counts the number of elements within a list that are greater than 30.

list = [20,20,35,30,26,65,54]
count=0
for i in list:
    if i>30:
        count+=1

print(count)