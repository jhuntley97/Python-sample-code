#Jwaun Huntley
#2/28/19

# Multiplies all values in a list

def multiplyList(numbers):
    total = 1
    for n in numbers:
        total *= n
#        total = total * n
    return(total)
n = (1, 5, 3, -8, 10)

print (multiplyList (n))

print (multiplyList([1, 2, 3]))
