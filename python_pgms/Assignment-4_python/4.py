# 4. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
# Sample String : 'restart'
# Expected Result : 'resta$t'

string = 'restart'

def madestring(string):
        t=string[1:]
        return t.replace(string[0],'$')

print(string[0]+madestring(string))

