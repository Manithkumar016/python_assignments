# 2) Write a Python class to find validity of a string of parentheses, '(', ')', '{', '}', '[' and ']. These brackets must be close in the correct order, for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid.

class Stackclass:
    def __init__(self): 
        pass
    def isValid(self,s):
        stk = []
        for i in s:
            if s[0]==")" or s[0]=="}" or s[0]=="]":
                stk.append(1)
                break
            elif i=="(" or i=="{" or i=="[":
                stk.append(i)
            elif i==")":
                if stk[-1]=="(":
                    stk.pop()
            elif i=="}":
                if stk[-1]=="{":
                    stk.pop()
            elif i=="]":
                if stk[-1]=="[":
                    stk.pop()
        return stk

st = Stackclass()
s="({[)]"
h=st.isValid(s)
if len(h)==0:
    print("Valid")
else:
    print("Not Valid")