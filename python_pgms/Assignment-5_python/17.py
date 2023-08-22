# 17. Using range(1,101), make three list, 
# one containing all even numbers
# one containing all odd numbers 
# One containing only prime numbers..

list1=[]
list2=[]
list3=[]
def isPrime(n):
    count =0
    if n==1:
        return True
    else:
        for i in range(2,n+1):
            if n%i==0:
                count+=1
        if count==1:
            return True
        else: return False

for i in range(1,101):
    if i%2==0:
        list1.append(i)
    elif i%2!=0:
        list2.append(i)
    if isPrime(i):
        list3.append(i)

print(list1,"\n")
print(list2,"\n")
print(list3,"\n")
