# 9. Write a Python program to multiply all the items in a dictionary.
sample_dict = {'apple': 3, 'banana': 1, 'cherry': 2, 'date': 4}
mul=1

for i in sample_dict:
    mul=mul*sample_dict[i]

print(mul)