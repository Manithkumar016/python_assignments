# 12. A student will not be allowed to sit in exam if his/her attendence is less than 75%.
# Take following input from user
# Number of classes held
# Number of classes attended.
# And print
# percentage of class attended
# Is student is allowed to sit in exam or not.

num_classes=int(input("Number of classes held: "))
att_classes=int(input("Number of classes attended: "))

n=(att_classes/num_classes)*100

print("attendence % : ",n,"%")

if n>=75 :
    print("you can attend exams :)")
else:
    print("your attendence is very low ,you are not allowed to attend exams :(")

