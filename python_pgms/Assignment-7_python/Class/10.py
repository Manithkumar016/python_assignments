# 10) Write a Python program to get the class name of an instance in Python.

class Pclass:
    def __init__(self) -> None:
        pass
obj =Pclass()

class_name = obj.__class__.__name__

print(class_name)