# 7) Write a Python class to reverse a string word by word. 
# Input string : 'hello .py' Expected Output : '.py hello' 

str= 'hello .py'

class Reverse:
    def __init__(self) -> None:
        pass
    def reverse_string(self,str):
        list=str.split(" ")
        list.reverse()
        s= " ".join(list)
        print(s)
        
r = Reverse()
r.reverse_string(str)