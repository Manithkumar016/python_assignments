# 11. Write a Python program to sort a dictionary by key.

sample_dict = {1:1,3:3,2:2}
n=list(sample_dict.items())
print(n)
def swap(i,j,n):
    temp = n[i]
    n[i]=n[j]
    n[j]=temp

for i in range(len(n)):
    for j in range(len(n)):
        if n[i]>n[j]:
            swap(i,j,n)

print(n)