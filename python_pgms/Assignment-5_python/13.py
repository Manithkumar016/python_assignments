# 13. Take 10 integers from keyboard using loop and print their average value on the screen.

sum=0
for i in range(10):
    n = int(input("enter a number : "))
    sum=sum+n
avg = sum/10
print(avg)
