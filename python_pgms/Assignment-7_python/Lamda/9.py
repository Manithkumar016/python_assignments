# 9) Write a Python program to find the elements of a given list of strings that contain specific substring using lambda. 
# Original list: ['red', 'black', 'white', 'green', 'orange'] 
# Substring to search: ack Elements of the said list that contain specific substring: ['black'] Substring to search: abc Elements of the said list that contain specific substring: [] 

Original_list = ['red', 'black', 'white', 'green', 'orange'] 

substring="abc"
list=[]

element = lambda substring,i: substring in i

for i in Original_list:
    if element(substring,i):
        list.append(i)

print(list)

