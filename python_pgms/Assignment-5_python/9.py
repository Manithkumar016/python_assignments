# 9. A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
# Ask user for quantity
# Suppose, one unit will cost 100.
# Judge and print total cost for user.

Q = int(input("enter the quantity: "))
price=Q*100

if price>1000:
    price=price*0.9

print(price)

