# 14. Print multiplication table of 24, 50 and 29 using loop.

def table(n):
    for i in range(1,11):
        print(f"{n}*{i}={n*i}")
    print("__________________")

table(24)
table(50)
table(29)
