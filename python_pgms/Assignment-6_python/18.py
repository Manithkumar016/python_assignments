# 18. Write a Python program to check if all dictionaries in a list are empty or not.
# Sample list : [{},{},{}]
# Return value : True
# Sample list : [{1,2},{},{}]
# Return value : False

list=[{},{},{}]
def isempty(i):
    if len(i)==0:
        return True
    else:
        return False
    

b=True
for i in list:
    if isempty(i):
        continue
    else:
        b=False

print(b)



