# 2. Write a Python script to add a key to a dictionary.
# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}
dict={0: 10, 1: 20}

n=int(input("enter key: "))
m=int(input("enter the value: "))

dict[n]=m

print(dict)