# 10) Write a Python program to sort a given mixed list of integers and strings using lambda. Numbers must be sorted before strings. 
# Original list: [19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1] 
# Sort the said mixed list of integers and strings: [1, 10, 12, 19, 'blue', 'green', 'green', 'red', 'white']

Original_list=[19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1] 
list2=[]
list3=[]
sort_list=lambda list:sorted(list)

for i in Original_list:
    if str(i).isnumeric():
        list2.append(i)
    else:
        list3.append(i)
print(sort_list(list2)+sort_list(list3))