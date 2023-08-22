# 7. Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
# Sample String : 'The lyrics is not that poor!'
# 'The lyrics is poor!'
# Expected Result : 'The lyrics is good!'
# 'The lyrics is poor!'


s="The lyrics is not that poor!"

def madestring(s):
    t=s.split(" ")
    for i in t:
        if i=="not":
            print(t.index('not'))
            t[t.index('not'):t.index('poor!')+1] = ["good!"]
            return t
    return t

print(" ".join(madestring(s)))
