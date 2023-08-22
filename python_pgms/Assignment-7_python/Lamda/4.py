# 4) Write a Python program to find if a given string starts with a given character using Lambda.

str="pace wisdom"
character = "p"

check_string=lambda str,character: character==str[0]

print(check_string(str,character))