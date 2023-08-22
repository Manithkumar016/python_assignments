# 5. Write a Python program to calculate the sum and average of n integer numbers (input from the user). Input 0 to finish

n=int(input("enter a number: "))
sum=0
if n==0:
    pass
else:
    for i in range(n+1):
        sum =sum+i
avg =sum/n
print("sum: ",sum ,"Avg: ",avg)
