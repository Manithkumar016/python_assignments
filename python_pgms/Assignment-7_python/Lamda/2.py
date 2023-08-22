
# 2) Write a Python program to sort a list of tuples using Lambda. 
# Original list of tuples: [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
# Sorting the List of Tuples: [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]


list1 = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

sorted_list = sorted(list1, key=lambda x: x[1])
print("\nSorting the List of Tuples:", sorted_list)

