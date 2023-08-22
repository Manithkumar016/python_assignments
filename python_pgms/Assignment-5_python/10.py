# 10. A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
# Ask user for their salary and year of service and print the net bonus amount.

sal= int(input("enter the salary: "))
exp=int(input("enter year of service: "))

if exp>=5:
    sal=sal+sal*0.05

print(sal)

