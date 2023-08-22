# 10. Write a Python program to remove a key from a dictionary. 

# 10. Write a Python program to remove a key from a dictionary. 

sample_dict = {'apple': 3, 'banana': 1, 'cherry': 2, 'date': 4}
n=input("enter a key to pop: ")

try:
    sample_dict.pop(n)
except:
    print("entered a  key is not valid\n")


print(sample_dict)