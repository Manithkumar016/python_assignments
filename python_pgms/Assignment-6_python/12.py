# 12. Write a Python program to get the maximum and minimum value in a dictionary. 

dict ={1:1,2:7,3:3,4:0}
n=list(dict.items())
max=0

for i in dict:
    if dict[i]>max:
        max=dict[i]

min = max
for i in dict:
    if dict[i]<min:
        min=dict[i]

print(f"max : {max} and min : {min}")
