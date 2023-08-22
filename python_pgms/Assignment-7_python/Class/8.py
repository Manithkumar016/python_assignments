# 8) Write a python class which has 2 methods get_string and print_string. get_string takes a string from the user and print_string prints the string in reverse order

class String_Methods:
    def __init__(self) -> None:
        pass
    def get_string(self):
        input("enter a string: ")
    def print_string(self,str):
        list1=list(str)
        list1.reverse()
        s="".join(list1)
        print(s)

s= String_Methods()
s.get_string()
s.print_string("pace wisdom")