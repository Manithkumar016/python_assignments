# 4. Write a Python script to check if a given key already exists in a dictionary. 

def key_check(key,dict):
    h=False
    for i in dict:
        if i==key:
            h=True
    return h

dict={1:1,2:2,3:3}
print(key_check(2,dict))
print(key_check(4,dict))