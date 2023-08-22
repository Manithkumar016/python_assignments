# 18. From the two list obtained in previous question, make new lists, containing only numbers which are divisible by 4, 6, 8, 10, 3, 5, 7 and 9 in separate lists.

def newlist(n):
    list=[]
    for i in range(1,101):
        if i%n==0:
            list.append(i)
    return list
# 4, 6, 8, 10, 3, 5, 7 and 9
print(newlist(4),"\n")
print(newlist(6),"\n")
print(newlist(8),"\n")
print(newlist(10),"\n")
print(newlist(3),"\n")
print(newlist(5),"\n")
print(newlist(7),"\n")
print(newlist(9),"\n")
