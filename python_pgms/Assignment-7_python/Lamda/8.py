# 8) Write a Python program to check whether a given string contains a capital letter, a lower case letter, a number and a minimum length using lambda. Minimum length : 10 input string: PaceWisd0m o/p: valid string 


contains_capital = lambda str: any(i.isupper() for i in str)
contains_lower = lambda str: any(i.islower() for i in str)
min_length = lambda str: len(str)>=10
isnumber = lambda str:any(i.isnumeric() for i in str)

check_string = lambda str:contains_capital(str) and contains_lower(str) and min_length(str) and isnumber(str)

print(check_string("PaceWisd0m"))