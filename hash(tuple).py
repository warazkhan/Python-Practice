#Given an integer and another space-separated integers as input, create a tuple of those  integers. 
#Then compute and print the result of tuple.

numberOfElements= int(input())
inputslist= input().split()
numbers=[]

for i in range (0, numberOfElements):
    numbers.append(int(inputslist[i]))

inputsTuple = tuple(numbers)
resultHashValue = hash(inputsTuple)

print(resultHashValue)