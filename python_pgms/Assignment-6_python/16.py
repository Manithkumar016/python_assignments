# 16. Write a Python program to find the highest 3 values in a dictionary.

d ={1:1,2:2,3:1,4:4,5:7,6:5,7:1}

sorted_dict = sorted(d.values()) 

print(sorted_dict[-3:])