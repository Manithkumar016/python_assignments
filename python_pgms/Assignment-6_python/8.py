# 8.  Write a Python program to sum all the items in a dictionary.

sample_dict = {'apple': 3, 'banana': 1, 'cherry': 2, 'date': 4}
sum =0

for i in sample_dict:
    sum=sum+sample_dict[i]

print(sum)