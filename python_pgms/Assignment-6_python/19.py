# 19. Write a Python program to remove duplicates from a list of lists.
# Sample list : [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
# New List : [[10, 20], [30, 56, 25], [33], [40]]

Sample_list = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
list=[]
for i in Sample_list:
    if i not in list:
        list.append(i)

print(list)