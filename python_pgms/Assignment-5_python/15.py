# 15. Take integer inputs from user until he/she presses q ( Ask to press q to quit after every integer input ). Print average and product of all numbers.

n=""
i=''
sum=0
product=1
while(i!='q'):
    i=input("enter a integer: ")
    if i=='q':
        break
    else:
        n=n+i
    l=input("do you want to quit(q/n): ")
    if l=="q":
        break

for i in range(len(n)):
    sum=sum+int(n[i])
    product=product*int(n[i])

print("avg : ",(sum/len(n)))
print("---------------")
print("product: ",product)
