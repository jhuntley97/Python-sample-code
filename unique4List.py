#Jwaun Huntley
#2/28/19

#Function receieves list and prints out only the unique elements

def uniqueList(numbers):
    newList = []
    for n in numbers:
        if n not in newList:
            newList.append(n)
    return newList

print(uniqueList([1, 2, 2, 3, 3, 3, 7, 4, 3, 10]))
