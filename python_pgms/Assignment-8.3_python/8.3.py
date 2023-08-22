# A balanced delimiter starts with an opening character ((, [, {), ends with a matching closing character (), ], } respectively), and has only other matching delimiters in between. A balanced delimiter may contain any number of balanced delimiters.

# Examples
# The following are examples of balanced delimiter strings:

# ()[]{}
# ([{}])
# ([]{})
# The following are examples of invalid strings:
# ([)]
# ([]
# [])
# ([})
# Input is provided as a single string. Your output should be True or False according to whether the string is balanced. For example:

# Input:
# ([{}])
# Output:
# True


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
s="([{}]){"
h=st.isValid(s)
if len(h)==0:
    print("True")
else:
    print("False")