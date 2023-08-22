# 1. Write a Python script to sort (ascending and descending) a dictionary by value.

sample_dict = {'apple': 3, 'banana': 1, 'cherry': 2, 'date': 4}

def swap(i,j,n):
    temp=n[i]
    n[i]=n[j]
    n[j]=temp

def sort_dict(sample_dict,s):
    n=list(sample_dict.items())
    if s.upper()=="ASC":
        for i in range(len(n)):
            for j in range(len(n)):
                if n[i][1]>n[j][1]:
                    swap(i,j,n)

    else:
        for i in range(len(n)):
            for j in range(len(n)):
                if n[i][1]<n[j][1]:
                    swap(i,j,n)
    return dict(n)

print(sort_dict(sample_dict,"asc"))
print(sort_dict(sample_dict,"dsc"))
