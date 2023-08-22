# 16. Take inputs from user to make a list. Again take one input from user and search it in the list and delete that element, if found. Iterate over list using for loop.


list=[]
i=""
print("enter 'done' to 'Quit'")
print("-----------------------")
while(i!='q'):
    i=input("enter a input: ")
    if i=='done':
        break
    else:
        list.append(i)

m=input("enter a search value: ")
for k in list:
    if k==m:
        list.remove(m)

print(list)

