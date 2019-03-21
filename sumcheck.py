# Jwaun Huntley
# 3/7/19

# Checks if the sum of two user inputs are equal to, greater than, or less than

number1 = int(input("Enter in number 1: "))
number2 = int(input("Enter in number 2: "))

def numberCheck(nl, n2):
    if n1 + n2 == 10:
        print("Equal")
    elif n1 + n2 > 10:
            print("Greater Than")
    else:
        print("Less Than")

#numberCheck(number1, number2)
print(numberCheck(number1, number2))
